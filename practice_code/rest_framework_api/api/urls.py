from django.urls import path, re_path, include
# from django.contrib import admin
from api import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'xxxxx', views.View1View)
router.register(r'rt', views.View1View)


urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    # 认证、权限、节流
    re_path(r'^(?P<version>[v1|v2]+)/auth/$', views.AuthView.as_view()),
    re_path(r'^(?P<version>[v1|v2]+)/order/$', views.OrderView.as_view()),
    re_path(r'^(?P<version>[v1|v2]+)/info/$', views.UserInfoView.as_view()),
    # 版本、解析器、序列化
    # 版本
    re_path(r'^(?P<version>[v1|v2]+)/users/$', views.UsersView.as_view(),name='uuu'),
    # django requst.post和request.body 取值
    re_path(r'^(?P<version>[v1|v2]+)/django/$', views.DjangoView.as_view(),name='ddd'),
    #解析器
    re_path(r'^(?P<version>[v1|v2]+)/parser/$', views.ParserView.as_view()),
    # 序列化
    re_path(r'^(?P<version>[v1|v2]+)/roles/$', views.RolesView.as_view()),
    # 序列化-超链
    re_path(r'^(?P<version>[v1|v2]+)/userinfo/$', views.UserInfoView2.as_view()),
    re_path(r'^(?P<version>[v1|v2]+)/group/(?P<xxx>\d+)/$', views.GroupView.as_view(),name='gp'),
    # 序列化-验证
    re_path(r'^(?P<version>[v1|v2]+)/usergroup/$', views.UserGroupView.as_view()),

    # 分页
    re_path(r'^(?P<version>[v1|v2]+)/pager1/$', views.Pager1View.as_view()),
    re_path(r'^(?P<version>[v1|v2]+)/pager2/$', views.PagerUserInfoView.as_view()),
    # 视图
    # # url(r'^(?P<version>[v1|v2]+)/v1/$', views.View1View.as_view()),
    #
    # # http://127.0.0.1:8000/api/v1/v1/?format=json
    # url(r'^(?P<version>[v1|v2]+)/v1/$', views.View1View.as_view({'get': 'list','post':'create'})),
    # # http://127.0.0.1:8000/api/v1/v1.json
    # url(r'^(?P<version>[v1|v2]+)/v1\.(?P<format>\w+)$', views.View1View.as_view({'get': 'list','post':'create'})),
    # url(r'^(?P<version>[v1|v2]+)/v1/(?P<pk>\d+)/$', views.View1View.as_view({'get': 'retrieve','delete':'destroy','put':'update','patch':'partial_update'})),
    # url(r'^(?P<version>[v1|v2]+)/v1/(?P<pk>\d+)\.(?P<format>\w+)$', views.View1View.as_view({'get': 'retrieve','delete':'destroy','put':'update','patch':'partial_update'})),

    re_path(r'^(?P<version>[v1|v2]+)/test/$', views.TestView.as_view()),
    # 路由
    re_path(r'^(?P<version>[v1|v2]+)/', include(router.urls)),
]
