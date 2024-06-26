from django.shortcuts import render, redirect
from django import views

# Create your views here.
from functools import wraps
from django.utils.decorators import method_decorator


def check_login(func):
    @wraps(func)
    def inner(request, *args, **kwargs):
        ret = request.session.get("is_login")
        if ret == "1":
            return func(request, *args, **kwargs)
        else:
            next_url = request.path_info
            print(next_url)
            return redirect("/app02/login?next={}".format(next_url))
    return inner


def login(request):
    print(request.get_full_path)
    print(request.path_info)
    print("*"*120)

    if request.method == "POST":
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")
        next_url = request.GET.get("next")

        if user == "david" and pwd == "123456":
            if next_url:
                rep = redirect(next_url)
            else:
                rep = redirect("/app02/home")
            # 设置session, 存储到服务器端 数据库session表中 [session需要定期用脚本清理]
            request.session["is_login"] = "1"
            request.session["name"] = user
            request.session.set_expiry(7)  # 7秒钟之后失效
            return rep

    return render(request, "app02/login.html")


@check_login
def home(request):
    user = request.session.get("name")
    ret = request.session.get("is_login")
    print(user, ret)
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


# 类里的 方法装饰器
class UserInfo(views.View):

    @method_decorator(check_login)
    def get(self, request):
        return render(request, "app02/userinfo.html")
