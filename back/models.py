from django.db import models


# Create your models here.

class Referans(models.Model):
    ref_adi = models.CharField(max_length=300, verbose_name='Referasn adı')
    ref_baslik=models.CharField(max_length=300, verbose_name='Başlık')
    ref_firma=models.CharField(max_length=300, verbose_name='Firma')
    ref_teknoloji=models.CharField(max_length=500, verbose_name='Teknolojiler')
    ref_aciklama=models.TextField(null=True,blank=True, verbose_name='Başlık')
    ref_siteurl = models.CharField(max_length=500, verbose_name='Site url')
    ref_resim=models.ImageField(verbose_name='Resim')
    ref_url = models.CharField(max_length=500, verbose_name='Url')
    ref_seo_baslik = models.CharField(max_length=70, verbose_name='seo başlık', null=True, blank=True)
    ref_seo_keywords = models.TextField(verbose_name='Anahtar kelimeler', null=True, blank=True)
    ref_seo_aciklama = models.TextField(verbose_name='Seo Açıklama', null=True, blank=True)

    def __str__(self):
        if self.ref_adi==None:
            return 'null'
        return 'sss'


    def __unicode__(self):
        return self.ref_adi

class İsler(models.Model):
    ref_adi = models.CharField(max_length=300, verbose_name='Referasn adı')
    ref_baslik = models.CharField(max_length=300, verbose_name='Başlık')
    ref_firma = models.CharField(max_length=300, verbose_name='Firma')
    ref_teknoloji = models.CharField(max_length=500, verbose_name='Teknolojiler')
    ref_aciklama = models.TextField(null=True, blank=True, verbose_name='Başlık')
    ref_siteurl = models.CharField(max_length=500, verbose_name='Site url')
    ref_resim = models.ImageField(verbose_name='Resim')
    ref_url = models.CharField(max_length=500, verbose_name='Url')
    ref_seo_baslik = models.CharField(max_length=70, verbose_name='seo başlık', null=True, blank=True)
    ref_seo_keywords = models.TextField(verbose_name='Anahtar kelimeler', null=True, blank=True)
    ref_seo_aciklama = models.TextField(verbose_name='Seo Açıklama', null=True, blank=True)

    def __str__(self):
        if self.ref_adi == None:
            return 'null'
        return self.ref_adi

    def __unicode__(self):
        return self.ref_adi

class Sayfa(models.Model):
    say_baslik = models.CharField(max_length=300, verbose_name='Başlık')
    say_adi = models.CharField(max_length=300, verbose_name='Referasn adı')
    say_aciklama = models.TextField(null=True, blank=True, verbose_name='Başlık')
    say_resim = models.ImageField(verbose_name='Resim', null=True, blank=True)
    say_url = models.CharField(max_length=500, verbose_name='Url')
    say_seo_baslik = models.CharField(max_length=70, verbose_name='seo başlık', null=True, blank=True)
    say_seo_keywords = models.TextField(verbose_name='Anahtar kelimeler', null=True, blank=True)
    say_seo_aciklama = models.TextField(verbose_name='Seo Açıklama', null=True, blank=True)

    def __str__(self):
        return self.say_adi


class Image(models.Model):
    res_referans=models.ForeignKey('İsler',on_delete=models.CASCADE)
    res_resim=models.ImageField(verbose_name='Resim')
    res_oncelik=models.CharField(max_length=40, verbose_name='Öncelik')

    def __str__(self):
        return 'Resim'




class Blog(models.Model):
    blog_baslik=models.CharField(max_length=300, verbose_name='Başlık')
    blog_altbaslik = models.CharField(max_length=500, verbose_name='Alt Başlık')
    blog_adi=models.CharField(max_length=300, verbose_name='Blog adı')
    blog_giris=models.TextField(null=True,blank=True, verbose_name='Giriş')
    blog_icerik= models.TextField(null=True, blank=True, verbose_name='İçerik')
    blog_resim=models.ImageField(verbose_name='Resim')
    blog_url = models.CharField(max_length=500, verbose_name='Url')
    blog_seo_baslik = models.CharField(max_length=70, verbose_name='seo başlık', null=True, blank=True)
    blog_seo_keywords = models.TextField(verbose_name='Anahtar kelimeler', null=True, blank=True)
    blog_seo_aciklama = models.TextField(verbose_name='Seo Açıklama', null=True, blank=True)

    def __str__(self):
        return self.blog_adi



class Seo(models.Model):
    seo_baslik = models.CharField(max_length=70, verbose_name='seo başlık', null=True, blank=True)
    seo_keywords = models.TextField(verbose_name='Anahtar kelimeler', null=True, blank=True)
    seo_aciklama = models.TextField(verbose_name='Seo Açıklama', null=True, blank=True)

    def __str__(self):
        return 'seo'




class İletisim(models.Model):
    durum=(
        ('okundu','okundu'),
        ('okunmadı','okunmadı')
    )
    ilt_isim=models.CharField(max_length=300, null=True, blank=True, verbose_name='İsim')
    ilt_firma = models.CharField(max_length=300,null=True, blank=True,  verbose_name='Firma')
    ilt_telefon=models.CharField(max_length=300,null=True, blank=True,  verbose_name='Telefon')
    ilt_eposta=models.CharField(max_length=300,null=True, blank=True,  verbose_name='Eposta')
    ilt_turu=models.CharField(max_length=300,null=True, blank=True,  verbose_name='Tür')
    ilt_mesaj=models.TextField(null=True, blank=True, verbose_name='İçerik')
    ilt_durum=models.CharField(max_length=300,choices=durum,null=True, blank=True,verbose_name='durum')

    def __str__(self):
        return self.ilt_isim




