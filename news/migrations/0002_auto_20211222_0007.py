# Generated by Django 2.2.24 on 2021-12-21 23:07

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='img/news', verbose_name='zdjęcie'),
        ),
    ]
