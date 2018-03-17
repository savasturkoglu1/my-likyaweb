from back.models import İletisim
from django import forms

class iForm(forms.ModelForm):

    class Meta:
        model=İletisim

        fields=[
            'ilt_isim',
            'ilt_telefon',
            'ilt_eposta',
            'ilt_firma',
            'ilt_mesaj',
            'ilt_turu'
        ]