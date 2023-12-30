# Generated by Django 5.0 on 2023-12-30 09:11

import petstagram.photos.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_alter_photo_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(upload_to='photos/', validators=[petstagram.photos.validators.validate_file_size]),
        ),
    ]
