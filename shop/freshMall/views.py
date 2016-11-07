# coding=utf-8
from django.shortcuts import render, redirect
from django.http import *
from models import *
from Tools import *
import deractor
import json
from time import time
# 导入分页的包
from django.core.paginator import Paginator
# Create your views here.
# 装饰器 对每个页面都得进行显示帐号


@deractor.login_name
def index(request, dic):
	'''
					这是首页需要的展示的

	'''
	# loginname = request.session.get("name")
	# print '这是session', loginname
	fruitlist = GoodsList.objects.filter(goodsType=1)[:4]
	seafoodlist = GoodsList.objects.filter(goodsType=2)[:4]
	meatlist = GoodsList.objects.filter(goodsType=3)[:4]
	poultrylist = GoodsList.objects.filter(goodsType=4)[:4]
	greenlist = GoodsList.objects.filter(goodsType=5)[:4]
	coolerlist = GoodsList.objects.filter(goodsType=6)[:4]

	dic['fruitlist'] = fruitlist
	dic['seafoodlist'] = seafoodlist
	dic['poultrylist'] = poultrylist
	dic['meatlist'] = meatlist
	dic['greenlist'] = greenlist
	dic['coolerlist'] = coolerlist


	# dic = {

	#     'fruitlist': fruitlist,
	#     # 'seafoodlist':seafoodlist,
	#     'user_name': loginname
	#     # 'meatlist':meatlist

	# }

	return render(request, 'freshMall/index.html', dic)


def registerHandle(request):
	'''
					用户注册的方法
					# 这是柳怀洋 代码

	'''
	u=UserInfo()
	#这是判断用户是否勾选同意协议
	if request.POST.get('allow')=='on':
		uname = request.POST['user_name']
		pwd = request.POST['pwd']
		cpwd = request.POST['cpwd']
		email = request.POST['email']

		if (uname and pwd and cpwd and email)!='':
			nname = UserInfo.objects.filter(account=uname)
			if not nname:
				if pwd==cpwd:
					u.passswd = pwd
					e = UserInfo.objects.filter(email=email)
					if not e:
						u.account = uname
						u.email = request.POST['email']
						u.isDelete = False
						u.save()
						return render(request, 'freshMall/login.html')
					else:
						return render(request, 'freshMall/register.html')
				else:
					return render(request, 'freshMall/register.html')
			else:
				return render(request, 'freshMall/register.html')
		else:
			return render(request, 'freshMall/register.html')
	else:
		return render(request, 'freshMall/register.html')






	# per = UserInfo()
	# account = request.POST['user_name']
	# pwd = request.POST["pwd"]
	# email = request.POST["email"]

	# per.account = account
	# per.passswd = pwd
	# per.email = email
	# per.save()
	# # print '这是名字', per.account
	# # print request.method
	# return redirect('/login/')


def loginHandle(request):
	'''
					用户登录验证

	'''
	receName = request.POST['uname']
	recePwd = request.POST['pwd']
	perlist = UserInfo.objects.filter(account=receName).filter(passswd=recePwd)
	# 这是一个判断的标志 判断用户是否勾选记住账户密码
	flag  = request.POST.get('isrember',default='')
	# 这是通过创建爱呢respons的子类来从重定向 和写 cookie
	response = HttpResponseRedirect('/index/')
	if flag =="on":
		print "这是要写入的cook",receName
		response.set_cookie('remberAccount',receName)
	if len(perlist)==1:
		request.session['name'] = receName
	
		return response
	else:
		propmptInfo='<h4 color="red">你输入的信息有误<h34>'
		dic = {
		'propmptInfo':propmptInfo
		}
		return render(request, 'freshMall/login.html',dic)

	# for 
	# if per:
	# 	if per.passswd == recePwd:
	# 		# 如果登录成功  就把session 存到数据库
	# 		request.session['name'] = receName
	# 		# return render(request, 'freshMall/index.html')
	# 		return redirect('/index/')

	# 	else:
	# 		return render(request, 'freshMall/register.html')
	

def loginout(request):
	'''
					用户退出操作

	'''
	# 这是推出登录

	del request.session['name']  # 这是删除这个特定的
	# request.session.clear()
	# request.session.flush()
	return redirect('/index/')


def testform(request):
	'''
					这是用户在注册是 验证账户是否被使用了,一个异步验证

	'''

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


@deractor.login_name
def detail(request, dic):
	'''
					每个商品的详情页面

	'''
	per = UserInfo.objects.get(account=dic['user_name'])

	# # 找到商品的id
	# del request.session[per.account]
	id = int(request.GET.get('goodsId',1))
	goods = GoodsList.objects.get(pk = id)

	# 下面这个代码是实现把相对应的用户,最近浏览的商品信息存到cookiet 根据
	# # cookiet 的键是根据用户账户存的

	if request.session.get(per.account):
		print "这是有"
		alreadybrowse = request.session.get(per.account)
		alreadybrowse.append(goods.id)
		# # 先得找出这个人的已有的session 取出来,再添加,不然每次都会覆盖以前的.

		print "这是在商品页面取出的seesion11111", request.session.get(per.account)
		# 这里因为是引用 所以直接往里面添加,其seesion显示也改变了
		# alreadybrowse.append(goods.id)
		request.session[per.id]=alreadybrowse
		# print "这是在商品页面取出的seesion", alreadybrowse
		print "这是在商品页面取出的seesion", request.session.get(per.account)


	else:
		print "这是没有"
		request.session[per.account] = []
		alreadybrowse = request.session.get(per.account)
		alreadybrowse.append(goods.id)
		request.session[per.account]=alreadybrowse
		print request.session[per.account]
	# 马尧代码******************************
	goods = GoodsList.objects.all()
	#推荐商品(当前类对应下的列表)
	# 通过商品找到商品类,然后通过类找到类id,再通过类id找到分类下所有商品
	
	# recommendGoods = GoodsList.objects.all()
	id = int(request.GET.get('goodsId',1))
	goods = GoodsList.objects.get(pk = id)
	goodclass = goods.goodsType
	recommendGoods = GoodsList.objects.filter(goodsType = goodclass).order_by('-goodsPubdate')[0:4]

	# print '这是view中数量',dic['shopNum']
	goodsDic = {
		'goods':goods,
		'recommendGoods':recommendGoods,
		'goodClass':goodclass,
		'user_name':dic['user_name'],
		'shopNum':dic['shopNum'],
	}

	return render(request,'freshMall/detail.html',goodsDic)


@deractor.login_name
def cart(request, dic):
	'''
					这是展示购物车的商品信息

	'''
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
			print '这是商品信息', temp
		dic['carlist'] = carlist
		print '这是view中数量',dic['shopNum']
		# dic={
		# 	'carlist':carlist
		# }

	return render(request, 'freshMall/cart.html', dic)


def cartHandle(request):
	'''
	这是对应 购物车中POST ,把修改的信息传过来并且写道数据库中,方便结算页面展示
	并且修改状态信息,
	我这里犯的错误:通过filter 查询出来的是一个迭代的对象,你直接对他.id 是不对的,是什么都没有的  你得迭代之后在id,才行
	如果是 get 查询的 返回的是一个对象,所以直接可.id 等属性

	'''

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
			temp.amount = num
			# 修改状态
			temp.isSettle = True
			print temp.total
			temp.save()
			print temp.total

	print 'isDelete', ShoppingCart.objects.filter(isSettle=True)
	data = {'result': True}
	return JsonResponse(data)


@deractor.login_name
def place_order(request, dic):
	'''
					这是结算页面,就是购物车结算后到的页面,显示购物车中结算的物品

	'''
	# 这是处理购物车信息把状态为 1 的列出来
	if dic['user_name'] == '':

		return render(request, 'freshMall/login.html', dic)

	else:
		per = UserInfo.objects.get(account=dic['user_name'])
		# 找到这个人提交的购物信息
		shoplist = ShoppingCart.objects.filter(
			userId=per.id).filter(isSettle=1)
		# 算出商品的总价钱传到页面 ,因为在模板里再进行相加会很麻烦
		sumPic = 0

		for shop in shoplist:

			sumPic += shop.total

		print '找到的商品', shoplist
		print '总价', sumPic
		shopSum = len(shoplist)
		# print shopSum
		# 把信息添加到字典中
		dic['submitCart'] = shoplist
		dic['sumPic'] = sumPic
		dic['sumCount'] = shopSum

		return render(request, 'freshMall/place_order.html', dic)


@deractor.login_name
def submitOrder(request, dic):
	'''
		这是提交订单后,删除购物车结算的信息.复制到订单表


	'''
	# 找到登录账户的id
	per = UserInfo.objects.get(account=dic['user_name'])
	# 这是一个提交订单的方法
	# 如果购物车里面又符合的数据 才执行创建订单 创建详情订单操作
	shoplist = ShoppingCart.objects.filter(userId=per.id).filter(isSettle=1)
	if len(shoplist):
		# 创建一个订单的对象
		order = OrderForm()
		# 存id
		order.userId = per
		print '这是时间', int(time())
		# 设置订单编号
		order.orderNum = int(time())
		order.isPay = False
		order.orderSum = request.POST['orderSum']
		order.save()
		print '这是订单表id', order.id

		# 存储订单商品详细信息
		# detail = OrderDetail
		shoplist = ShoppingCart.objects.filter(
			userId=per.id).filter(isSettle=1)
		for shop in shoplist:
			detail = OrderDetail()
			# 商品外键和订单外键
			detail.goodsId = shop.goodsId
			detail.orderId = order

			detail.goodsCount = shop.amount
			detail.total = shop.total
			detail.save()

			# 省略一个删除操作
			shop.delete()

	# 查询这个用户的全部订单,返回信息

		# orderlist = OrderForm.objects.filter(userId=per.id)

		# dic['orderlist'] = orderlist
	data = {'result': True}
	return JsonResponse(data)
	# return redirect('/index/')

	# return render(request, 'freshMall/user_center_order.html',dic)


@deractor.login_name
def user_center_order(request, dic, pIndex):  # 这里的pIndex是位置参数
	'''	
					这是用户订单中心

	'''
	if dic['user_name'] == '':
		return render(request, 'freshMall/login.html', dic)
	else:
		per = UserInfo.objects.get(account=dic['user_name'])

		orderlist = OrderForm.objects.filter(userId=per.id)
	 
		# 传一个列表 和每页要显示几个
		pag = Paginator(orderlist, 4)
		pagelist = pag.page_range
		if pIndex == '':
			pIndex = '1'

		orderlist2 = pag.page(int(pIndex))
		dic['orderlist'] = orderlist2
		dic['pagelist'] = pagelist
		dic['p'] = pIndex

		return render(request, 'freshMall/user_center_order.html', dic)


@deractor.login_name
def delCartShop(request, dic):
	'''
					购车页面删除操作,对应前面的删除和数量为0时候

	'''

	# 这是传过来商品的id
	Goodid = request.POST['shopId']
	# 在找到这时候是谁登录,找到他的id
	per = UserInfo.objects.get(account=dic['user_name'])

	# 找到匹配的商品
	shoplist = ShoppingCart.objects.filter(
		userId=per.id).filter(goodsId=Goodid)
	# print '这是找到的商品', shoplist

	# 因为是获取的数组,需要迭代的删除
	for shop in shoplist:
		shop.delete()
	# print "这是删除人的id", per.id
	# print '这是删除商品的id', Goodid
	data = {'result': True}
	return JsonResponse(data)


@deractor.login_name
def addCart(request, dic):
	'''
		详情页面添加购物车操作,如果购物车列表中有这个商品 就把数量拿出来相加

	'''
	print"这是增加购物"
	# 获取到登录人的信息
	per = UserInfo.objects.get(account=dic['user_name'])
	# print "这是登人的id",per.id
	goodID = request.POST.get('goodID',default='')
	print'接受的商品id',goodID
	good = GoodsList.objects.get(pk=goodID)

	num = request.POST.get('num',default=1)
	print '这是传过来的数量',num
	gtotal = request.POST.get('total',default=0)
	
	print '这是传过来的价钱',gtotal

	# 从购物车列表中找这个这个商品 如果找到了就把数量和价格加到里面 如果没有 就新存进去
	flag = ShoppingCart.objects.filter(
		userId=per.id).filter(goodsId=good.id)

	print('这个商品在表中是否'), len(flag)
	if len(flag) != 0:
		# 因为返回的是个列表 只能通过遍历 改变其属性.
		for cart in flag:
			print '这是数据库中的数量',cart.amount
			print '这是数据库中的价格',cart.total
			print type(num)
			print type(gtotal)
			cart.amount += float(num)
			cart.total += float(gtotal)
			cart.save()
			print('11111111')
			print '这是数据库中的数量',cart.amount
			print '这是数据库中的价格',cart.total

	else:
		cart = ShoppingCart()
		# 注意对于外键必须通过对象的方法是赋值
		cart.goodsId = good
		cart.userId = per
		cart.amount = num
		cart.total = gtotal
		cart.save()

		

	return JsonResponse(dic)


@deractor.login_name
def immediateBuy(request, dic):
	'''
					商品页面立即购买,和添加购物车操作差不多,把结算状态改成 True 
	'''
	# 获取到登录人的信息
	per = UserInfo.objects.get(account=dic['user_name'])
	print per
	goodID = request.POST['goodID']
	print goodID
	good = GoodsList.objects.get(pk=goodID)
	print good

	num = request.POST['num']
	print num
	gtotal = request.POST['total']
	print gtotal
	print "添加购物车信息", goodID, num, gtotal

	cart = ShoppingCart()
	# 注意对于外键必须通过对象的方法是赋值
	cart.goodsId = good

	cart.userId = per

	cart.amount = num

	cart.total = gtotal

	cart.isSettle = True

	cart.save()
# 返回一个True  当所有斗执行完成 让jq 进行重定向
	data = {'result': True}
	return JsonResponse(data)


def register(request):
	return render(request, 'freshMall/register.html')


@deractor.login_name
def user_center_info(request, dic):
	if dic['user_name'] == '':
		return render(request, 'freshMall/login.html', dic)
	else:
		per = UserInfo.objects.get(account=dic['user_name'])
		# 创建一个商品列表 用于存储最近浏览的商品
		shoplist = []
		# print '这是用户的',per.id
		print per.id
		looklist = request.session.get(per.account,default=[])
		# 这里是对如果用户没有浏览任何东西 进行判断 如果为空就啥不显示,如果不为空就作下面的操作
		if looklist:
			# 对查看列表进行去重
			newlist = remove_repeat(looklist)
			# 如果浏览的信息少于5个就显示这些
			if len(newlist)<5:
				for shop in newlist:
					p = GoodsList.objects.get(id=shop)
					shoplist.append(p)
				dic['shoplist'] = shoplist

			# 大于5个就取最后面5个
			else:
				
				for shop in newlist[-1:-6:-1]:
					p = GoodsList.objects.get(id=shop)
					shoplist.append(p)
					dic['shoplist'] = shoplist



		return render(request, 'freshMall/user_center_info.html', dic)

			# print shoplist
			# # print "这是个人呢信息页面获取的session",looklist

		# return render(request, 'freshMall/user_center_info.html', dic)


@deractor.login_name
def user_center_site(request, dic):
	per = UserInfo.objects.get(account=dic['user_name'])
	receInfo=Consignee.objects.filter(userNum=per.id)
	dic['receInfo'] = receInfo
	return render(request, 'freshMall/user_center_site.html', dic)



@deractor.login_name
def list(request,dic):
	'''
		这是列表页的展示 通过传过来的商品类id 进行分类
		马尧作品 这是所有页面最复杂的 写的真的很棒
	'''
	# 获取到传过来的类别的
	id = int(request.GET.get('classId',1))
	goodclass = GoodsClass.objects.get(pk = id)
	sort = request.GET.get('sort', "default")
	print (sort)
	if sort == "" or sort == "default":
		sort = "default"
		goodsList = goodclass.goodslist_set.all()
		active = {'default': 'active'}
	elif sort == "byPrice":
		sort = "byPrice"
		goodsList = goodclass.goodslist_set.all().order_by('goodsPrice')
		active = {'byPrice': 'active'}
	elif sort == "byHot":
		sort = "byHot"
		goodsList = goodclass.goodslist_set.all().order_by('-buyTimes')
		active = {'byHot': 'active'}
	else:
		return HttpResponse('404')

	#推荐商品(当前类对应下的列表)
	recommendGoods = goodclass.goodslist_set.all().order_by('-goodsPubdate')[0:3]
	# 分页
	p =Paginator(goodsList,3)	#每页显示的个数
	# if pIndex == '':
	# 	pIndex = '1'
	pIndex =int(request.GET.get('pIndex',1))
	# 得到具体页
	list2 = p.page(pIndex)
	plist = p.page_range
	# print goodclass
	# 按照价格排序
	# goodsList = GoodsList.objects.order_by('goodsPrice')
	# goods = GoodsList.objects.get(pk = id)
	

	goodsDic = {
		'recommendGoods':recommendGoods,
		'pageList': list2, 
		'plist':plist,
		'goodclass':goodclass,
		'pIndex': pIndex,
		'active':active,
		'sort':sort,
		'user_name':dic['user_name'],
		'shopNum':dic['shopNum'],
	}

	
	return render(request,'freshMall/list.html',goodsDic)







@deractor.login_name
def usersitehandler(request,dic):
	# 找到登录的人信息
	per = UserInfo.objects.get(account=dic['user_name'])
	print "sdfasd",per
	user = Consignee()
	user.recePerName = request.POST['recePerName']
	# print "添加的人的姓名",request.POST['recePerName']

	user.addr = request.POST['addr']
	# print "添加的人的地址",request.POST['addr']

	user.postCode = request.POST['postCode']
	# print "添加的人的邮编",request.POST['postCode']

	user.recePerTel = request.POST['recePerTel']
	# print "添加的人的电话",request.POST['recePerTel']
	user.userNum = per
	user.save()

	return redirect('/user_center_site/')




def search(request):
	searchContent = request.GET('search')
	# print searchContent

	return render(request, 'freshMall/cart.html')





def login(request):
	dic = {}
	# 
	if request.COOKIES.has_key('remberAccount'):

		dic['remberAccount'] = request.COOKIES['remberAccount']



	return render(request, 'freshMall/login.html',dic)
