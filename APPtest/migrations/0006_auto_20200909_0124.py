# Generated by Django 3.1.1 on 2020-09-08 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APPtest', '0005_ordereditem_orderdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordereditem',
            name='OrderDate',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
