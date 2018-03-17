from back.models import Seo


def servis(request):

    seo=Seo.objects.get(id=1)

    return {
        'seo':seo
    }