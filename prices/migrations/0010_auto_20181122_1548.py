# Generated by Django 2.1.3 on 2018-11-22 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prices', '0009_auto_20181122_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='service_details',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Szczegóły'),
        ),
    ]
