# Generated by Django 4.1.7 on 2023-04-01 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_servicesmain_remove_blog_slug_remove_services_descr_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='slug',
        ),
        migrations.AddField(
            model_name='blog',
            name='slug',
            field=models.SlugField(blank=True, unique=True, verbose_name='Blog link'),
        ),
    ]
