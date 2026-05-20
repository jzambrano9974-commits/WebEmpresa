from .models import Redsocial

def redes_sociales(request):
    redes = Redsocial.objects.all()
    return {'redes': redes}