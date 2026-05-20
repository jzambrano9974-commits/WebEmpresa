from django.contrib import admin
from django.urls import path, include  # <-- ¡Añadimos 'include' aquí!
from django.conf.urls.static import static
from django.conf import settings
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Rutas que se quedan en la app principal 'core'
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('store/', views.store, name='store'),

    # --- APLICAMOS EL REQUISITO DEL PROFESOR (INCLUDE) ---
    path('blog/', include('blog.urls')),
    path('services/', include('services.urls')),
    path('rs/', include('rs.urls')),
]

# Configuración para poder ver las imágenes en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)