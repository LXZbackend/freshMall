from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^login/$', views.login),
	url(r'^cart/$', views.cart),
	url(r'^user_center_order/$', views.user_center_order),
	url(r'^register/$', views.register),

]
