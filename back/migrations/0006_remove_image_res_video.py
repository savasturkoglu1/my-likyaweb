# Generated by Django 2.0.1 on 2018-02-25 15:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0005_seo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='res_video',
        ),
    ]