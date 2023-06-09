# Generated by Django 4.1.7 on 2023-04-02 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_servicesall_remove_services_slug_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='servicesall',
            options={'verbose_name': 'ServisesAll', 'verbose_name_plural': 'ServicesAll'},
        ),
        migrations.RemoveField(
            model_name='servicesall',
            name='descr',
        ),
        migrations.RemoveField(
            model_name='servicesall',
            name='img_main',
        ),
        migrations.RemoveField(
            model_name='servicesall',
            name='slug',
        ),
        migrations.AddField(
            model_name='services',
            name='descr',
            field=models.CharField(default=1, max_length=300, verbose_name='ServicessAll description'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='services',
            name='img_main',
            field=models.ImageField(default=1, upload_to='media/service', verbose_name='ServicessAll image'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='services',
            name='slug',
            field=models.SlugField(blank=True, unique=True, verbose_name='ServicesAll link'),
        ),
    ]
