# Generated by Django 4.1.7 on 2023-04-05 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_blogcategory_projectcategory_servicecategory_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcategory',
            name='name',
            field=models.CharField(max_length=60, verbose_name='BlogCategory name'),
        ),
    ]
