#coding=utf-8
from django.shortcuts import render
from models import *
# Create your views here.


def index(request):
	# 获取到所有的分类
	shopclass = goodsClass.objects.all()

	'''
	第一种想法是 找到向关联的表中的1对多中的1 ，通过分类找所以的商品
	但是这个在shell 下不报错 在这里报错
	获取到商品第一级分类
	获取一个商品类型下 id 为1 的对象
	shopclass =  goodsClass.objects.get(pk=1)
	通过这个找下面的所有的子 ，通过1 找多
	fruitlist = shopclass.goodslist_set.all()
	获取到所以商品列表  这时候显示的是所有的商品，需要进行赛选
	goodslist = goodsList.objects.all()
	'''
	# 第一种思路报错 只能通过遍历所有商品找出对应类别，存到一个列表中
	fruitlist = goodsList.objects.filter(goodsType=1)
	seafoodlist = goodsList.objects.filter(goodsType=2)
	meatlist = goodsList.objects.filter(goodsType=3)
	# fruitlist = goodsList.objects.filter(goodsType=1)
	print fruitlist,seafoodlist,meatlist



	dic={
	'firstclass':shopclass,
	'fruitlist':fruitlist,
	'seafoodlist':seafoodlist,
	'meatlist':meatlist


	}


	print shopclass


	return render(request, 'freshMall/index.html',dic)


def login(request):
	return render(request, 'freshMall/login.html')


def cart(request):
	return render(request, 'freshMall/cart.html')


def user_center_order(request):
	return render(request, 'freshMall/user_center_order.html')


def register(request):
	return render(request, 'freshMall/register.html')
