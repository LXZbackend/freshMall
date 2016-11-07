#coding=utf-8
from django.shortcuts import *
from models import *
def login_name(fn):
	def fun(request,*args):
		username = request.session.get('name',default='')

		if username!='':
			per = UserInfo.objects.get(account=username)
			shopNum = ShoppingCart.objects.filter(userId=per.id).filter(isSettle=False)
			print '购物车的数量',len(shopNum)
			dic = {
			'shopNum':len(shopNum),
			'user_name':username
			}
		else:
			dic = {
			'user_name':username
			}
		result = fn(request,dic,*args)
		return result
	return fun




def login_yz(fn):
    def fun(request, *args):
        if request.session.has_key('username'):
            result = fn(request, *args)
        else:
            result = redirect('/login/')
        return result
    return fun
