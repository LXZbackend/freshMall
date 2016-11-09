from django.views.decorators.http import require_POST
from utils.views import json_view
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import SOrder, SOrderGoods
from apps.goods.models import Goods
from apps.address.models import Address
from apps.cart.models import Cart
from .enums import *
from django.core.paginator import Paginator, EmptyPage
import json


@login_required
def my_order(request, page):
    user = request.user
    order_li_all = SOrder.objects.filter(user=user).order_by('-create_time')
    for item in order_li_all:
        item.ctime = item.create_time.strftime('%Y-%m-%d %H:%M:%S')
        item.status = ORDER_TYPE[item.order_status]
        item.goods_li = []
        sorder_items = SOrderGoods.objects.filter(sorder=item)
        for sorder_item in sorder_items:
            goods = sorder_item.goods
            goods.img = goods.image_set.all()[0].img_url
            goods.price = "%.2f" % sorder_item.goods_price
            goods.count = sorder_item.goods_count
            goods.total = "%.2f" % (sorder_item.goods_price * goods.count)
            item.goods_li.append(goods)
        item.total = "%.2f" % (item.total_amount + item.ex_price)
        item.ex_price = "%.2f" % item.ex_price
    paginator = Paginator(order_li_all, LIST_PAGE_CAPACITY)
    page = int(page)
    try:
        order_li = paginator.page(page)
    except EmptyPage:
        order_li = paginator.page(paginator.num_pages)
        page = paginator.num_pages
     # 分页页数显示计算
    num_pages = paginator.num_pages
    if num_pages <= 5:
        pages = paginator.page_range
    elif (num_pages - page) < 2:
        pages = [x for x in range(num_pages-4, num_pages+1)]
    elif page < 3:
        pages = [x for x in range(1, 6)]
    else:
        pages = [x for x in range(page-2, page+3)]
    pre_page = page - 1
    next_page = page + 1 if page < num_pages else 0

    return render(request, 'user_center_order.html', {'order_li':order_li, 'pre_page':pre_page, 'next_page':next_page, 'pages':pages, 'active_page':page})


@login_required
@require_POST
@json_view
def add_order(request):
    user = request.user
    order_json = request.body.decode('utf-8')
    order_data = json.loads(order_json)
    # 判断库存
    for item in order_data['goods']:
        goods = Goods.objects.get(id=item['goods_id'])
        if goods.goods_stock < item['count']:
            return {'code':2, 'content':'not enough'}
    # 须做地址判断，若不存在，则需反馈
    address = Address.objects.get(id=order_data['addr_id'])
    # 快递费暂时默认写死
    order_obj = SOrder.add_one_object(user=user, addr=address, ex_price=10.0)
    # 遍历添加order_goods
    total_amount = 0.0
    total_count = 0
    for item in order_data['goods']:
        goods = Goods.objects.get(id=item['goods_id'])
        total_amount += goods.goods_price*item['count']
        total_count += item['count']
        SOrderGoods.add_one_object(sorder=order_obj, goods=goods, goods_price=goods.goods_price, goods_count=item['count'])
        goods.goods_stock -= item['count']
        goods.goods_sales += item['count']
        goods.save()
    order_obj.total_amount = total_amount
    order_obj.total_count = total_count
    order_obj.save()
    carts = order_data['carts']
    if carts:
        Cart.objects.filter(id__in=carts).delete()
    return {'code':1, 'content':'add order ok'}


@login_required
def commit_order(request):
    user = request.user
    try:
        address = Address.objects.get(user=user)
    except Address.DoesNotExist:
        address = None
    # ?g=1@2,3@4
    goods_str = request.GET['g']
    goods_li = []
    total_count = 0
    total_amount = 0
    for item in goods_str.split(','):
        goods_id = item.split('@')[0]
        goods_count = int(item.split('@')[1])
        goods = Goods.objects.get(id=goods_id)
        goods.img = goods.image_set.all()[0].img_url
        goods.price = "%.2f" % goods.goods_price
        goods.total = "%.2f" % (goods.goods_price * goods_count)
        goods.count = goods_count
        total_amount += (goods.goods_price * goods_count)
        total_count += goods_count
        goods_li.append(goods)
    query_str = request.META['QUERY_STRING']
    ex_price = '10.00'
    total = "%.2f" % (total_amount + 10)
    total_amount = "%.2f" % total_amount
    carts = request.GET.get('c', None) 
    if carts != None:
        carts = carts.split(',')
        carts = [int(cart_id) for cart_id in carts]
    else:
        carts = []
    return render(request, 'place_order.html', {'address':address, 'goods_li':goods_li, 'total_amount':total_amount, 'total_count':total_count, 'query_str':query_str, 'total':total, 'ex_price':ex_price, 'carts':carts})


@login_required
@require_POST
@json_view
def finish_order(request):
    order_id = request.POST['order_id']
    try:
        sorder = SOrder.objects.get(user=request.user, id=order_id)
    except SOrder.DoesNotExist:
        return {'code':2, 'content':'order does not exist'}
    sorder.order_status = UNCOMMENTED
    sorder.save()
    return {'code':1, 'content':'finish order ok'}


@login_required
def comment(request):
    if request.method == 'GET':
        order_id = request.GET['o']
        item = SOrder.objects.get(user=request.user, id=order_id)
        item.ctime = item.create_time.strftime('%Y-%m-%d %H:%M:%S')
        item.status = ORDER_TYPE[item.order_status]
        item.goods_li = []
        sorder_items = SOrderGoods.objects.filter(sorder=item)
        for sorder_item in sorder_items:
            goods = sorder_item.goods
            goods.img = goods.image_set.all()[0].img_url
            goods.price = "%.2f" % sorder_item.goods_price
            goods.count = sorder_item.goods_count
            goods.total = "%.2f" % (sorder_item.goods_price * goods.count)
            item.goods_li.append(goods)
        item.total = "%.2f" % (item.total_amount + item.ex_price)
        item.ex_price = "%.2f" % item.ex_price
        return render(request, 'order_comment.html', {'item':item, 'goods_count':len(item.goods_li)})
    else:
        order_id = request.POST['order_id']
        sorder = SOrder.objects.get(user=request.user, id=order_id)
        goods_count = request.POST['goods_count']
        goods_count = int(goods_count)
        for i in range(1, goods_count+1):
            goods_id = request.POST['goods_id_%d' % i]
            content = request.POST.get('content_%d' % i, '')
            goods = Goods.objects.get(id=goods_id)
            sorder_goods = SOrderGoods.objects.get(sorder=sorder, goods=goods)
            sorder_goods.comment = content
            sorder_goods.save()
        sorder.order_status = FINISHED
        sorder.save()
        return redirect('/order/1')





