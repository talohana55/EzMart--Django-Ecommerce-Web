# Generated by Django 3.1.3 on 2021-01-01 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_ordereditem_shop_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordereditem',
            name='shop_name',
        ),
    ]