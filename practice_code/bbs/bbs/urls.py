"""bbs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path,include
from blog import views
from django.views.static import serve
from django.conf import settings
from blog import urls as blog_urls


urlpatterns = [
    path('admin/', admin.site.urls),

    re_path(r'^login/$', views.login),
    re_path(r'^logout/$', views.logout),
    re_path(r'^reg/$', views.register),
    re_path(r'^index/$', views.index),
    # 将所有以blog开头的url都交给app下面的urls.py来处理
    re_path(r'^blog/', include(blog_urls)),
    re_path(r'^get_valid_img.png/', views.get_valid_img),

    # 极验滑动验证码 获取验证码的url
    re_path(r'^pc-geetest/register', views.get_geetest),
    # 专门用来校验用户名是否已被注册的接口
    re_path(r'^check_username_exist/$', views.check_username_exist),

    # media相关的路由设置 -- 固定配置，记住即可
    re_path(r'^media/(?P<path>.*)$', serve, {"document_root": settings.MEDIA_ROOT}),

    # 空跳转首页
    re_path(r'^$', views.index),

]
handler404 = views.page_not_found

