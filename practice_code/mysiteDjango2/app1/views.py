from django.shortcuts import render, redirect

# Create your views here.
from functools import wraps


def check_login(func):
    @wraps(func)     # 装饰器修复技术
    def inner(request, *args, **kwargs):
        ret = request.get_signed_cookie("is_login", default="0", salt="s10nb")
        if ret == "1" :
            # 已登录过的 继续执行
            return func(request, *args, **kwargs)
        else:
            # 获取当前访问的url
            next_url = request.path_info
            print(next_url)
            return redirect("/app01/login/?next={}".format(next_url))
    return inner


def login(request):
    print(request.get_full_path)  # 全路径
    print(request.path_info)   # 当前路径
    print('*'*120)

    if request.method == "POST":
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')

        # 从URL里面取到 next 参数
        next_url = request.GET.get("next")

        if user == "david" and pwd == "123456":
            # 登陆成功
            # 告诉浏览器保存一个键值对
            if next_url:
                rep = redirect(next_url)  # 得到一个响应对象
            else:
                rep = redirect("app01/home")  # 得到一个响应对象

            rep.set_signed_cookie("is_login", "1", salt="s10nb", max_age=10)  # 单位是秒
            return rep
    # 非POST 提交数据的请求， 则直接返回login页面
    return render(request, "app01/login.html")


@check_login
def home(request):
    return render(request, "app01/home.html")


@check_login
def index(request):
    return render(request, "app01/index.html")


def logout(request):
    # 删除cookie
    rep = redirect("/app01/login")
    rep.delete_cookie("is_login")  # 先获取要返回的对象， 然后操作cookie
    return rep