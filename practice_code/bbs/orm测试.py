import os

if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bbs.settings")

    import django
    django.setup()

    from blog import models
    from django.db.models import Count
    print(models.UserInfo.objects.filter(username='david'))
    print(models.UserInfo.objects.get(username='david'))
    user = models.UserInfo.objects.filter(username='david').first()
    print(user)
    print("*" * 120)
    blog = user.blog
    print(blog)
    print("*" * 120)
    category_list = models.Category.objects.filter(blog=blog).annotate(c=Count("article")).values("title", "c")
    print(category_list)
    print("*" * 120)
    # print(models.Category.objects.filter(blog=blog).annotate(c=Count("article"))).values("title", "c")