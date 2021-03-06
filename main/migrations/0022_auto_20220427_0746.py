# Generated by Django 3.1.7 on 2022-04-27 04:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_auto_20220426_1827'),
    ]

    operations = [
        migrations.CreateModel(
            name='InfoTab',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='bullying',
            name='author',
            field=models.CharField(default='Адміністратор', max_length=50),
        ),
        migrations.AddField(
            model_name='bullying',
            name='img',
            field=models.ImageField(default=1, upload_to='img', verbose_name='Зображення'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bullying',
            name='post_date',
            field=models.DateField(auto_now_add=True, default='2022-02-20'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bullying',
            name='short_post',
            field=models.TextField(blank=True, null=True, verbose_name='Прев’ю'),
        ),
        migrations.AlterField(
            model_name='blogpsychologa',
            name='short_post',
            field=models.TextField(blank=True, null=True, verbose_name='Прев’ю'),
        ),
        migrations.AlterField(
            model_name='blogpsychologa',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='bullying',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='distancestudy',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='document',
            name='tab',
            field=models.ForeignKey(default='Документи', on_delete=django.db.models.deletion.SET_DEFAULT, to='main.sitetab', verbose_name='Вкладка на якій буде знаходитися документ(-и)'),
        ),
        migrations.AlterField(
            model_name='news',
            name='short_post',
            field=models.TextField(blank=True, null=True, verbose_name='Прев’ю'),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Заголовок'),
        ),
    ]
