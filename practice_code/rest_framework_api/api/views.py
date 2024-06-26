from django.shortcuts import render
# Create your views here.

from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework import exceptions
from rest_framework.authentication import BasicAuthentication
from api.utils.permission import SVIPPermission
from api.utils.permission import MyPermission1
from api.utils.throttle import VisitThrottle
from api import models

from rest_framework.versioning import QueryParameterVersioning,URLPathVersioning
from django.urls import reverse
import json

# 认证、权限、节流
ORDER_DICT = {
    1:{
        'name': "媳妇",
        'age':18,
        'gender':'男',
        'content':'...'
    },
    2:{
        'name': "老狗",
        'age':19,
        'gender':'男',
        'content':'...。。'
    },
}


def md5(user):
    import hashlib
    import time
    ctime = str(time.time())
    m = hashlib.md5(bytes(user,encoding='utf-8'))
    m.update(bytes(ctime,encoding='utf-8'))
    return m.hexdigest()


class AuthView(APIView):
    """
    用于用户登录认证
    """
    authentication_classes = []
    permission_classes = []
    throttle_classes = [VisitThrottle,]

    def post(self,request,*args,**kwargs):

        ret = {'code':1000,'msg':None}
        try:
            user = request._request.POST.get('username')
            pwd = request._request.POST.get('password')
            obj = models.UserInfo.objects.filter(username=user,password=pwd).first()
            if not obj:
                ret['code'] = 1001
                ret['msg'] = "用户名或密码错误"
            # 为登录用户创建token
            token = md5(user)
            # 存在就更新，不存在就创建
            models.UserToken.objects.update_or_create(user=obj,defaults={'token':token})
            ret['token'] = token
        except Exception as e:
            ret['code'] = 1002
            ret['msg'] = '请求异常'

        return JsonResponse(ret)


class OrderView(APIView):
    """
    订单相关业务(只有SVIP用户有权限)
    """

    def get(self,request,*args,**kwargs):
        # request.user
        # request.auth
        self.dispatch
        ret = {'code':1000,'msg':None,'data':None}
        try:
            ret['data'] = ORDER_DICT
        except Exception as e:
            pass
        return JsonResponse(ret)


# 节流控制 默认配置使用 LuffyUser -- 在settings配置中 DEFAULT_THROTTLE_CLASSES
class UserInfoView(APIView):
    """
    订单相关业务（普通用户、VIP）
    """
    permission_classes = [MyPermission1, ]

    def get(self,request,*args,**kwargs):
        return HttpResponse('用户信息')

from rest_framework.versioning import QueryParameterVersioning, URLPathVersioning
# 版本、解析器、序列化
# ########## 版本 ############################
class UsersView(APIView):

    def get(self,request,*args,**kwargs):

        self.dispatch
        # 获取版本
        print(request.version)
        # 获取处理版本的对象
        print(request.versioning_scheme)

        # 使用rest_framework 内置反向生成URL（rest framework），不需要加version参数， reqeust中有version， request.version
        u1 = request.versioning_scheme.reverse(viewname='uuu',request=request)
        print(u1)

        # 使用Django 的reverse实现反向生成URL，需要加 kwargs参数
        u2 = reverse(viewname='uuu',kwargs={'version':2})
        print(u2)

        return HttpResponse('用户列表')


################# 解析器 ######################
# DjangoView -- 测试Django request.POST  / request.body
"""
request.POST里不一定取到值，但request.body里一定可以取到值，因为request.post里的值是从
requst.body里转化取过来的，需要满足以下要求，request.post里才有值
1. 请求头要求：
    Content-Type: application/x-www-form-urlencoded
    PS: 如果请求头中的 Content-Type: application/x-www-form-urlencoded，request.POST中才有值（去request.body中解析数据）。
2. 数据格式要求：
      name=alex&age=18&gender=男
"""
class DjangoView(APIView):
    def post(self, request, *args, **kwargs):
        print(type(request._request))
        from django.core.handlers.wsgi import WSGIRequest
        return HttpResponse('POST和Body')


# from rest_framework.parsers import JSONParser, FormParser
class ParserView(APIView):
    # parser_classes = [JSONParser,FormParser,]
    """
    JSONParser:表示只能解析content-type:application/json头
    JSONParser:表示只能解析content-type:application/x-www-form-urlencoded头
    """

    def post(self,request,*args,**kwargs):
        """
        允许用户发送JSON格式数据
            a. content-type: application/json
            b. {'name':'alex',age:18}
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        """
        1. 获取用户请求
        2. 获取用户请求体
        3. 根据用户请求头 和 parser_classes = [JSONParser,FormParser,] 中支持的请求头进行比较
        4. JSONParser对象去请求体
        5. request.data  - 获取解析后的数据
        """
        print(request.data, type(request.data), request.data.get("测试"))
        return HttpResponse('ParserView')


################ 序列化 #######################
"""
两个用途
1- 对请求数据进行验证  -- Django form组件也可以实现
2- 对QuerySet数据进行序列化
"""
from rest_framework import serializers


class RolesSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()


class RolesView(APIView):
    def get(self,request,*args,**kwargs):

        # 方式一：
        # roles = models.Role.objects.all().values('id','title')
        # roles = list(roles)
        # ret = json.dumps(roles,ensure_ascii=False)

        # 方式二：对于 [obj,obj,obj,]
        # roles = models.Role.objects.all()
        # ser = RolesSerializer(instance=roles,many=True)
        # ret = json.dumps(ser.data, ensure_ascii=False)

        role = models.Role.objects.all().first()
        # print(role)
        ser = RolesSerializer(instance=role, many=False)
        # ser.data 已经是转换完成的结果

        ret = json.dumps(ser.data, ensure_ascii=False)
        return HttpResponse(ret)


# serializers.Serializer 实现序列化类
# class UserInfoSerializer(serializers.Serializer):
#     xxxxx = serializers.CharField(source="user_type") # row.user_type
#     oooo = serializers.CharField(source="get_user_type_display") # row.get_user_type_display()
#     username = serializers.CharField()
#     password = serializers.CharField()
#     gp = serializers.CharField(source="group.title")
#     # rls = serializers.CharField(source="roles.all")
#     rls = serializers.SerializerMethodField() # 自定义显示
#
#     def get_rls(self,row):
#
#         role_obj_list = row.roles.all()
#
#         ret = []
#         for item in role_obj_list:
#             ret.append({'id':item.id,'title':item.title})
#         return ret

# 自定义字段显示
class MyField(serializers.CharField):

    def to_representation(self, value):
        print(value)
        return "xxxxx"


# serializers.ModelSerializer 实现序列化类
# class UserInfoSerializer(serializers.ModelSerializer):
#     oooo = serializers.CharField(source="get_user_type_display")  # row.user_type
#     rls = serializers.SerializerMethodField()  # 自定义显示
#     x1 = MyField(source='username')
#
#     class Meta:
#         model = models.UserInfo
#         # fields = "__all__"
#         fields = ['id','username','password','oooo','rls','group','x1']
#
#     def get_rls(self, row):
#         role_obj_list = row.roles.all()
#
#         ret = []
#         for item in role_obj_list:
#             ret.append({'id':item.id,'title':item.title})
#         return ret

class UserInfoSerializer(serializers.ModelSerializer):
    group = serializers.HyperlinkedIdentityField(view_name='gp',lookup_field='group_id',lookup_url_kwarg='xxx')
    class Meta:
        model = models.UserInfo
        # fields = "__all__"
        fields = ['id','username','password','group','roles']
        # 深度代表继续乡下解析， depth=1时，会将 roles id解析为对应文字
        depth = 0 # 0 ~ 10
        # depth = 1 # 0 ~ 10


from rest_framework.response import Response
class UserInfoView2(APIView):
    def get(self,request,*args,**kwargs):

        users = models.UserInfo.objects.all()
        # 对象， Serializer类处理； self.to_representation
        # QuerySet，ListSerializer类处理； self.to_representation
        ser = UserInfoSerializer(instance=users,many=True,context={'request': request})
        # ensure_ascii=False  配置可以在页面正常显示汉字
        # ret = json.dumps(ser.data, ensure_ascii=False)
        ret = json.dumps(ser.data)
        # return HttpResponse(ret)
        return Response(ret)

class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.UserGroup
        fields = "__all__"


class GroupView(APIView):
    def get(self,request,*args,**kwargs):
        pk = kwargs.get('xxx')
        obj = models.UserGroup.objects.filter(pk=pk).first()

        ser = GroupSerializer(instance=obj,many=False)
        ret = json.dumps(ser.data,ensure_ascii=False)
        return HttpResponse(ret)


###################### 验证 ############################

class XXValidator(object):
    def __init__(self, base):
        self.base = base

    def __call__(self, value):
        if not value.startswith(self.base):
            message = '标题必须以 %s 为开头。' % self.base
            raise serializers.ValidationError(message)

    def set_context(self, serializer_field):
        """
        This hook is called by the serializer instance,
        prior to the validation call being made.
        """
        # 执行验证之前调用,serializer_fields是当前字段对象
        pass


class UserGroupSerializer(serializers.Serializer):
    title = serializers.CharField(error_messages={'required':'标题不能为空'},validators=[XXValidator('老男人'),])

    # def validate_title(self, value):
    #     from rest_framework import exceptions
    #     raise exceptions.ValidationError('看你不顺眼')
    #     return value


class UserGroupView(APIView):

    def post(self,request,*args,**kwargs):

        ser = UserGroupSerializer(data=request.data)
        if ser.is_valid():
            print(ser.validated_data['title'])
        else:
            print(ser.errors, type(ser.errors))

        return HttpResponse('提交数据-{}'.format(ser.errors.get("title")[0]))



##################    分页   ###################################
from api.utils.serializsers.pager import PagerSerialiser
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination,CursorPagination

class MyCursorPagination(CursorPagination):
    cursor_query_param = 'cursor'
    page_size = 2
    ordering = 'id'
    # page_size_query_param = None
    # max_page_size = None
    # url测试 /api/v1/pager2/?page_size=3&token=9dd14855433ab0777ae52970e44bdc5b
    page_size_query_param = 'page_size'
    max_page_size = 4


class Pager1View(APIView):

    def get(self,request,*args,**kwargs):
        # 获取所有数据
        roles = models.Role.objects.all()
        # 创建分页对象
        # pg = CursorPagination()
        pg = MyCursorPagination()
        # 在数据库中获取分页的数据
        pager_roles = pg.paginate_queryset(queryset=roles,request=request,view=self)
        # 对数据进行序列化
        ser = PagerSerialiser(instance=pager_roles, many=True)
        # return Response(ser.data)
        return pg.get_paginated_response(ser.data)


class PagerUserInfoView(APIView):
    def get(self, request, *args, **kwargs):
        # 获取所有数据
        userinfo = models.UserInfo.objects.all()
        print(userinfo)
        # 创建分页对象
        # pg = CursorPagination()
        pg = MyCursorPagination()
        # 在数据库中获取分页的数据
        pager_userinfo = pg.paginate_queryset(queryset=userinfo, request=request, view=self)
        # 对数据进行序列化
        ser = UserInfoSerializer(instance=pager_userinfo, many=True, context={'request': request})
        # return Response(ser.data)
        return pg.get_paginated_response(ser.data)

#######################   视图  ######################################
"""
from api.utils.serializsers.pager import PagerSerialiser
from rest_framework.generics import GenericAPIView

class View1View(GenericAPIView):
    queryset = models.Role.objects.all()
    serializer_class = PagerSerialiser
    pagination_class = PageNumberPagination
    def get(self,request,*args,**kwargs):
        # 获取数据
        roles = self.get_queryset() # models.Role.objects.all()

        # [1, 1000,]     [1,10]
        pager_roles = self.paginate_queryset(roles)

        # 序列化
        ser = self.get_serializer(instance=pager_roles,many=True)

        return Response(ser.data)
"""

"""
from api.utils.serializsers.pager import PagerSerialiser
from rest_framework.viewsets import GenericViewSet

class View1View(GenericViewSet):
    queryset = models.Role.objects.all()
    serializer_class = PagerSerialiser
    pagination_class = PageNumberPagination

    def list(self, request, *args, **kwargs):
        # 获取数据
        roles = self.get_queryset()  # models.Role.objects.all()

        # [1, 1000,]     [1,10]
        pager_roles = self.paginate_queryset(roles)

        # 序列化
        ser = self.get_serializer(instance=pager_roles, many=True)

        return Response(ser.data)

"""


from api.utils.serializsers.pager import PagerSerialiser
from rest_framework.viewsets import GenericViewSet,ModelViewSet
from rest_framework.mixins import ListModelMixin,CreateModelMixin

class View1View(ModelViewSet):
    queryset = models.Role.objects.all()
    serializer_class = PagerSerialiser
    pagination_class = PageNumberPagination


##################  渲染器  ####################
from rest_framework.renderers import JSONRenderer,BrowsableAPIRenderer

class TestView(APIView):
    # renderer_classes = [JSONRenderer,BrowsableAPIRenderer]
    def get(self, request, *args, **kwargs):
        # 获取所有数据
        roles = models.Role.objects.all()

        # 创建分页对象
        # pg = CursorPagination()
        pg = MyCursorPagination()

        # 在数据库中获取分页的数据
        pager_roles = pg.paginate_queryset(queryset=roles, request=request, view=self)

        # 对数据进行序列化
        ser = PagerSerialiser(instance=pager_roles, many=True)

        return Response(ser.data)
