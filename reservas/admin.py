from django.contrib import admin
from .models import Reserva, ReservaServicio


class ReservaServicioInline(admin.TabularInline):
    model = ReservaServicio
    extra = 1
    fields = ("servicio", "cantidad", "precio_unitario", "subtotal")
    readonly_fields = ("subtotal",)


@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ("id", "salon", "cliente", "fecha_evento", "hora_inicio", "hora_fin", "estado", "total")
    list_filter = ("estado", "salon")
    search_fields = ("cliente__nombres", "cliente__apellidos", "salon__nombre")
    date_hierarchy = "fecha_evento"
    inlines = [ReservaServicioInline]


@admin.register(ReservaServicio)
class ReservaServicioAdmin(admin.ModelAdmin):
    list_display = ("reserva", "servicio", "cantidad", "precio_unitario", "subtotal")
    list_filter = ("servicio",)
    search_fields = ("reserva__id", "servicio__nombre")
