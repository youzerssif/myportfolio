# Generated by Django 3.1.7 on 2021-02-24 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myservices', '0006_remove_service_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='pourcentage',
            field=models.IntegerField(null=True),
        ),
    ]
