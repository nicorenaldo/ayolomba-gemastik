# Generated by Django 3.0.8 on 2020-09-07 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0015_auto_20200907_1955'),
    ]

    operations = [
        migrations.AddField(
            model_name='lomba',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
