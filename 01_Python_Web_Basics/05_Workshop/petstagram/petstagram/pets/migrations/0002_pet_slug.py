# Generated by Django 5.0 on 2023-12-16 08:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('pets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='slug',
            field=models.SlugField(default='none', unique=True),
            preserve_default=False,
        ),
    ]
