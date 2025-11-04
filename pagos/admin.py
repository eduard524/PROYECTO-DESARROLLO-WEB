from django.contrib import admin
from .models import MetodoPago, Pago

@admin.register(MetodoPago)
class MetodoPagoAdmin(admin.ModelAdmin):
    list_display = ("nombre","activo")
    list_filter = ("activo",)

@admin.register(Pago)
class PagoAdmin(admin.ModelAdmin):
    list_display = ("id","reserva","metodo","monto","moneda","estado","fecha_pago")
    list_filter = ("estado","metodo")
    search_fields = ("reserva__cliente__nombres","reserva__cliente__apellidos","referencia_txn")
