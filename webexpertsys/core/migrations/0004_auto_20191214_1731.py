# Generated by Django 2.2.7 on 2019-12-14 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20191214_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='number',
            field=models.IntegerField(null=True, unique=True, verbose_name='Приоритет'),
        ),
    ]
