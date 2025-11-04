# reservas/views.py
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Reserva


class ReservaList(ListView):
    model = Reserva
    template_name = "reservas/list.html"
    context_object_name = "reservas"


class ReservaCreate(CreateView):
    model = Reserva
    fields = ["salon", "cliente", "fecha_evento", "hora_inicio", "hora_fin", "estado", "notas", "total"]
    template_name = "reservas/form.html"
    success_url = reverse_lazy("reservas:list")


class ReservaUpdate(UpdateView):
    model = Reserva
    fields = ["salon", "cliente", "fecha_evento", "hora_inicio", "hora_fin", "estado", "notas", "total"]
    template_name = "reservas/form.html"
    success_url = reverse_lazy("reservas:list")


class ReservaDelete(DeleteView):
    model = Reserva
    template_name = "reservas/confirm_delete.html"
    success_url = reverse_lazy("reservas:list")
