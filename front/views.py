from django.shortcuts import render, HttpResponse
from back.models import Referans, İsler,Image,Seo,Blog
from .forms import iForm
# Create your views here.


def index(request):
    seo=Seo.objects.get(id=1)
    ref=İsler.objects.all()
    context={
        'ref':ref,
        'seo':seo
    }
    return render(request, 'front/index.html',context)


def referans(request, url):
    ref=İsler.objects.get(ref_url=url)
    res=Image.objects.filter(res_referans_id=ref.id)
    context={
        'ref':ref,
        'res':res
    }
    return render(request, 'front/referans.html', context)

def hiz(request):
    return render(request,'front/hizmetlerimiz.html')


def hak(request):
    return render(request,'front/hakkımızda.html')

def blog(request):
    blog=Blog.objects.all()
    return render(request ,'front/blogs.html',{'blog':blog})


def yazı(request , url):
    yazı=Blog.objects.get(blog_url=url)
    blog = Blog.objects.all().order_by('id')[:10]
    context={
        'yazi':yazı,
        'blog':blog
    }
    return render(request ,'front/yazı.html',context)
def iletisim(request):
    return render(request,'front/iletisim.html')


def yenimesaj(request):
    frm=iForm(request.POST)

    if frm.is_valid():
        kayit=frm.save()
        if(kayit):
            return HttpResponse('oldu')
        else:
            return HttpResponse('hata')

def refs(request):
    ref=İsler.objects.all()
    context={
        'ref':ref
    }

    return render(request, 'front/referanslar.html',context)