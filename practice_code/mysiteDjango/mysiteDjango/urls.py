"""mysiteDjango URL Configuration

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
from django.urls import path, include, re_path
#from .views import login
from app01 import views
# from app2 import views as app2_views
from app2 import urls as app2_urls
from app3 import views as v3


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login),
    path('index/', views.index),
    path('user_list/', views.user_list),
    path('add_user/', views.add_user),

    path('publisher_list/', views.publisher_list),
    path('add_publisher/', views.add_publisher),
    path('delete_publisher/', views.delete_publisher),
    path('edit_publisher/', views.edit_publisher),

    path('book_list/', views.book_list),
    path('add_book/', views.add_book),
    path('delete_book/', views.delete_book),
    path('edit_book/', views.edit_book),

    path('author_list/', views.author_list),
    path('add_author/', views.add_author),
    path('delete_author/', views.delete_author),
    path('edit_author/', views.edit_author),

    path('t_test/', views.template_test),

    # url 练习，
    re_path('^book/(?P<year>[0-9]{2,4})/(?P<title>[a-zA-Z]{2})/$', views.book),
    # re_path('book/[0-9]{2,4}/$', views.book),

    # CBV 文件上传
    re_path('^app2/', include(app2_urls)),

    # 分页
    re_path('^app3/books/$', v3.books),

]
