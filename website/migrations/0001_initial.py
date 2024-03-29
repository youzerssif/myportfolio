# Generated by Django 3.1.7 on 2021-04-11 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apropos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200, null=True)),
                ('image', models.FileField(null=True, upload_to='monimage')),
                ('description', models.TextField()),
                ('email', models.EmailField(max_length=254, null=True)),
                ('numero', models.CharField(max_length=50, null=True)),
                ('lieu', models.CharField(max_length=50, null=True)),
                ('facebook', models.URLField(blank=True, null=True)),
                ('twitter', models.URLField(blank=True, null=True)),
                ('linkedin', models.URLField(blank=True, null=True)),
                ('instagram', models.URLField(blank=True, null=True)),
                ('googlemap', models.CharField(max_length=254, null=True)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_upd', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Apropos',
                'verbose_name_plural': 'Aproposs',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50, null=True)),
                ('numero', models.CharField(max_length=50, null=True)),
                ('sujet', models.CharField(max_length=50, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('message', models.TextField()),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_upd', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contacts',
            },
        ),
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_upd', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Newsletter',
                'verbose_name_plural': 'Newsletters',
            },
        ),
        migrations.CreateModel(
            name='Statistique',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_heureux', models.IntegerField()),
                ('projet_realises', models.IntegerField()),
                ('heures_works', models.IntegerField()),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_upd', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Statistique',
                'verbose_name_plural': 'Statistiques',
            },
        ),
    ]
