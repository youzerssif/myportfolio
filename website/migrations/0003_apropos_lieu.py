# Generated by Django 3.1.7 on 2021-03-01 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20210224_1011'),
    ]

    operations = [
        migrations.AddField(
            model_name='apropos',
            name='lieu',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
