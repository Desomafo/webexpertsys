# Generated by Django 2.2.7 on 2019-12-14 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20191214_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='number',
            field=models.IntegerField(null=True, verbose_name='Приоритет'),
        ),
    ]