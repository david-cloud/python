from django.shortcuts import render, redirect
from django import views

# Create your views here.
from functools import wraps
# Django提供的工具，把函数装饰器转变成方法装饰器
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt, csrf_protect


def check_login(func):
    @wraps(func)  # 装饰器修复技术
    def inner(request, *args, **kwargs):
        ret = request.session.get("is_login")
        # 1. 获取cookie中的随机字符串
        # 2. 根据随机字符串去数据库取 session_data --> 解密 --> 反序列化成字典
        # 3. 在字典里面 根据 is_login 取具体的数据
        if ret == "1":
            # 已经登陆过的 继续执行
            return func(request, *args, **kwargs)
        # 没有登录过的 跳转到登录页面
        else:
            # 获取当前访问的URL
            next_url = request.path_info
            print(next_url)
            return redirect("/app02/login/?next={}".format(next_url))
    return inner


@csrf_exempt
def login(request):
    if request.method == "POST":
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")
        # 从URL里面取到 next 参数
        next_url = request.GET.get("next")

        if user == "alex" and pwd == "dsb":
            # 登陆成功
            # 告诉浏览器保存一个键值对

            if next_url:
                rep = redirect(next_url)  # 得到一个响应对象
            else:
                rep = redirect("/app02/home/")  # 得到一个响应对象
            # 设置session
            request.session["is_login"] = "1"
            request.session["name"] = user
            request.session.set_expiry(7)  # 7秒钟之后失效
            return rep

    return render(request, "app02/login.html")


@check_login
def home(request):
    user = request.session.get("name")
    return render(request, "app02/home.html", {"user": user})


@check_login
def index(request):

    return render(request, "app02/index.html")


# 注销函数
def logout(request):
    # 只删除session数据
    # request.session.delete()
    # 如何删除session数据和cookie
    request.session.flush()
    return redirect("/app02/login/")


# @method_decorator(check_login, name="get")
class UserInfo(views.View):

    @method_decorator(check_login)
    def get(self, request):
        return render(request, "app02/userinfo.html")
