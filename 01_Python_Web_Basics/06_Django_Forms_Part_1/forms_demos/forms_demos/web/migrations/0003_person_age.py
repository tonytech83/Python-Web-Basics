# Generated by Django 5.0 on 2023-12-28 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_pet_person_pets'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='age',
            field=models.PositiveIntegerField(default=21),
            preserve_default=False,
        ),
    ]
