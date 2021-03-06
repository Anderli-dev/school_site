# Generated by Django 3.1.7 on 2022-04-27 05:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_auto_20220427_0746'),
    ]

    operations = [
        migrations.CreateModel(
            name='InfoPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('post_date', models.DateField(auto_now_add=True)),
                ('slug', models.SlugField(default='', unique=True)),
                ('post', models.TextField(verbose_name='Текст поста')),
                ('tab', models.ForeignKey(default='Документи', on_delete=django.db.models.deletion.SET_DEFAULT, to='main.sitetab', verbose_name='Вкладка на якій буде cnjhsyrf')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Пости',
            },
        ),
        migrations.DeleteModel(
            name='DistanceStudy',
        ),
        migrations.DeleteModel(
            name='InfoTab',
        ),
    ]
