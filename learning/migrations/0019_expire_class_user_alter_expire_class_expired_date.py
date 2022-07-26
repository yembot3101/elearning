# Generated by Django 4.0.4 on 2022-05-17 22:04

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('learning', '0018_remove_expire_class_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='expire_class',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='expire_class',
            name='expired_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 17, 23, 4, 51, 952660)),
        ),
    ]
