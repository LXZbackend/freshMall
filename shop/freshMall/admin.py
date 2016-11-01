# coding=utf-8
from django.contrib import admin
from models import *
# Register your models here.


class userInfoAdmin(admin.ModelAdmin):
    list_display = ['account', 'passswd'
                    ,'email', 'isDelete']


class consigneeAdmin(admin.ModelAdmin):
    list_display = ['recePerName', 'recePerTel',
                    'addr', 'postCode', 'isDelete', 'userNum']


class goodsClassAdmin(admin.ModelAdmin):
    list_display = ['className']


class goodsListAdmin(admin.ModelAdmin):
    list_display = ['goodsName', 'goodsDetail', 'goodsRoute',
                    'goodsStock', 'goodsPrice', 'goodsType']


class shoppingCartAdmin(admin.ModelAdmin):
    list_display = ['goodsId', 'userId', 'userId', 'total']


class orderFormAdmin(admin.ModelAdmin):
    list_display = ['orderDate', 'userId']


class orderDetailAdmin(admin.ModelAdmin):
    list_display = ['goodsId', 'orderId', 'orderId',
                    'goodsCount', 'orderSum', 'orderStatus']


admin.site.register(UserInfo, userInfoAdmin)
admin.site.register(Consignee, consigneeAdmin)
admin.site.register(GoodsClass, goodsClassAdmin)
admin.site.register(GoodsList, goodsListAdmin)
admin.site.register(ShoppingCart, shoppingCartAdmin)
admin.site.register(OrderForm, orderFormAdmin)
admin.site.register(OrderDetail, orderDetailAdmin)
