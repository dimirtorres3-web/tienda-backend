from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=200, verbose_name="Nombre del Producto")
    descripcion = models.TextField(verbose_name="Descripción", blank=True)
    precio = models.IntegerField(verbose_name="Precio en Guaraníes")
    imagen = models.ImageField(upload_to='productos/', verbose_name="Foto del Producto", blank=True, null=True)

    def _str_(self):
        return self.nombre