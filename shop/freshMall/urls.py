# coding=utf-8
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^index/$', views.index, name='index'),  # 首页
    url(r'^login/$', views.login, name='login'),  # 登录
    url(r'^loginHandle/$', views.loginHandle, name='loginHandle'),  # 登录处理

    url(r'^loginout/$', views.loginout, name='loginout'),  # 退出
    url(r'^cart/$', views.cart, name='cart'),  # 购物车

    # url(r'^list([0-9]*)/$', views.list, name="list"),  # 商品列表
    # 详情页面跳转
    # url(r'^detail([0-9]*)/$', views.detail, name='detail'),  # 详情页面
    url(r'^register/$', views.register, name='register'),  # 注册页面

    url(r'^user_center_order([0-9]*)/$', views.user_center_order,
        name='user_center_order'),  # 个人订单列表
    # 个人信息
    url(r'^user_center_info/$', views.user_center_info, name="user_center_info"),
    url(r'^user_center_site/$', views.user_center_site, name="user_center_site"),
    # url(r'^search/$', views.search, name='search'),
    url(r'^registerHandle/$', views.registerHandle, name='registerHandle'),
    # 购物车传过来信息
    url(r"^cartHandle/$", views.cartHandle, name='cartHandle'),


    # 表单验证
    url(r'^testform/$', views.testform, name='testform'),
    # 结算
    url(r'^place_order/$', views.place_order, name='place_order'),
    # 提交订单
    url(r'^submitOrder/$', views.submitOrder, name='submitOrder'),
    # 删除购物车中的商品
    url(r'^delCartShop/$', views.delCartShop, name='delCartShop'),

    # 详情页面添加商品
    url(r"^addCart/$", views.addCart, name='addCart'),
    # 详情页面立即购买

    url(r"^immediateBuy/$", views.immediateBuy, name='immediateBuy'),
    # 用户添加收件人信息

     url(r"^usersitehandler/$", views.usersitehandler, name='usersitehandler'),



    #马尧
    url(r'^list/$', views.list, name='list'),
    url(r'^detail/$', views.detail, name='detail'),








]
