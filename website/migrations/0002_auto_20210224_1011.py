# Generated by Django 3.1.7 on 2021-02-24 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apropos',
            name='facebook',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='apropos',
            name='instagram',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='apropos',
            name='linkedin',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='apropos',
            name='twitter',
            field=models.URLField(blank=True, null=True),
        ),
    ]
