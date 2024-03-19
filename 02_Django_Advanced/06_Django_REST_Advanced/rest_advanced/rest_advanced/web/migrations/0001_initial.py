# Generated by Django 5.0.3 on 2024-03-18 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('pages', models.IntegerField(default=0)),
                ('description', models.TextField(default='', max_length=100)),
                ('author', models.CharField(max_length=20)),
                ('genre', models.CharField(choices=[('Fantasy', 'Fantasy'), ('Sci-Fi', 'Sci Fi')], max_length=7)),
            ],
        ),
    ]