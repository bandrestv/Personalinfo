from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<pi_text_id>[0-9]+)/$', views.obj_name, name='obj_name'),
    url(r'^(?P<pi2_text_id>[0-9]+)/results/$', views.st, name='st'),
]