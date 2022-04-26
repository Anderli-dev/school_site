# Generated by Django 3.1.7 on 2022-04-26 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_remove_employees_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='employees',
            name='order',
            field=models.PositiveIntegerField(db_index=True, default=1, editable=False, verbose_name='order'),
            preserve_default=False,
        ),
    ]
