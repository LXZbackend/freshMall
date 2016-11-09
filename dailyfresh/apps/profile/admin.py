from django.contrib import admin
from apps.profile.models import *
# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
	list_display = ('user_id', 'user_type', 'sex','realname','province','city','county','addr_detail')
	search_fields = ('user_id', 'user_type', 'sex','realname','province','city','county','addr_detail')
	list_filter = ['user_id', 'user_type', 'sex','realname','province','city','county','addr_detail']

admin.site.register(Profile,ProfileAdmin)
