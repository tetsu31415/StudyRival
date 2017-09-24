from django.conf.urls import include, url
import django.contrib.auth.views
from . import views

urlpatterns = [
    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'app/login.html',
        },
        name='login'),
    url(r'^logout/$',
        django.contrib.auth.views.logout,
        {
            'template_name': 'app/logout.html',
        },
        name='logout'),

    url(r'^ranking/$', views.ranking, name='ranking'),
    url(r'', include('social_django.urls', namespace = 'social')),
    url(r'', views.stop_watch, name='stop_watch'),
]
