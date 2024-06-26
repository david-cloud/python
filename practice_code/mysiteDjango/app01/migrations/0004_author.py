# Generated by Django 2.0.1 on 2023-06-28 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_auto_20230627_1700'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64, unique=True)),
                ('book', models.ManyToManyField(to='app01.Book')),
            ],
        ),
    ]
