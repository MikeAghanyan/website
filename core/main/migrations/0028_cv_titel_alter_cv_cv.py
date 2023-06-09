# Generated by Django 4.1.7 on 2023-04-05 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0027_cv'),
    ]

    operations = [
        migrations.AddField(
            model_name='cv',
            name='titel',
            field=models.CharField(default=11, max_length=30, verbose_name='CV titel'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cv',
            name='cv',
            field=models.FileField(upload_to='media', verbose_name='CV file'),
        ),
    ]
