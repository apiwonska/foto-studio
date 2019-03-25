# Generated by Django 2.1.3 on 2018-11-22 23:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GalleryPortrait',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True, verbose_name='Tytuł')),
                ('author', models.CharField(blank=True, max_length=100, null=True, verbose_name='Autor')),
                ('order', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Kolejność na stronie')),
                ('image', models.ImageField(upload_to='images/portraits/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'gif'])], verbose_name='Plik')),
            ],
            options={
                'verbose_name': 'Galeria - Fotografia Portretowa',
                'verbose_name_plural': 'Galeria - Fotografia Portretowa',
            },
        ),
        migrations.CreateModel(
            name='GalleryStudio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True, verbose_name='Tytuł')),
                ('author', models.CharField(blank=True, max_length=100, null=True, verbose_name='Autor')),
                ('order', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Kolejność na stronie')),
                ('image', models.ImageField(upload_to='images/studio/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'gif'])], verbose_name='Plik')),
            ],
            options={
                'verbose_name': 'Galeria - Studio',
                'verbose_name_plural': 'Galeria - Studio',
            },
        ),
        migrations.CreateModel(
            name='GalleryWeddings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True, verbose_name='Tytuł')),
                ('author', models.CharField(blank=True, max_length=100, null=True, verbose_name='Autor')),
                ('order', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Kolejność na stronie')),
                ('image', models.ImageField(upload_to='images/weddings/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'gif'])], verbose_name='Plik')),
            ],
            options={
                'verbose_name': 'Galeria - Fotografia Weselna',
                'verbose_name_plural': 'Galeria - Fotografia Weselna',
            },
        ),
    ]