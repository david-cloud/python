import os


if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bbs.settings")

    import django
    django.setup()

    # from blog import models
    # ret = models.Article.objects.first().comment_set.all()
    # print(ret)


    # 由于重写了Django auth模块原有的用户认证表 User ---> UserInfo
    # 所以User 相关的使用都要改为 UserInfo
    # User.objects.create(username="alex", password="alexdsb")  # 不用这个
    # User.objects.create_superuser()

    # from django.contrib.auth.models import User
    # user = User.objects.get(username='admin')
    # user.set_password('new_password')
    # user.save()

    # from blog import models
    # user_obj = models.UserInfo.objects.get(username='admin')
    # 校验密码是否正确
    # ret = user_obj.check_password("123456")
    # print(ret)
    # 修改密码
    # user_obj.set_password("GOODluck135%%##")
    # user_obj.save()
    # return HttpResponse("o98k")

    from blog import models
    user = models.UserInfo.objects.filter(username='david').first()
    blog = user.blog.theme
    print(blog)
