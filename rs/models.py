from django.db import models

class Redsocial(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    link = models.URLField(max_length=200, verbose_name="Enlace")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "Red social"
        verbose_name_plural = "Redes sociales"

    def __str__(self):
        return self.name