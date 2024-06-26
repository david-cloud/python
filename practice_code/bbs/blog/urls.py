# from django.conf.urls import path, re_path
from django.urls import path, re_path
from blog import views


urlpatterns = [

    re_path(r"up_down/$",views.up_down),
    # /blog/xiaohei/tag/python
    # /blog/xiaohei/category/技术
    # /blog/xiaohei/archive/2018-05
    # url(r'(\w+)/tag/(\w+)', views.tag),
    # url(r'(\w+)/category/(\w+)', views.category),
    # url(r'(\w+)/archive/(.+)', views.archive),
    # 三和一 URL

    re_path(r'(\w+)/(tag|category|archive)/(.+)/$', views.home),  # home(request, username, tag, 'python')
    re_path(r'(\w+)/article/(\d+)/$', views.article_detail),  # 文章详情  article_detail(request, xiaohei, 1)

    re_path(r'(\w+)/$', views.home),  # home(request, username)

]