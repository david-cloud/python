from django.shortcuts import render, redirect

# Create your views here.
from functools import wraps


def check_login(func):
    @wraps(func)  # 装饰器修复技术
    def inner(request, *args, **kwargs):
        ret = request.get_signed_cookie("is_login", default="0", salt="s10nb")
        if ret == "1":
            # 已经登陆过的 继续执行
            return func(request, *args, **kwargs)
        # 没有登录过的 跳转到登录页面
        else:
            # 获取当前访问的URL
            next_url = request.path_info
            print(next_url)
            return redirect("/login/?next={}".format(next_url))
    return inner


def login(request):
    print(request.get_full_path())  # 获取当前请求的路径和参数
    print(request.path_info)  # 取当前请求的路径
    print("-" * 120)

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
                rep = redirect("/home/")  # 得到一个响应对象

            # rep.set_cookie("is_login", "1")
            # 设置加盐的cookie
            rep.set_signed_cookie("is_login", "1", salt="s10nb", max_age=10)  # 单位是秒
            return rep

    return render(request, "login.html")


def home(request):
    # 从请求的cookie中找 有没有 xiaohei
    # ret = request.COOKIES.get("is_login", 0)
    # 取加盐过的
    ret = request.get_signed_cookie("is_login", default="0", salt="s10nb")
    print(ret, type(ret))
    if ret == "1":
        # 表示已经登陆过
        return render(request, "home.html")
    else:
        return redirect("/login/")

@check_login
def index(request):

    return render(request, "index.html")


# 注销函数
def logout(request):
    # 如何删除Cookie
    rep = redirect("/login/")
    rep.delete_cookie("is_login")
    return rep