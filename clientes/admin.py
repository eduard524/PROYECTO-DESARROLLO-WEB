from django.contrib import admin
from .models import Cliente

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombres', 'apellidos', 'email', 'telefono', 'nit')
    search_fields = ('nombres', 'apellidos', 'email', 'nit')
