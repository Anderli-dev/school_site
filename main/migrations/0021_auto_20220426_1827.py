# Generated by Django 3.1.7 on 2022-04-26 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_auto_20220426_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpsychologa',
            name='author',
            field=models.CharField(default='Психолог', max_length=50),
        ),
        migrations.AlterField(
            model_name='news',
            name='author',
            field=models.CharField(default='Адміністратор', max_length=50),
        ),
    ]
