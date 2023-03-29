# Generated by Django 4.1.7 on 2023-03-25 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_delete_background_alter_project_descr_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='descr',
            field=models.CharField(max_length=300, verbose_name='Blog description'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='time',
            field=models.CharField(max_length=2, verbose_name='Blog reading time'),
        ),
    ]