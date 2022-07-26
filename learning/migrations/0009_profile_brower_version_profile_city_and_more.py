# Generated by Django 4.0.4 on 2022-05-13 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0008_alter_payed_class_ref_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='brower_version',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='city',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='continent',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='device_type',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='error',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='os_version',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='postal',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='timeZone',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
