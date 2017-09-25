from django.conf.urls import url, include
import django.contrib.auth.views
from . import views

urlpatterns = [

    # トップページ
    url(r'^$', views.TopPageView.as_view(), name='index'),
 
    # マイページ機能
    url(r'^mypage/$', views.MyPageView.as_view(), name='mypage'),
    url(r'^user_update/(?P<pk>[0-9]+)/$',
        views.UserUpdateView.as_view(), name='user_update'),
    
    # ログイン、ログアウト
    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'easy_regist/login.html',
        },
        name='login'),
    url(r'^logout/$',
        django.contrib.auth.views.logout,
        {
            'template_name': 'easy_regist/login.html',
        },
        name='logout'),
]
