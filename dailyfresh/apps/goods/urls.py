from django.conf.urls import url, patterns, include
from . import views


urlpatterns = patterns(
    '',
    url(r'^$', views.home_list_page),
    url(r'^detail/(\d+)$', views.goods_detail),
    url(r'^list/(?P<goods_type_id>\d+)/(?P<page>\d+)$', views.goods_list),
    url(r'^search$', views.MySearchView.as_view()),
    # url(r'^search/', include('haystack.urls')),
)
