# Generated by Django 3.1.7 on 2021-04-12 17:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0004_blogpsychologa'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpsychologa',
            name='img',
            field=models.ImageField(default=1, upload_to='', verbose_name='Зображення'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('img', models.ImageField(upload_to='', verbose_name='Зображення')),
                ('short_post', models.TextField(verbose_name='Короткий опис')),
                ('post_date', models.DateField(auto_now_add=True)),
                ('slug', models.SlugField(default='', unique=True)),
                ('post', models.TextField(verbose_name='Текст поста')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор поста')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Новини',
            },
        ),
    ]
