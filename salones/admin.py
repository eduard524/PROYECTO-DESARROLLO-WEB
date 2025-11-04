# salones/admin.py
from django.contrib import admin
from .models import Salon, ImagenSalon, FechaBloqueada

@admin.register(Salon)
class SalonAdmin(admin.ModelAdmin):
    list_display  = ("nombre", "capacidad", "precio_hora", "disponible", "creado_en")
    list_filter   = ("disponible",)
    search_fields = ("nombre",)

@admin.register(ImagenSalon)
class ImagenSalonAdmin(admin.ModelAdmin):
    list_display  = ("salon", "orden", "ruta", "creado_en")
    list_filter   = ("salon",)
    search_fields = ("salon__nombre", "ruta")

@admin.register(FechaBloqueada)
class FechaBloqueadaAdmin(admin.ModelAdmin):
    list_display  = ("salon", "fecha", "motivo")
    list_filter   = ("salon",)
    search_fields = ("salon__nombre", "motivo")
