# Generated by Django 3.1.7 on 2022-05-02 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_auto_20220427_0857'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='infopage',
            options={'verbose_name': 'Сторінку', 'verbose_name_plural': 'Сторінки'},
        ),
        migrations.AlterField(
            model_name='financefiles',
            name='financ_zvit',
            field=models.FileField(blank=True, null=True, upload_to='files', verbose_name='PDF-файл'),
        ),
        migrations.AlterField(
            model_name='infopage',
            name='post',
            field=models.TextField(verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='infopage',
            name='tab',
            field=models.ForeignKey(default='Документи', on_delete=django.db.models.deletion.SET_DEFAULT, to='main.sitetab', verbose_name='Вкладка на якій буде сторінка'),
        ),
    ]
