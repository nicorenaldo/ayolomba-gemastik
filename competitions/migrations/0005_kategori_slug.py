# Generated by Django 3.0.8 on 2020-07-26 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0004_lomba_inactive'),
    ]

    operations = [
        migrations.AddField(
            model_name='kategori',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
