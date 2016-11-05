# coding=utf-8
from django.shortcuts import render, redirect
from django.http import *
from models import *
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
    fruitlist = GoodsList.objects.filter(goodsType=1)
    seafoodlist = GoodsList.objects.filter(goodsType=2)
    meatlist = GoodsList.objects.filter(goodsType=3)
    poultrylist = GoodsList.objects.filter(goodsType=4)

    dic['fruitlist'] = fruitlist
    dic['seafoodlist'] = seafoodlist
    dic['poultrylist'] = poultrylist
    dic['meatlist'] = meatlist
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

    '''

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
    '''
                    用户登录验证

    '''
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
def detail(request, dic, shopId):
    '''
                    每个商品的详情页面

    '''

    shopinfo = GoodsList.objects.get(pk=shopId)
    dic['shopinfo'] = shopinfo

    return render(request, 'freshMall/detail.html', dic)


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
    print '这是找到的商品', shoplist

    # 因为是获取的数组,需要迭代的删除
    for shop in shoplist:
        shop.delete()
    print "这是删除人的id", per.id
    print '这是删除商品的id', Goodid
    data = {'result': True}
    return JsonResponse(data)


@deractor.login_name
def addCart(request, dic):
    '''
                    详情页面添加购物车操作,如果购物车列表中有这个商品 就把数量拿出来相加

    '''

    # 获取到登录人的信息
    per = UserInfo.objects.get(account=dic['user_name'])
    goodID = request.POST['goodID']
    good = GoodsList.objects.get(pk=goodID)

    num = request.POST['num']
    gtotal = request.POST['total']
    # 从购物车列表中找这个这个商品 如果找到了就把数量和价格加到里面 如果没有 就新存进去
    flag = ShoppingCart.objects.filter(
        userId=per.id).filter(goodsId=good.id)

    print('这个商品在表中是否'), len(flag)
    if len(flag) != 0:
        # 因为返回的是个列表 只能通过遍历 改变其属性.
        for cart in flag:
            # print '这是数据库中的数量',cart.amount
            # print '这是数据库中的价格',cart.total
            # print type(num)
            # print type(gtotal)
            cart.amount += float(num)
            cart.total += float(gtotal)
            cart.save()
            # print('11111111')
            # print '这是数据库中的数量',cart.amount
            # print '这是数据库中的价格',cart.total

    else:
        cart = ShoppingCart()
        # 注意对于外键必须通过对象的方法是赋值
        cart.goodsId = good
        cart.userId = per
        cart.amount = num
        cart.total = gtotal
        cart.save()

    # per = UserInfo.objects.get(account=dic['user_name'])
    # # print per
    # goodID = request.POST['goodID']
    # # print goodID
    # good = GoodsList.objects.get(pk=goodID)
    # # print good

    # num = request.POST['num']
    # print num
    # gtotal = request.POST['total']
    # print gtotal
    # print "添加购物车信息", goodID, num, gtotal

    # cart = ShoppingCart()
    # # 注意对于外键必须通过对象的方法是赋值
    # cart.goodsId = good
    # cart.userId = per
    # cart.amount = num
    # cart.total = gtotal
    # cart.save()

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
        return render(request, 'freshMall/user_center_info.html', dic)


@deractor.login_name
def user_center_site(request, dic):
    return render(request, 'freshMall/user_center_site.html', dic)


def search(request):
    searchContent = request.GET('search')
    # print searchContent

    return render(request, 'freshMall/cart.html')


def list(request):
    return render(request, 'freshMall/list.html')


def login(request):
    return render(request, 'freshMall/login.html')
