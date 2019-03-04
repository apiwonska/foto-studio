# Generated by Django 2.1.3 on 2018-11-23 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_auto_20181122_2327'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='staff',
            options={'ordering': ['order'], 'verbose_name': 'pracownik', 'verbose_name_plural': 'pracownicy'},
        ),
        migrations.AddField(
            model_name='staff',
            name='order',
            field=models.PositiveSmallIntegerField(default=1, verbose_name='Kolejność na stronie'),
            preserve_default=False,
        ),
    ]
