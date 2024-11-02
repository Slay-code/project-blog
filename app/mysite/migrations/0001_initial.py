# Generated by Django 5.0.7 on 2024-10-19 19:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryGame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название')),
                ('slug', models.SlugField(blank=True, null=True, unique=True, verbose_name='URL')),
            ],
            options={
                'db_table': 'CategoryGame',
            },
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название')),
                ('slug', models.SlugField(blank=True, null=True, unique=True, verbose_name='URL')),
                ('description', models.TextField(blank=True, default='Нет описания', verbose_name='Описание')),
                ('iamge', models.ImageField(blank=True, max_length=1000, upload_to='foto', verbose_name='Изображение')),
                ('time_created', models.DateTimeField(auto_now_add=True, verbose_name='Время публикации')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.categorygame', verbose_name='Категория')),
            ],
            options={
                'db_table': 'Game',
            },
        ),
    ]