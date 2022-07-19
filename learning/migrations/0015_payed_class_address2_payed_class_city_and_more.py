# Generated by Django 4.0.4 on 2022-05-17 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0014_alter_ban_receiver'),
    ]

    operations = [
        migrations.AddField(
            model_name='payed_class',
            name='address2',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='payed_class',
            name='city',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='payed_class',
            name='country',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='payed_class',
            name='email',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='payed_class',
            name='fname',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='payed_class',
            name='lname',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='payed_class',
            name='payment_mode',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='payed_class',
            name='state',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='payed_class',
            name='uname',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='payed_class',
            name='zip',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
