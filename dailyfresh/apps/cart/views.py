from django.views.decorators.http import require_POST
from utils.views import json_view
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Cart
from apps.goods.models import Goods


@login_required
@require_POST
@json_view
def add_to_cart(request):
    goods_id = int(request.POST['goods_id'])
    goods_num = int(request.POST['goods_num'])
    goods = Goods.objects.get(id=goods_id)
    if goods.goods_stock < goods_num:
        return {'code':2, 'content': 'not enough'}
    Cart.add_one_object(user=request.user, goods=goods, goods_num=goods_num)
    return {'code': 1, 'content': 'add cart ok'}


@login_required
@require_POST
@json_view
def delete_from_cart(request):
    cart_id = int(request.POST['cart_id'])
    Cart.objects.get(user=request.user, id=cart_id).delete()
    return {'code': 1, 'content': 'delete cart ok'}


@login_required
def cart(request):
    cart_li = Cart.objects.filter(user=request.user).order_by("-create_time")
    total = 0
    count = 0
    for item in cart_li:
        item.img = item.goods.image_set.all()[0].img_url
        item.price = "%.2f" % item.goods.goods_price
        item.total = "%.2f" % (item.goods.goods_price * item.goods_num)
        total += (item.goods.goods_price * item.goods_num)
        count += item.goods_num
    return render(request, 'cart.html', {'cart':cart_li, 'total':total, 'count':count})


@login_required
@require_POST
@json_view
def update_cart(request):
    cart_id = request.POST['cart_id']
    goods_count = request.POST['goods_count']
    goods_count = int(goods_count)
    cart_obj = Cart.objects.get(user=request.user, id=cart_id)
    if cart_obj.goods.goods_stock < goods_count:
        return {'code':2, 'content': 'not enough'}
    cart_obj.goods_num = goods_count
    cart_obj.save()
    return {'code': 1, 'content': 'update cart ok'}
