#coding=utf-8
from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^index/$', views.index, name='index'),
	url(r'^login/$', views.login,name='login'),
	url(r'^loginHandle/$',views.loginHandle,name='loginHandle'),

	url(r'^loginout/$',views.loginout,name='loginout'),
	url(r'^cart/$', views.cart,name='cart'),

	url(r'^list/$',views.list,name="list"),
	# 详情页面跳转
	url(r'^detail(?P<shopId>[0-9]*)/$',views.detail,name='detail'),
	url(r'^register/$', views.register,name='register'),
	url(r'^user_center_order/$', views.user_center_order,name='user_center_order'),
	url(r'^user_center_info/$',views.user_center_info,name ="user_center_info"),
	url(r'^search/$',views.search,name='search'),
	url(r'^rejisrHandle/$',views.rejisrHandle,name='rejisrHandle'),


	# 表单验证
	url(r'^testform/$',views.testform,name='testform')
]
