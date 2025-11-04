from django.db import models
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError

from salones.models import Salon
from clientes.models import Cliente
from servicios.models import Servicio


class Reserva(models.Model):
    ESTADOS = (
        ("pendiente", "Pendiente"),
        ("confirmada", "Confirmada"),
        ("pagada", "Pagada"),
        ("cancelada", "Cancelada"),
    )

    salon        = models.ForeignKey(Salon, on_delete=models.PROTECT, related_name="reservas")
    cliente      = models.ForeignKey(Cliente, on_delete=models.PROTECT, related_name="reservas")
    fecha_evento = models.DateField()
    hora_inicio  = models.TimeField()
    hora_fin     = models.TimeField()
    estado       = models.CharField(max_length=20, choices=ESTADOS, default="pendiente", db_index=True)
    total        = models.DecimalField(max_digits=12, decimal_places=2, validators=[MinValueValidator(0)], default=0)
    notas        = models.CharField(max_length=300, blank=True)
    creado_en    = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-fecha_evento", "-creado_en")
        verbose_name = "Reserva"
        verbose_name_plural = "Reservas"
        indexes = [
            models.Index(fields=["fecha_evento"]),
            models.Index(fields=["estado"]),
        ]

    def clean(self):
      
        if self.hora_fin and self.hora_inicio and self.hora_fin <= self.hora_inicio:
            raise ValidationError("La hora de fin debe ser mayor que la hora de inicio.")

    def __str__(self):
        return f"Reserva #{self.pk or ''} - {self.salon.nombre} - {self.fecha_evento}"


class ReservaServicio(models.Model):
    reserva         = models.ForeignKey(Reserva, on_delete=models.CASCADE, related_name="items")
    servicio        = models.ForeignKey(Servicio, on_delete=models.PROTECT, related_name="reservas_items")
    cantidad        = models.PositiveIntegerField(validators=[MinValueValidator(1)], default=1)
    precio_unitario = models.DecimalField(max_digits=12, decimal_places=2, validators=[MinValueValidator(0)])
    subtotal        = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        verbose_name = "Servicio en reserva"
        verbose_name_plural = "Servicios en reserva"
        unique_together = (("reserva", "servicio"),)

    def save(self, *args, **kwargs):
        # Calcula subtotal si no viene seteado
        if self.cantidad is not None and self.precio_unitario is not None:
            self.subtotal = self.cantidad * self.precio_unitario
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.servicio.nombre} x{self.cantidad} (Reserva #{self.reserva_id})"
