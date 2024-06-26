from django.shortcuts import render

# Create your views here.

from app3 import models


def books(request):
    # 从URL取参数
    page_num = request.GET.get("page")
    print(page_num, type(page_num))

    # 总数据是多少
    total_count = models.Book.objects.all().count()

    # 调用一个类
    from utils.mypage import Page
    page_obj = Page(page_num, total_count, per_page=10, url_prefix="/app3/books/", max_page=9, )
    ret = models.Book.objects.all()[page_obj.start:page_obj.end]
    page_html = page_obj.page_html()
    return render(request, "app3/books.html", {"books": ret, "page_html": page_html})
