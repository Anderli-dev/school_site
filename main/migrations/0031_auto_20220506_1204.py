# Generated by Django 3.1.7 on 2022-05-06 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0030_distancelessons_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='distancelessons',
            options={'ordering': ('order',), 'verbose_name': 'Розклад дистанційних уроків', 'verbose_name_plural': 'Розклади дистанційних уроків'},
        ),
    ]
