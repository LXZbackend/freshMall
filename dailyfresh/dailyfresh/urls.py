from django.conf.urls import patterns, include, url
from django.contrib import admin
from apps.goods import views

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'ecom.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.home_list_page),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^passport/', include('apps.passport.urls')),
    url(r'^profile/', include('apps.profile.urls')),
    url(r'^image/', include('apps.image.urls')),
    url(r'^goods/', include('apps.goods.urls')),
    url(r'^cart/', include('apps.cart.urls')),
    url(r'^address/', include('apps.address.urls')),
    url(r'^order/', include('apps.order.urls')),
)
