# Generated by Django 2.1.3 on 2019-07-19 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_auto_20190718_2352'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='GalleryPortrait',
            new_name='FotoPortrait',
        ),
        migrations.RenameModel(
            old_name='GalleryStudio',
            new_name='FotoStudio',
        ),
        migrations.RenameModel(
            old_name='GalleryWeddings',
            new_name='FotoWedding',
        ),
    ]
