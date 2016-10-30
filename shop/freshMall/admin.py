# coding=utf-8
from django.contrib import admin
from models import *
# Register your models here.


class userInfoAdmin(admin.ModelAdmin):
    list_display = ['account', 'passswd',
                    'name', 'telephone', 'email', 'isDelete']


class consigneeAdmin(admin.ModelAdmin):
    list_display = ['recePerName', 'recrPerTel',
                    'addr', 'postcode', 'isDelete', 'userNum']


class goodsClassAdmin(admin.ModelAdmin):
    list_display = ['className']


class goodsListAdmin(admin.ModelAdmin):
    list_display = ['goodsName', 'goodsDetail', 'goodsRoute',
                    'goodsStock', 'goodsPrice', 'goodsType']


class shoppingCartAdmin(admin.ModelAdmin):
    list_display = ['goodsId', 'userInfo', 'amount', 'total']


class orderFormAdmin(admin.ModelAdmin):
    list_display = ['orderDate', 'userId']


class orderDetailAdmin(admin.ModelAdmin):
    list_display = ['goodsId', 'orderId', 'orderId',
                    'goodsCount', 'orderSum', 'orderStatus']


admin.site.register(userInfo, userInfoAdmin)
admin.site.register(consignee, consigneeAdmin)
admin.site.register(goodsClass, goodsClassAdmin)
admin.site.register(goodsList, goodsListAdmin)
admin.site.register(shoppingCart, shoppingCartAdmin)
admin.site.register(orderForm, orderFormAdmin)
admin.site.register(orderDetail, orderDetailAdmin)
