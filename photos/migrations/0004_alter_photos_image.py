# Generated by Django 3.2.5 on 2021-10-12 05:03

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0003_auto_20211012_0534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photos',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]