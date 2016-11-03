# coding=utf-8
from django.shortcuts import render, redirect
from django.http import *
from models import *
import deractor
import json
# Create your views here.
# 装饰器 对每个页面都得进行显示帐号


@deractor.login_name
def index(request, dic):
	# loginname = request.session.get("name")
	# print '这是session', loginname

	fruitlist = GoodsList.objects.filter(goodsType=1)
	dic['fruitlist'] = fruitlist
	# dic = {

	#     'fruitlist': fruitlist,
	#     # 'seafoodlist':seafoodlist,
	#     'user_name': loginname
	#     # 'meatlist':meatlist

	# }

	return render(request, 'freshMall/index.html', dic)


def registerHandle(request):
	# 注册的方法
	per = UserInfo()
	account = request.POST['user_name']
	pwd = request.POST["pwd"]
	email = request.POST["email"]

	per.account = account
	per.passswd = pwd
	per.email = email
	per.save()
	# print '这是名字', per.account
	# print request.method
	return redirect('/login/')


def loginHandle(request):
	# 登录验证
	receName = request.POST['uname']
	recePwd = request.POST['pwd']
	per = UserInfo.objects.get(account=receName)

	print per.passswd
	if per:
		if per.passswd == recePwd:
			# 如果登录成功  就把session 存到数据库
			request.session['name'] = receName
			# return render(request, 'freshMall/index.html')
			return redirect('/index/')

		else:
			return render(request, 'freshMall/register.html')
	# return render(request, 'freshMall/login.html')


def loginout(request):
	# 这是推出登录

	del request.session['name']  # 这是删除这个特定的
	# request.session.clear()
	# request.session.flush()
	return redirect('/index/')


def login(request):
	return render(request, 'freshMall/login.html')


def testform(request):
	# 这个方法是处理注册是异步检测账户是否存在的一个方法
	nameflag = False
	testname = request.POST['name']
	# testemail = request.POST['email']
	# print '这是验证的名高子',testname

	personlist = UserInfo.objects.all()
	for info in personlist:
		if info.account == testname:
			print info.account
			nameflag = True
	data = {'name': nameflag}
	return JsonResponse(data)


def detail(request, shopId):
	shopinfo = GoodsList.objects.get(pk=shopId)

	dic = {

		'shopinfo': shopinfo,

	}

	return render(request, 'freshMall/detail.html', dic)


@deractor.login_name
def cart(request, dic):
	# loginname = request.session.get("name",default='')
	if dic['user_name'] != '':
		per = UserInfo.objects.get(account=dic['user_name'])
		# print '这是id',per.id
		# print type(per)
		carlist = ShoppingCart.objects.filter(userId=per.id)
		# print '这是商品',carlist
		# print dir(carlist)
		for temp in carlist:
			# print temp.goodsId.goodsDetail
			print temp
		dic['carlist'] = carlist
		# dic={
		# 	'carlist':carlist
		# }

	return render(request, 'freshMall/cart.html', dic)


def cartHandle(request):
	'''
	我这里犯的错误:通过filter 查询出来的是一个迭代的对象,你直接对他.id 是不对的,是什么都没有的  你得迭代之后在id,才行
	如果是 get 查询的 返回的是一个对象,所以直接可.id 等属性


	'''

	print "*******8"
	# 首先你得找到现在是谁登录的 得操作他的购物车
	loginname = request.session.get("name")
	# 通过名字找到这个人的id
	per = UserInfo.objects.get(account=loginname)
	perID = per.id
	print '这是登录人的id', perID

	# request 接受传过来的数据
	data = request.body
	print data
	# 进行反序列化 直接通过字典就可以获取了
	dic = json.loads(data)
	# print(dic["gId"])
	# 拿到了购物车的商品id 和数量  他俩下标是11 对应的
	gId = dic["gId"]
	gNum = dic["gNum"]

	# 长度.用于遍历
	g_len = len(gId)

	for i in range(g_len):
		shopinfo = ShoppingCart.objects.filter(
			goodsId=gId[i]).filter(userId=perID)
		for temp in shopinfo:

			price = temp.goodsId.goodsPrice
			num = gNum[i]

			print '单价', float(price)
			print '数量', float(num)
			# 修改小计
			temp.total = float(price) * float(num)
			# 修改数量
			temp.c = num
			# 修改状态
			temp.isDelete =True
			print temp.total
			temp.save()
			print temp.total

	print 'isDelete', ShoppingCart.objects.filter(isDelete=True)
	data = {'result':"True"}
	return JsonResponse(data)
  


@deractor.login_name
def place_order(request,dic):
	# 这是处理购物车信息把状态为 1 的列出来
	per = UserInfo.objects.get(account=dic['user_name'])
	# 找到这个人提交的购物信息
	shoplist = ShoppingCart.objects.filter(userId=per.id).filter(isDelete=1)
	# 算出商品的总价钱传到页面 ,因为在模板里再进行相加会很麻烦
	sumPic = 0

	for  shop in shoplist:

		sumPic+=shop.total

		
	print shoplist
	print '总价',sumPic
	shopSum = len(shoplist)
	# print shopSum
	# 把信息添加到字典中
	dic['submitCart']=shoplist
	dic['sumPic'] = sumPic
	dic['sumCount'] = shopSum

	return render(request, 'freshMall/place_order.html',dic)


def user_center_order(request):
	return render(request, 'freshMall/user_center_order.html')


def register(request):
	return render(request, 'freshMall/register.html')


def user_center_info(request):
	return render(request, 'freshMall/user_center_info.html')


def search(request):
	searchContent = request.GET('search')
	# print searchContent

	return render(request, 'freshMall/cart.html')


def list(request):
	return render(request, 'freshMall/list.html')
