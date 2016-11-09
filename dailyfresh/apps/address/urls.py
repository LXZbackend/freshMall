from django.conf.urls import url, patterns
from . import views

urlpatterns = patterns(
    '',
    url(r'^$', views.address),
    url(r'^add$', views.add_one_address),
)
