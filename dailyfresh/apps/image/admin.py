from django.contrib import admin
from apps.image.models import *
# Register your models here.
class ImageAdmin(admin.ModelAdmin):
	list_display = ('img_product_id', 'img_url', 'img_type')
	search_fields = ('img_product_id', 'img_url', 'img_type')
	list_filter = ['img_product_id', 'img_url', 'img_type']

admin.site.register(Image,ImageAdmin)
