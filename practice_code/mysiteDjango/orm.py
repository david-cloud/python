import os
import sys

if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysiteDjango.settings")
    import django
    django.setup()

    from app01 import models

    # ret = models.Publisher.objects.first()
    # ret = models.Publisher.objects.all().order_by("id")
    # ret = models.Publisher.objects.get(book__id=1)
    # ret = models.Publisher.objects.get(id=1, name='新华社第一分社')
    # ret = models.Publisher.objects.filter(id=1).values("name")
    # ret = models.Publisher.objects.all().values("id", "name")
    # ret = models.Publisher.objects.filter(id__gt=2).values("id", "name")
    # ret = models.Publisher.objects.filter(name__contains="中关").values("id", "name")
    # ret = models.Publisher.objects.filter(id=1).values("book__title")
    # ret = models.Book.objects.filter(id=1).values("publisher__name")
    # ret = models.Book.objects.get(id=1).publisher.name
    # ret = models.Book.objects.count()
    from django.db.models import F, Q
    # ret = models.Book.objects.filter(Q(id=1) | Q(publisher__name="中关村报社"))

    from django.db.models import Avg, Sum, Max, Min, Count
    # ret = models.Book.objects.all().aggregate(Count("title"))
    # ret = models.Book.objects.filter(id=1).aggregate(book_count=Count("title"))
    # ret = models.Book.objects.aggregate(book_count=Count("title"))
    # ret = models.Book.objects.annotate(author_count=Count("author__name")).values("author_count", "title")
    # print(ret)


