from django.db import models
from django.core.validators import MinValueValidator

class Salon(models.Model):
    nombre      = models.CharField(max_length=120, db_index=True)
    capacidad   = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    descripcion = models.TextField(blank=True, null=True)
    precio_hora = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    disponible  = models.BooleanField(default=True, db_index=True)
    creado_en   = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("nombre",)

    def __str__(self):
        return f"{self.nombre} (Capacidad: {self.capacidad})"


class ImagenSalon(models.Model):
    salon     = models.ForeignKey(Salon, on_delete=models.CASCADE, related_name="imagenes")
    ruta      = models.CharField(max_length=255)
    alt_text  = models.CharField(max_length=200, blank=True)
    orden     = models.PositiveIntegerField(default=1)
    creado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("salon", "orden")
    
        unique_together = (("salon", "orden"),)

    def __str__(self):
        return f"{self.salon.nombre} - #{self.orden}"


class FechaBloqueada(models.Model):
    salon  = models.ForeignKey(Salon, on_delete=models.CASCADE, related_name="fechas_bloqueadas")
    fecha  = models.DateField()
    motivo = models.CharField(max_length=200, blank=True)

    class Meta:
        ordering = ("-fecha",)
        unique_together = (("salon", "fecha"),)
        verbose_name = "Fecha bloqueada"
        verbose_name_plural = "Fechas bloqueadas"

    def __str__(self):
        return f"{self.salon.nombre} - {self.fecha}"
