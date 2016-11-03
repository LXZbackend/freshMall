#coding=utf-8
from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^$', views.index, name='index'),

	url(r'^index/$', views.index, name='index'),#首页
	url(r'^login/$', views.login,name='login'),#登录
	url(r'^loginHandle/$',views.loginHandle,name='loginHandle'),#登录处理

	url(r'^loginout/$',views.loginout,name='loginout'),#退出
	url(r'^cart/$', views.cart,name='cart'),#购物车

	url(r'^list/$',views.list,name="list"),#商品列表
	# 详情页面跳转
	url(r'^detail(?P<shopId>[0-9]*)/$',views.detail,name='detail'),#详情页面
	url(r'^register/$', views.register,name='register'),#注册页面
	url(r'^user_center_order/$', views.user_center_order,name='user_center_order'),#个人订单列表
	# 个人信息
	url(r'^user_center_info/$',views.user_center_info,name ="user_center_info"),
	url(r'^search/$',views.search,name='search'),
	url(r'^registerHandle/$',views.registerHandle,name='registerHandle'),
	#购物车传过来信息
	url(r"^cartHandle/$",views.cartHandle,name='cartHandle'),


	# 表单验证
	url(r'^testform/$',views.testform,name='testform'),
	# 结算
	url(r'^place_order/$',views.place_order,name='place_order'),
]
