from .models import link

def ctx_dict (request):
    ctx = {}
    links = link.objects.all()
    for Link in links:
        ctx[Link.key] = Link.url
    return ctx