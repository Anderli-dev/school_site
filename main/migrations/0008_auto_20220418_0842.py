# Generated by Django 3.1.7 on 2022-04-18 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20210511_2133'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='finance',
            options={'verbose_name': 'Державне забезпечення', 'verbose_name_plural': 'Державне забезпечення'},
        ),
        migrations.AlterField(
            model_name='blogpsychologa',
            name='short_post',
            field=models.TextField(blank=True, null=True, verbose_name='Короткий опис'),
        ),
        migrations.AlterField(
            model_name='news',
            name='short_post',
            field=models.TextField(blank=True, null=True, verbose_name='Короткий опис'),
        ),
    ]
