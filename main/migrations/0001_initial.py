# Generated by Django 3.1.7 on 2021-03-27 23:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Назва документа')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='Посилання')),
            ],
            options={
                'verbose_name': 'Документ',
                'verbose_name_plural': 'Документи',
            },
        ),
        migrations.CreateModel(
            name='DocumentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DocumentFiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documents', models.FileField(upload_to='files', verbose_name='PDF-файл')),
                ('Document', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='main.document')),
            ],
        ),
        migrations.AddField(
            model_name='document',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.documenttype', verbose_name='Тип документу'),
        ),
    ]
