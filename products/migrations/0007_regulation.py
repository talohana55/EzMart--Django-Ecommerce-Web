# Generated by Django 3.1.3 on 2020-12-27 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20201220_1553'),
    ]

    operations = [
        migrations.CreateModel(
            name='Regulation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('regulation', models.TextField()),
                ('last_changed', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
