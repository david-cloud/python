from django.db import models

# Create your models here.
# ORM相关的只能写在这个文件里,写到别的文件里Django找不到


class UserInfo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(null=False, max_length=32)

    def __str__(self):
        return "<UserInfo object: {}>".format(self.name)

# 出版社
class Publisher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=63, null=False, unique=True)

    def __str__(self):
        return "<Publisher object: {}>".format(self.name)
# 图书
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=64, null=False, unique=True)
    # 和出版社关联的外键字段, publisher在python里是一个对象，在数据创建时会自动加_id -->publisher_id
    publisher = models.ForeignKey(to="Publisher", on_delete=models.CASCADE)

    def __str__(self):
        return "Book object: {}".format(self.title)

# 作者
class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, null=False, unique=True)
    # 告诉ORM 我这张表和book表是多对多的关联关系,ORM自动帮我生成了第三张表
    book = models.ManyToManyField(to="Book")

    def __str__(self):
        return "Author object: {}".format(self.name)