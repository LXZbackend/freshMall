from django.contrib import admin
from apps.cart.models import *
# Register your models here.
class CartAdmin(admin.ModelAdmin):
	list_display = ('user_id', 'goods_id', 'goods_num')
	search_fields = ('user_id', 'goods_id', 'goods_num')
	list_filter = ['user_id', 'goods_id', 'goods_num']

admin.site.register(Cart,CartAdmin)
