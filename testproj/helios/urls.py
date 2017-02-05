from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.service_list, name='service_list'),
    url(r'^service/(?P<pk>\d+)/$', views.service_detail, name='service_detail'),
    url(r'^api/services/$', views.api_service_list, name='api_service_list'),
    url(r'^api/service/(?P<pk>[0-9]+)/$', views.api_service_detail, name='api_service_detail'),

]