from django.views.decorators.http import require_http_methods, require_POST
from utils.views import json_view
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from apps.address.models import Address
from .models import BrowseHistory


@login_required
def profile(request):
    try:
        address = Address.objects.get(user=request.user)
    except Address.DoesNotExist:
        address = None 

    # 不支持distinct去重，只能手动去重
    # browse_history = BrowseHistory.objects.filter(user=request.user).order_by('-create_time').distinct('goods')[:5]
    browse_history = BrowseHistory.objects.filter(user=request.user).order_by('-create_time')
    history_goods_li = []
    goods_ids = []
    num = 0
    for item in browse_history:
        goods = item.goods
        if goods.id not in goods_ids:
            num += 1
            goods_ids.append(goods.id)
            goods.price = "%.2f" % goods.goods_price
            goods.img = goods.image_set.all()[0].img_url
            history_goods_li.append(goods)
            if 5 == num:
                break
    return render(request, "user_center_info.html", {"address":address, "history_goods_li":history_goods_li})
