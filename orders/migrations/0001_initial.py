# Generated by Django 3.1.3 on 2020-12-06 22:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderedItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='date_sold')),
                ('price', models.FloatField()),
                ('quantity', models.IntegerField()),
                ('product', models.CharField(max_length=200)),
                ('status', models.CharField(choices=[('created', 'Created'), ('paid', 'Paid'), ('shipped', 'Shipped')], default='created', max_length=120)),
                ('shipping_address', models.CharField(max_length=100)),
                ('buyer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Buyer', to=settings.AUTH_USER_MODEL)),
                ('seller', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Seller', to=settings.AUTH_USER_MODEL)),
            ],
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
