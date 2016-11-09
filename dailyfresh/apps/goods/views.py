from django.views.decorators.http import require_POST
from .logics import GoodsLogic
from utils.views import json_view
from django.shortcuts import render
from .enums import *
from apps.cart.models import Cart
from apps.profile.models import BrowseHistory
from django.db.models import Sum
from django.core.paginator import Paginator, EmptyPage
from haystack.generic_views import SearchView


def home_list_page(request):
    fruits = GoodsLogic.get_goods_by_type(FRUITS, HOME_ITEM_NUMS) 
    seafood = GoodsLogic.get_goods_by_type(SEAFOOD, HOME_ITEM_NUMS) 
    meat = GoodsLogic.get_goods_by_type(MEAT, HOME_ITEM_NUMS) 
    eggs = GoodsLogic.get_goods_by_type(EGGS, HOME_ITEM_NUMS) 
    vegetables = GoodsLogic.get_goods_by_type(VEGETABLES, HOME_ITEM_NUMS) 
    frozen = GoodsLogic.get_goods_by_type(FROZEN, HOME_ITEM_NUMS) 
    cart = {'goods_num__sum':0}
    if request.user.is_authenticated():
        cart = Cart.objects.filter(user=request.user).aggregate(Sum('goods_num'))
        if None == cart['goods_num__sum']:
            cart['goods_num__sum'] = 0
    return render(request,'index.html', {'fruits':fruits, 'seafood':seafood, 'meat':meat, 'eggs':eggs, 'vegetables':vegetables, 'frozen':frozen, 'cart':cart['goods_num__sum']})


def goods_detail(request, goods_id):
    goods = GoodsLogic.get_one_goods(goods_id)
    comments = goods.sordergoods_set.all().order_by('-create_time')[:30]
    for comment in comments:
        comment.ctime = comment.create_time.strftime('%Y-%m-%d %H:%M:%S')
        comment.user = comment.sorder.user.username
    new_goods_li = GoodsLogic.get_goods_by_type(goods.goods_type_id, limit=2, sort='new')
    cart = {'goods_num__sum':0}
    if request.user.is_authenticated():
        cart = Cart.objects.filter(user=request.user).aggregate(Sum('goods_num'))
        if None == cart['goods_num__sum']:
            cart['goods_num__sum'] = 0
        BrowseHistory.add_one_object(user=request.user, goods=goods)
    return render(request, 'detail.html', {'goods':goods, 'cart':cart['goods_num__sum'], 'new_goods_li':new_goods_li, 'comments':comments})


def goods_list(request, goods_type_id, page):
    goods_type_id = int(goods_type_id)
    page = int(page)
    sort = request.GET.get('sort', 'default')
    new_goods_li = GoodsLogic.get_goods_by_type(goods_type_id, limit=2, sort='new')
    goods_li_all = GoodsLogic.get_goods_by_type(goods_type_id, sort=sort)
    cart = {'goods_num__sum':0}
    if request.user.is_authenticated():
        cart = Cart.objects.filter(user=request.user).aggregate(Sum('goods_num'))
        if None == cart['goods_num__sum']:
            cart['goods_num__sum'] = 0
    paginator = Paginator(goods_li_all, LIST_PAGE_CAPACITY)
    try:
        goods_li = paginator.page(page)
    except EmptyPage:
        goods_li = paginator.page(paginator.num_pages)
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

    return render(request, 'list.html', {'sort':sort, 'type_name':GOODS_TYPE[goods_type_id], 'type_id':goods_type_id, 'new_goods_li':new_goods_li, 'goods_li':goods_li, 'cart':cart['goods_num__sum'], 'pre_page':pre_page, 'next_page':next_page, 'pages':pages, 'active_page':page})


class MySearchView(SearchView):
    
    def get_context_data(self, *args, **kwargs):
        context = super(MySearchView, self).get_context_data(*args, **kwargs)
        for result in context['page_obj'].object_list:
            result.object.img = result.object.image_set.all()[0].img_url
        return context

