# Generated by Django 3.1.7 on 2022-04-26 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_auto_20220426_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpsychologa',
            name='author',
            field=models.CharField(default='Психолог', max_length=128, verbose_name='Автор поста'),
        ),
    ]