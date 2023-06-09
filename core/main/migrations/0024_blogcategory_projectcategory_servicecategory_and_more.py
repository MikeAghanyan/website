# Generated by Django 4.1.7 on 2023-04-05 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_remove_category_descr_remove_category_img_main_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='BlogCategory name')),
                ('active', models.BooleanField(blank=True, verbose_name='Blog active')),
                ('descr', models.TextField(blank=True, max_length=1500, verbose_name='BlogCaregory description')),
                ('img_main', models.ImageField(blank=True, upload_to='media/Blog_category', verbose_name='BlogCategory image')),
                ('date', models.DateField(blank=True, verbose_name='BlogCategory release time')),
                ('time', models.CharField(blank=True, max_length=2, verbose_name='BlogCategory reading time')),
            ],
            options={
                'verbose_name': 'BlogCategory',
                'verbose_name_plural': 'BlogCategories',
            },
        ),
        migrations.CreateModel(
            name='ProjectCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='ProjectCategory name')),
                ('descr', models.TextField(blank=True, max_length=1500, verbose_name='ProjectCaregory description')),
                ('img_main', models.ImageField(blank=True, upload_to='media', verbose_name='ProjectCategory image')),
            ],
            options={
                'verbose_name': 'ProjectCategory',
                'verbose_name_plural': 'ProjectCategories',
            },
        ),
        migrations.CreateModel(
            name='ServiceCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='ServiceCategory name')),
                ('descr', models.TextField(blank=True, max_length=1500, verbose_name='ServiceCaregory description')),
                ('img_main', models.ImageField(blank=True, upload_to='media/Service_category', verbose_name='ServiceCategory image')),
            ],
            options={
                'verbose_name': 'ServiceCategory',
                'verbose_name_plural': 'ServiceCategories',
            },
        ),
        migrations.CreateModel(
            name='SubBlogCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, unique=True, verbose_name='SubBlogCategory link')),
                ('titel', models.CharField(max_length=30, verbose_name='SubBlogCategory titel')),
                ('text1', models.TextField(blank=True, verbose_name='SubBlogCategory text1')),
                ('text2', models.TextField(blank=True, verbose_name='SubBlogCategory text2')),
                ('text3', models.TextField(blank=True, verbose_name='SubBlogCategory text3')),
                ('text4', models.TextField(blank=True, verbose_name='SubBlogCategory text4')),
                ('text5', models.TextField(blank=True, verbose_name='SubBlogCategory text5')),
                ('text6', models.TextField(blank=True, verbose_name='SubBlogCategory text6')),
                ('img_1', models.ImageField(blank=True, upload_to='media/Blog_category', verbose_name='SubBlogCategory image1')),
                ('img_2', models.ImageField(blank=True, upload_to='media/Blog_category', verbose_name='SubBlogCategory image2')),
                ('img_3', models.ImageField(blank=True, upload_to='media/Blog_category', verbose_name='SubBlogCategory image3')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_categ', to='main.blogcategory')),
            ],
            options={
                'verbose_name': 'SubBlogCategory',
                'verbose_name_plural': 'SubBlogCategories',
            },
        ),
        migrations.CreateModel(
            name='SubServiceCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, unique=True, verbose_name='SubServiceCategory link')),
                ('titel', models.CharField(max_length=30, verbose_name='SubServiceCategory titel')),
                ('text1', models.TextField(blank=True, verbose_name='SubServiceCategory text1')),
                ('text2', models.TextField(blank=True, verbose_name='SubServiceCategory text2')),
                ('text3', models.TextField(blank=True, verbose_name='SubServiceCategory text3')),
                ('text4', models.TextField(blank=True, verbose_name='SubServiceCategory text4')),
                ('text5', models.TextField(blank=True, verbose_name='SubServiceCategory text5')),
                ('text6', models.TextField(blank=True, verbose_name='SubServiceCategory text6')),
                ('img_1', models.ImageField(blank=True, upload_to='media/Service_category', verbose_name='SubServiceCategory image1')),
                ('img_2', models.ImageField(blank=True, upload_to='media/Service_category', verbose_name='SubServiceCategory image2')),
                ('img_3', models.ImageField(blank=True, upload_to='media/Service_category', verbose_name='SubServiceCategory image3')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service_categ', to='main.servicecategory')),
            ],
            options={
                'verbose_name': 'SubServiceCategory',
                'verbose_name_plural': 'SubServiceCategory',
            },
        ),
        migrations.RemoveField(
            model_name='subcategory',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='SubCategory',
        ),
    ]
