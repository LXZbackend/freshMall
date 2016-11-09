from django.conf.urls import url, patterns
from . import views


urlpatterns = patterns(
    '',
    url(r'^(?P<page>\d+)$', views.my_order),
    url(r'^commit$', views.commit_order),
    url(r'^add$', views.add_order),
    url(r'^finish$', views.finish_order),
    url(r'^comment$', views.comment),
)
