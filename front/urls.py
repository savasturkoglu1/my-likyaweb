from django.urls import path
from django.conf.urls import url

from . import views



urlpatterns =[
    path('',views.index),
    url(r'^referans/(?P<url>[\w\-]+)/', views.referans),
    url(r'^referaslarımız',views.refs),
    url(r'^hizmetlerimiz', views.hiz),
    url(r'^hakkımızda', views.hak),
    url(r'^blog', views.blog),
    url(r'^iletisim', views.iletisim),
    url(r'^yenimesaj', views.yenimesaj),
    url(r'^yazı/(?P<url>[\w\-]+)/', views.yazı),


]