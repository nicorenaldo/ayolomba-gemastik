# Generated by Django 3.0.8 on 2020-08-25 14:10

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('competitions', '0007_lomba_tanggalpelaksanaan'),
    ]

    operations = [
        migrations.AddField(
            model_name='lomba',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AlterField(
            model_name='lomba',
            name='deadline',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='lomba',
            name='tanggalpelaksanaan',
            field=models.DateTimeField(),
        ),
    ]
