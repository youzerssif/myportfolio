# Generated by Django 3.1.7 on 2021-07-29 11:09

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='imageblog'),
        ),
    ]