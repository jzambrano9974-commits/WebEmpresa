from .models import Redsocial

def redes_sociales(request):
    # Traemos todos los registros tal cual están en la BD
    redes = Redsocial.objects.all()
    return {'redes': redes}