# Generated by Django 2.0.1 on 2018-03-07 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0010_i̇letisim'),
    ]

    operations = [
        migrations.AlterField(
            model_name='i̇letisim',
            name='ilt_durum',
            field=models.CharField(blank=True, choices=[('okundu', 'okundu'), ('okunmadı', 'okunmadı')], max_length=300, null=True, verbose_name='durum'),
        ),
    ]
