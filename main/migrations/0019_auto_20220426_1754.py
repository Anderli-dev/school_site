# Generated by Django 3.1.7 on 2022-04-26 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_auto_20220426_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpsychologa',
            name='author',
            field=models.TextField(default='Психолог', verbose_name='Автор поста'),
        ),
    ]
