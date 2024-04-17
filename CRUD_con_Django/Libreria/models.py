from typing import Any
from django.db import models


# Modelo Books.
class Books(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, null=False, verbose_name='Título')
    description = models.TextField(null=False, verbose_name='Descripción')
    image = models.ImageField(upload_to='images/', null=True, verbose_name='Imagen')


    def __str__(self):
        return (f"Id: {self.id}. Título: {self.title}")


    # Borrar la imagen del storage usando como parametro el nombre
    # de la imagen. Esto acción se ejecutará tanto al borrar ul libro desde
    # la consola de administrador como cuando se haga uso en el CRUD.
    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()