from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=32)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "book"
