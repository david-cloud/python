from django.shortcuts import render
from django.shortcuts import HttpResponse, redirect
from app01 import models
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.


def login(request):
    error_msg = ''
    if request.method == "POST":
        print(request.POST)
        email = request.POST.get("email",None)
        pwd = request.POST.get("pwd",None)
        print(email, pwd)
        if email == "123456@daimler.com" and pwd == "123456":
            #return redirect("/user_list/")
            return redirect("/publisher_list/")
        else:
            error_msg = "邮箱或密码错误!"
    return render(request, "login.html", {"error": error_msg})


def index(request):
    return HttpResponse('login success!')


def user_list(request):
    user_info = models.UserInfo.objects.all()
    #print(user_info)
    #print(user_info[0].id, user_info[0].name)
    #print(user_info[0])
    return render(request, 'user_list.html', {'user_list': user_info})


def add_user(request):
    if request.method == "POST":
        new_name = request.POST.get("username", None)
        #new_name = request.POST.get("username")
        models.UserInfo.objects.create(name=new_name)
        return redirect("/user_list/")
    return render(request, "add_user.html")


############ publisher
def publisher_list(request):
    ret = models.Publisher.objects.all()
    return render(request, 'publisher_list.html', {'publisher_list': ret})


def add_publisher(request):
    error_msg = ''
    if request.method == 'POST':
        new_name = request.POST.get('publisher_name')
        if new_name:
            models.Publisher.objects.create(name=new_name)
            return redirect('/publisher_list/')
        else:
            error_msg = "名字不能为空！"
    return render(request, 'add_publisher.html', {'error': error_msg})


def delete_publisher(request):
    publisher_id = request.GET.get('id')
    print(publisher_id)
    try:
        if publisher_id:
            publisher_obj = models.Publisher.objects.get(id=publisher_id)
            print(publisher_obj)
            publisher_obj.delete()
            return redirect('/publisher_list/')
        else:
            return HttpResponse("ID不存在！")
    except ObjectDoesNotExist:
        return HttpResponse("不存在此数据，ID不存在！")


def edit_publisher(request):
    if request.method == 'POST':
        publisher_id = request.POST.get('id')  # 隐藏ID
        print(publisher_id)
        new_name = request.POST.get('publisher_name')
        print(new_name)
        if new_name:
            publisher_obj = models.Publisher.objects.get(id=publisher_id)
            publisher_obj.name = new_name
            publisher_obj.save()
            return redirect('/publisher_list/')
        else:
            error_msg = "名字不能为空！"
        return render(request, 'edit_publisher.html', {'error': error_msg})
    elif request.method == 'GET':
        try:
            publisher_id = request.GET.get('id')
            publisher_obj = models.Publisher.objects.get(id=publisher_id)
            return render(request, 'edit_publisher.html', {'publisher': publisher_obj})
        except ObjectDoesNotExist:
            return HttpResponse("不存在此数据，ID不存在,无法编辑！")


######## BOOK
def book_list(request):
    all_book = models.Book.objects.all()
    return render(request, "book_list.html", {"all_book": all_book})


def add_book(request):
    if request.method == "POST":
        new_title = request.POST.get("book_title")
        # 这里获取的值为select框 value的值 - value="{{ publisher.id }}
        publisher_id = request.POST.get("publisher")
        models.Book.objects.create(title=new_title, publisher_id=publisher_id)
        return redirect("/book_list/")

    ret = models.Publisher.objects.all()
    return render(request, "add_book.html", {"publisher_list": ret})


def delete_book(request):
    delete_book_id = request.GET.get("id")
    book_obj = models.Book.objects.get(id=delete_book_id)
    book_obj.delete()
    return redirect("/book_list/")


def edit_book(request):
    if request.method == "POST":
        book_id = request.POST.get("id")
        book_title = request.POST.get("book_title")
        publisher_id = request.POST.get("publisher")
        book_obj = models.Book.objects.get(id=book_id)
        book_obj.title = book_title
        book_obj.publisher_id = publisher_id
        book_obj.save()
        return redirect("/book_list/")
    edit_book_id = request.GET.get("id")
    book_obj = models.Book.objects.get(id=edit_book_id)
    publisher_ret = models.Publisher.objects.all()
    return render(
        request,
        "edit_book.html",
        {"book_obj": book_obj, "publisher_list": publisher_ret},
    )


# 作者
def author_list(request):
    author_obj = models.Author.objects.all()
    return render(request, "author_list.html", {"author_list": author_obj})


def add_author(request):
    if request.method == "POST":
        new_author_name = request.POST.get("author_name")
        # post提交的数据是多个值的时候一定会要用getlist,如多选的checkbox和多选的select
        books = request.POST.getlist("books")
        #print(books)
        new_author_obj = models.Author.objects.create(name=new_author_name)
        # 把新作者和书籍建立对应关系,自动提交， 使用.set, books参数不能加引号
        new_author_obj.book.set(books)
        return redirect("/author_list/")
    book_obj = models.Book.objects.all()
    return render(request, "add_author.html", {"book_list": book_obj})


def delete_author(request):
    delete_author_id = request.GET.get("id")
    # 根据ID值取到要删除的作者对象,直接删除(ORM会自动将关联数据删除)
    # 1. 去作者表把作者删了
    # 2. 去作者和书的关联表,把对应的关联记录删除了
    models.Author.objects.get(id=delete_author_id).delete()
    return redirect("/author_list/")


def edit_author(request):
    if request.method == "POST":
        # 拿到提交过来的编辑后的数据
        edit_author_id = request.POST.get("author_id")
        new_author_name = request.POST.get("author_name")
        # 拿到编辑后作者关联的书籍信息
        new_books = request.POST.getlist("books")
        # 根据ID找到当前编辑的作者对象
        edit_author_obj = models.Author.objects.get(id=edit_author_id)
        # 更新作者的名字
        edit_author_obj.name = new_author_name
        # 更新作者关联的书的对应关系
        edit_author_obj.book.set(new_books)
        # 将修改提交到数据库
        edit_author_obj.save()
        # 返回作者列表页,查看是否编辑成功
        return redirect("/author_list/")

    edit_author_id = request.GET.get("id")
    edit_author_obj = models.Author.objects.get(id=edit_author_id)
    all_book_obj = models.Book.objects.all()
    return render(
        request,
        "edit_author.html",
        {"author": edit_author_obj, "book_list": all_book_obj}
    )


####################################### filter ###
# 测试用类
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        return '{} 今天好开心,跑了三米'.format(self)

    def __str__(self):
        return '<Person-object {}>'.format(self.name)


# 模板语言测试相关
def template_test(request):
    file_size = 123456789876543
    from datetime import datetime
    now = datetime.now()
    print("=" * 80)
    print(now)
    print("=" * 80)

    a_html = "<a href='http://www.sogo.com'>我是后端传过来的a标签</a>"
    script_html = "<script>for(var i=0;i<100;i++){alert(123);}</script>"

    p_str = """
        在苍茫的大海上，狂风卷积着乌云，在乌云和大海之间，海燕像黑色的闪电，在高傲地飞翔。
    """

    name_list = ['张三', '李四', '王五']
    name_list2 = [['张三0', '李四0', '王五0'], ['张三1', '李四1', '王五1']]

    name_dict = {'name1': '小黑', 'name2': '长江', 'name3': '诸葛亮'}
    p1 = Person('小白', 9000)
    p2 = Person('小黑', 10000)
    return render(
        request,
        't_text.html',
        {
            'name': '王镇', 'age': 18,
            'name_list': name_list,
            'name_list2': name_list2,
            'name_dict': name_dict,
            'p1': p1,
            'p2': p2,
            "file_size": file_size,
            "now": now,
            "a_html": a_html,
            "script_html": script_html,
            "p_str": p_str
        }
    )


#############################
def book(request, year, title):
    print(year, type(year))
    print(title, type(title))
    return HttpResponse("book list!!")

# def book(request):
#     return HttpResponse("book list!!")
