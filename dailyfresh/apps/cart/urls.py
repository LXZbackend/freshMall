from django.conf.urls import url, patterns
from . import views


urlpatterns = patterns(
    '',
    url(r'^$', views.cart),
    url(r'^add$', views.add_to_cart),
    url(r'^update$', views.update_cart),
    url(r'^delete$', views.delete_from_cart),
)
