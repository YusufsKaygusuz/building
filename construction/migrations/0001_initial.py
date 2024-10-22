# Generated by Django 4.2.5 on 2023-12-22 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=60)),
                ('description', models.CharField(max_length=100)),
                ('video', models.CharField(max_length=50)),
                ('firstChartNumber', models.CharField(max_length=10)),
                ('firstChartDescription', models.CharField(max_length=30)),
                ('secondChartNumber', models.CharField(max_length=10)),
                ('secondChartDescription', models.CharField(max_length=30)),
                ('thirdChartNumber', models.CharField(max_length=10)),
                ('thirdChartDescription', models.CharField(max_length=30)),
                ('fourthChartNumber', models.CharField(max_length=10)),
                ('fourthChartDescription', models.CharField(max_length=30)),
                ('slug', models.SlugField(blank=True)),
                ('isActive', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_surname', models.CharField(max_length=50)),
                ('image', models.CharField(max_length=50)),
                ('comment', models.TextField()),
                ('isActive', models.BooleanField(default=False)),
                ('score', models.PositiveIntegerField()),
                ('slug', models.SlugField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_telephone', models.CharField(max_length=18)),
                ('second_telephone', models.CharField(max_length=18)),
                ('e_mail_address', models.EmailField(max_length=254)),
                ('maps_address', models.TextField()),
                ('date', models.DateField(auto_now=True)),
                ('slug', models.SlugField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='HeaderIntroduction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('background_image', models.CharField(max_length=50)),
                ('slug', models.SlugField(blank=True)),
                ('isActive', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=25)),
                ('mini_description', models.CharField(max_length=25)),
                ('image_front', models.CharField(max_length=50)),
                ('image_back', models.CharField(max_length=50)),
                ('isActive', models.BooleanField(default=False)),
                ('slug', models.SlugField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=25)),
                ('description', models.TextField()),
                ('image', models.CharField(max_length=50)),
                ('isActive', models.BooleanField(default=False)),
                ('slug', models.SlugField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='SocialAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faceaccount', models.CharField(max_length=100)),
                ('instaccount', models.CharField(max_length=100)),
                ('twitteraccount', models.CharField(max_length=100)),
                ('linkedinaccount', models.CharField(max_length=100)),
                ('googlemaps', models.TextField()),
                ('slug', models.SlugField(blank=True)),
            ],
        ),
    ]
