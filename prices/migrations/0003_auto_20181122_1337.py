# Generated by Django 2.1.3 on 2018-11-22 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prices', '0002_auto_20181122_1335'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='price',
            name='table_id',
        ),
        migrations.AlterField(
            model_name='price_table',
            name='order',
            field=models.PositiveSmallIntegerField(null=True, verbose_name='Kolejność na stronie'),
        ),
        migrations.DeleteModel(
            name='Price',
        ),
    ]
