# Generated by Django 3.2.5 on 2021-10-12 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_auto_20211012_0527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photos',
            name='image_location',
            field=models.CharField(default='Location_image_was_taken', max_length=50),
        ),
        migrations.AlterField(
            model_name='photos',
            name='image_name',
            field=models.CharField(default='Name_of_image', max_length=100),
        ),
    ]
