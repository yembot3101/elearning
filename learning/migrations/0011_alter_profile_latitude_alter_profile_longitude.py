# Generated by Django 4.0.4 on 2022-05-13 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0010_profile_statisfy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='latitude',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='longitude',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
    ]
