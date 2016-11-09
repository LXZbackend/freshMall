from django.contrib import admin
from apps.address.models import *
# Register your models here.
class AddressAdmin(admin.ModelAdmin):
	list_display = ('user', 'recipient_name', 'recipient_phone','province','city','county','addr_detail')
	search_fields = ('user', 'recipient_name', 'recipient_phone','province','city','county','addr_detail')
	list_filter = ['user', 'recipient_name', 'recipient_phone','province','city','county','addr_detail']

admin.site.register(Address,AddressAdmin)
