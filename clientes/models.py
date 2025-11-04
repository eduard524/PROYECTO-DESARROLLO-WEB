from django.db import models

class Cliente(models.Model):
    nombres   = models.CharField(max_length=120)
    apellidos = models.CharField(max_length=120)
    telefono  = models.CharField(max_length=30, blank=True, null=True)
    email     = models.EmailField(unique=True, blank=True, null=True)
    nit       = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        ordering = ("apellidos", "nombres")

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"
