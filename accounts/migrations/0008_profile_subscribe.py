# Generated by Django 3.0.8 on 2020-09-09 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0018_auto_20200909_2112'),
        ('accounts', '0007_auto_20200901_2247'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='subscribe',
            field=models.ManyToManyField(to='competitions.Kategori'),
        ),
    ]
