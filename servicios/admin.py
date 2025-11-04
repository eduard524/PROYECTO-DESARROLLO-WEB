from django.contrib import admin
from .models import Servicio


@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ("nombre", "tipo", "precio_unitario", "activo", "creado_en")
    list_filter = ("tipo", "activo")
    search_fields = ("nombre", "descripcion")
    ordering = ("nombre",)
