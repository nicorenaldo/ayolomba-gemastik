# Generated by Django 3.0.8 on 2020-09-01 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0010_auto_20200901_2247'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lomba',
            name='description2',
        ),
    ]
