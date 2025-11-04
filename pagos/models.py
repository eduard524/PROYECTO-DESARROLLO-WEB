# pagos/models.py
from django.db import models

class MetodoPago(models.Model):
    nombre = models.CharField(max_length=60)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class Pago(models.Model):
    ESTADOS = [('aprobado','Aprobado'), ('pendiente','Pendiente'), ('rechazado','Rechazado')]
    reserva = models.ForeignKey('reservas.Reserva', on_delete=models.CASCADE, related_name='pagos')
    metodo = models.ForeignKey(MetodoPago, on_delete=models.PROTECT)
    monto = models.DecimalField(max_digits=12, decimal_places=2)
    moneda = models.CharField(max_length=10, default='GTQ')
    referencia_txn = models.CharField(max_length=120, blank=True, null=True)
    estado = models.CharField(max_length=10, choices=ESTADOS, default='aprobado')
    fecha_pago = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pago {self.id} R{self.reserva_id} - {self.monto} {self.moneda}"
