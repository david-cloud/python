# Generated by Django 2.0.1 on 2023-09-20 04:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20230920_1227'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='group',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.UserGroup'),
        ),
    ]
