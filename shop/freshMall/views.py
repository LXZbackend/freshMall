# coding=utf-8
from django.shortcuts import render, redirect
from django.http import *
from models import *
# Create your views here.


def index(request):

    loginname = request.session.get("name")
    print '这是session', loginname

    fruitlist = GoodsList.objects.filter(goodsType=1)

  
    print '这是类型',type(loginname)

    dic = {

        'fruitlist': fruitlist,
        # 'seafoodlist':seafoodlist,
        'user_name': loginname
        # 'meatlist':meatlist


    }

    return render(request, 'freshMall/index.html', dic)


def rejisrHandle(request):
	# 注册的方法
    per = UserInfo()
    print request.method
    per.account = request.POST['user_name']
    print '这是名字', per.account
    per.passswd = request.POST["pwd"]
    per.email = request.POST["email"]
    per.save()

    return redirect('/')


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

	#del request.session['name']  #这是删除这个特定的
    # request.session.clear()
    request.session.flush()
    return redirect('/index/')





def login(request):
    return render(request, 'freshMall/login.html')


def testform(request):

    nameflag = False 
    testname = request.POST['name']
    # testemail = request.POST['email']
    print testname

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


def cart(request):
    return render(request, 'freshMall/cart.html')


def user_center_order(request):
    return render(request, 'freshMall/user_center_order.html')


def register(request):
    return render(request, 'freshMall/register.html')


def user_center_info(request):
    return render(request, 'freshMall/user_center_info.html')


def search(request):
    searchContent = request.GET('search')
    print searchContent

    return render(request, 'freshMall/cart.html')


def list(request):
    return render(request, 'freshMall/list.html')
