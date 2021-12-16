# Generated by Django 2.1.3 on 2021-12-16 19:26

from django.db import migrations, models
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FotoPortrait',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True, verbose_name='tytuł')),
                ('author', models.CharField(blank=True, max_length=100, null=True, verbose_name='autor')),
                ('order', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='kolejność na stronie')),
                ('image', imagekit.models.fields.ProcessedImageField(upload_to='img/services/portrait/', verbose_name='zdjęcie')),
            ],
            options={
                'verbose_name': 'galeria - Fotografia Portretowa',
                'verbose_name_plural': 'galeria - Fotografia Portretowa',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='FotoStudio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True, verbose_name='tytuł')),
                ('author', models.CharField(blank=True, max_length=100, null=True, verbose_name='autor')),
                ('order', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='kolejność na stronie')),
                ('image', imagekit.models.fields.ProcessedImageField(upload_to='img/services/studio/', verbose_name='zdjęcie')),
            ],
            options={
                'verbose_name': 'galeria - Studio',
                'verbose_name_plural': 'galeria - Studio',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='FotoWedding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True, verbose_name='tytuł')),
                ('author', models.CharField(blank=True, max_length=100, null=True, verbose_name='autor')),
                ('order', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='kolejność na stronie')),
                ('image', imagekit.models.fields.ProcessedImageField(upload_to='img/services/wedding/', verbose_name='zdjęcie')),
            ],
            options={
                'verbose_name': 'galeria - Fotografia Weselna',
                'verbose_name_plural': 'galeria - Fotografia Weselna',
                'ordering': ['order'],
            },
        ),
    ]
