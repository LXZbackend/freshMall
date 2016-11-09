from django.contrib import admin
from apps.order.models import *
# Register your models here.
class SOrderAdmin(admin.ModelAdmin):
	list_display = ('user', 'addr','total_amount','total_count','ex_price','payment_method','order_status')
	search_fields = ('user', 'addr','total_amount','total_count','ex_price','payment_method','order_status')
	list_filter = ['user', 'addr','total_amount','total_count','ex_price','payment_method','order_status']

admin.site.register(SOrder,SOrderAdmin)
