# Generated by Django 3.1.7 on 2022-05-02 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_auto_20220429_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='financefiles',
            name='financ_zvit',
            field=models.FileField(blank=True, null=True, upload_to='files', verbose_name='PDF-файл'),
        ),
    ]
