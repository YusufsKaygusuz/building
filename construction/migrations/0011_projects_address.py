# Generated by Django 4.2.5 on 2023-12-27 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('construction', '0010_projects_detail_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='address',
            field=models.TextField(default=''),
        ),
    ]
