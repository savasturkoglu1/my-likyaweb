# Generated by Django 2.0.1 on 2018-03-06 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0008_auto_20180304_1910'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='blog_aciklama',
        ),
        migrations.AddField(
            model_name='blog',
            name='blog_giris',
            field=models.TextField(blank=True, null=True, verbose_name='Giriş'),
        ),
        migrations.AddField(
            model_name='blog',
            name='blog_icerik',
            field=models.TextField(blank=True, null=True, verbose_name='İçerik'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='blog_adi',
            field=models.CharField(max_length=300, verbose_name='Blog adı'),
        ),
    ]
