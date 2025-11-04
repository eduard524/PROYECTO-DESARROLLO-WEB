from django.db import models
from django.core.validators import MinValueValidator


class Servicio(models.Model):
    TIPOS = (
        ("silla", "Silla"),
        ("mesa", "Mesa"),
        ("sonido", "Sonido"),
        ("adorno", "Adorno"),
        ("combo", "Combo"),
        ("otro", "Otro"),
    )

    nombre = models.CharField(max_length=120, db_index=True)
    descripcion = models.TextField(blank=True, null=True)
    tipo = models.CharField(max_length=20, choices=TIPOS, default="otro")
    precio_unitario = models.DecimalField(
        max_digits=12, decimal_places=2,
        validators=[MinValueValidator(0)], default=0
    )
    activo = models.BooleanField(default=True, db_index=True)
    creado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("nombre",)
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"
        indexes = [
            models.Index(fields=["nombre"]),
            models.Index(fields=["tipo"]),
            models.Index(fields=["activo"]),
        ]

    def __str__(self):
        return f"{self.nombre} - {self.tipo} (GTQ {self.precio_unitario})"
