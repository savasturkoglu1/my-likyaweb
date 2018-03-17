# Generated by Django 2.0.1 on 2018-02-24 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0003_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_baslik', models.CharField(max_length=300, verbose_name='Başlık')),
                ('blog_altbaslik', models.CharField(max_length=500, verbose_name='Alt Başlık')),
                ('blog_adi', models.CharField(max_length=300, verbose_name='Referasn adı')),
                ('blog_aciklama', models.TextField(blank=True, null=True, verbose_name='Başlık')),
                ('blog_resim', models.ImageField(upload_to='', verbose_name='Resim')),
                ('blog_url', models.CharField(max_length=500, verbose_name='Url')),
                ('blog_seo_baslik', models.CharField(blank=True, max_length=70, null=True, verbose_name='seo başlık')),
                ('blog_seo_keywords', models.TextField(blank=True, null=True, verbose_name='Anahtar kelimeler')),
                ('blog_seo_aciklama', models.TextField(blank=True, null=True, verbose_name='Seo Açıklama')),
            ],
        ),
    ]
