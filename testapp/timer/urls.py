from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.test_view, name='stop_watch'),
#    url(r'^$', views.test_view, name='test'),
]