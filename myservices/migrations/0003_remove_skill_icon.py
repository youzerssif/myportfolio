# Generated by Django 3.1.7 on 2021-07-29 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myservices', '0002_auto_20210729_1118'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skill',
            name='icon',
        ),
    ]
