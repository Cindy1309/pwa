from django.db import models

class Subscriber(models.Model):

    nombre = models.CharField(max_length=100)

    correo = models.EmailField(unique=True)

    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre


class Visitor(models.Model):

    ip = models.GenericIPAddressField()

    user_agent = models.TextField()

    fecha_visita = models.DateTimeField(auto_now_add=True)

    def __str__(self):
         return self.ip