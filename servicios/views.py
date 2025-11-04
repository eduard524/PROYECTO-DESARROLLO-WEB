from django.shortcuts import render
from .models import Servicio

def servicio_list(request):
    servicios = Servicio.objects.all()
    return render(request, "servicios/list.html", {"servicios": servicios})
