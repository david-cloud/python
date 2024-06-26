from django.shortcuts import render, HttpResponse

# Create your views here.

from django.views import View
# CBV版 上传文件


class UploadFile(View):
    """
    保存上传文件前，数据需要存放在某个位置。默认当上传文件小于2.5M时，django会将上传文件的全部内容读进内存。从内存读取一次，写磁盘一次。
    但当上传文件很大时，django会把上传文件写到临时文件中，然后存放到系统临时文件夹中。
    :param request:
    :return:
    """
    @staticmethod
    def get(request):
        # print(year, type(year))
        # print(title, type(title))
        return render(request, "upload.html")

    @staticmethod
    def post(request):
        print(request.FILES, type(request.FILES))
        print(request.FILES["upload_file"], type(request.FILES["upload_file"]))
        print(request.FILES["upload_file"].name, type(request.FILES["upload_file"].name))

        # 从请求的FILES中获取上传文件的文件名，file为页面上type=files类型input的name属性值
        filename = request.FILES["upload_file"].name
        # # 在项目目录下新建一个文件
        with open(filename, "wb") as f:
            # 从上传的文件对象中一点一点读
            for i in request.FILES["upload_file"].chunks():
                # 写入本地文件
                f.write(i)
        return HttpResponse("上传OK")


# 分组命名匹配  处理函数需要接受对应参数
def book(request, year, title):
    print(year, type(year))
    print(title, type(title))
    return HttpResponse("app2 book list!!")