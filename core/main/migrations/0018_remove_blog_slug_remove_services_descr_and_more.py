# Generated by Django 4.1.7 on 2023-04-02 12:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_alter_servicesall_options_remove_servicesall_descr_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='services',
            name='descr',
        ),
        migrations.RemoveField(
            model_name='services',
            name='img_main',
        ),
        migrations.RemoveField(
            model_name='services',
            name='slug',
        ),
        migrations.AddField(
            model_name='blog',
            name='img1',
            field=models.ImageField(blank=True, upload_to='media/blog', verbose_name='Blog image'),
        ),
        migrations.AddField(
            model_name='blog',
            name='img2',
            field=models.ImageField(blank=True, upload_to='media/blog', verbose_name='Blog image'),
        ),
        migrations.AddField(
            model_name='blog',
            name='text1',
            field=models.TextField(blank=True, verbose_name='Blog text1'),
        ),
        migrations.AddField(
            model_name='blog',
            name='text2',
            field=models.TextField(blank=True, verbose_name='Blog text2'),
        ),
        migrations.AddField(
            model_name='blog',
            name='text3',
            field=models.TextField(blank=True, verbose_name='Blog text3'),
        ),
        migrations.AddField(
            model_name='blog',
            name='text4',
            field=models.TextField(blank=True, verbose_name='Blog text4'),
        ),
        migrations.AddField(
            model_name='blog',
            name='text5',
            field=models.TextField(blank=True, verbose_name='Blog text5'),
        ),
        migrations.AddField(
            model_name='blog',
            name='text6',
            field=models.TextField(blank=True, verbose_name='Blog text6'),
        ),
        migrations.AddField(
            model_name='servicesall',
            name='descr',
            field=models.CharField(blank=True, max_length=300, verbose_name='ServicessAll description'),
        ),
        migrations.AddField(
            model_name='servicesall',
            name='img_main',
            field=models.ImageField(blank=True, upload_to='media/service', verbose_name='ServicessAll image'),
        ),
        migrations.AddField(
            model_name='servicesall',
            name='slug',
            field=models.SlugField(blank=True, unique=True, verbose_name='ServicesAll link'),
        ),
        migrations.AlterField(
            model_name='services',
            name='service_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to='main.servicesall'),
        ),
        migrations.DeleteModel(
            name='Article',
        ),
    ]
