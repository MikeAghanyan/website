# Generated by Django 4.1.7 on 2023-04-01 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70, verbose_name='Contacts full_name')),
                ('email', models.EmailField(max_length=254, verbose_name='Contacts email')),
                ('subject', models.CharField(max_length=70, verbose_name='Contacts subject')),
                ('message', models.TextField(verbose_name='Contacts message')),
            ],
            options={
                'verbose_name': 'Contacts',
                'verbose_name_plural': 'Contacts',
            },
        ),
    ]
