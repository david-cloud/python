import os


if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysiteDjango.settings")
    import django
    django.setup()

    from app3 import models
    # 批量创建
    # 有100个书籍对象
    obj = [models.Book(title="沙河{}".format(i)) for i in range(1500)]
    # 在数据库中批量创建, 10次一提交
    models.Book.objects.bulk_create(obj, 10)
    # models.Book.objects.all().delete()