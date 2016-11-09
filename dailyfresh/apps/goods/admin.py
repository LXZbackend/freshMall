from django.contrib import admin
from apps.goods.models import *

# Register your models here.
class GoodsAdmin(admin.ModelAdmin):
	list_display = ('goods_type_id', 'goods_name','goods_subtitle', 'goods_price','goods_unit','goods_ex_price','goods_info','goods_status', 'goods_stock', 'goods_sales')
	search_fields = ('goods_type_id', 'goods_name','goods_subtitle','goods_price','goods_unit','goods_ex_price','goods_info','goods_status', 'goods_stock', 'goods_sales')
	list_filter = ['goods_type_id', 'goods_name','goods_subtitle','goods_price','goods_unit','goods_ex_price','goods_info','goods_status', 'goods_stock', 'goods_sales']

admin.site.register(Goods,GoodsAdmin)
