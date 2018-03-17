from django.contrib import admin
from .models import Referans, Sayfa, Image, Blog,Seo, İsler,İletisim


# Register your models here.


class PhotoInline(admin.StackedInline):
    model = Image
    extra =1

class refAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]

class ilt(admin.ModelAdmin):
    list_display=['ilt_isim','ilt_eposta','ilt_telefon','ilt_durum']
    class Meta:
        model=İletisim

admin.site.register(Sayfa)
admin.site.register(Blog)
admin.site.register(Seo)
admin.site.register(İsler, refAdmin)
admin.site.register(İletisim, ilt)