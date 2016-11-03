from django.shortcuts import *
def login_name(fn):
	def fun(request,*args):
		username = request.session.get('name',default='')
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
