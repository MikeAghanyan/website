# Generated by Django 4.1.7 on 2023-04-03 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_remove_blog_slug_remove_services_descr_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='service_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='serv', to='main.servicesall'),
        ),
    ]
