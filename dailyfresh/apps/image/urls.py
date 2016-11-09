from django.conf.urls import url, patterns
from . import views


urlpatterns = patterns(
    '',
    url(r'^get/(?P<file_id>\w+)$', views.get_image),
)
