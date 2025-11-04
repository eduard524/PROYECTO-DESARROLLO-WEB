from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Cliente
from .forms import ClienteForm

class ClienteList(ListView):
    model = Cliente
    template_name = "clientes/list.html"
    context_object_name = "clientes"

class ClienteCreate(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = "clientes/form.html"
    success_url = reverse_lazy("clientes:list")

class ClienteUpdate(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = "clientes/form.html"
    success_url = reverse_lazy("clientes:list")

class ClienteDelete(DeleteView):
    model = Cliente
    template_name = "clientes/confirm_delete.html"
    success_url = reverse_lazy("clientes:list")
