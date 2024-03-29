# Generated by Django 2.1.3 on 2021-12-16 19:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(max_length=200, verbose_name='usługa')),
                ('service_details', models.CharField(blank=True, max_length=200, null=True, verbose_name='szczegóły')),
                ('price', models.CharField(max_length=20, verbose_name='cena')),
                ('order', models.PositiveSmallIntegerField(verbose_name='kolejność ceny w tabeli')),
            ],
            options={
                'verbose_name': 'cena',
                'verbose_name_plural': 'ceny',
                'ordering': ['price_list', 'order'],
            },
        ),
        migrations.CreateModel(
            name='PriceList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_price_list', models.CharField(max_length=100, verbose_name='nazwa cennika')),
                ('order', models.PositiveSmallIntegerField(verbose_name='kolejność tabel')),
            ],
            options={
                'verbose_name': 'cennik - kategoria',
                'verbose_name_plural': 'cenniki - kategorie',
                'ordering': ['order'],
            },
        ),
        migrations.AddField(
            model_name='price',
            name='price_list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prices.PriceList', verbose_name='cennik'),
        ),
    ]
