# salones/views.py
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Salon
from .forms import SalonForm

class SalonList(ListView):
    model = Salon
    template_name = "salones/list.html"
    context_object_name = "salones"

class SalonCreate(CreateView):
    model = Salon
    form_class = SalonForm
    template_name = "salones/form.html"
    success_url = reverse_lazy("salones:list")

class SalonUpdate(UpdateView):
    model = Salon
    form_class = SalonForm
    template_name = "salones/form.html"
    success_url = reverse_lazy("salones:list")

class SalonDelete(DeleteView):
    model = Salon
    template_name = "salones/confirm_delete.html"
    success_url = reverse_lazy("salones:list")
