# Generated by Django 3.1.7 on 2021-03-27 23:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0003_finance_financefiles'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPsychologa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Назва поста')),
                ('short_post', models.TextField(verbose_name='Короткий опис')),
                ('post_date', models.DateField(auto_now_add=True)),
                ('slug', models.SlugField(default='', unique=True)),
                ('post', models.TextField(verbose_name='Текст поста')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор поста')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Блог психолога',
            },
        ),
    ]
