# salones/forms.py
from django import forms
from .models import Salon

class SalonForm(forms.ModelForm):
    class Meta:
        model = Salon
        fields = ["nombre", "capacidad", "descripcion", "precio_hora", "disponible"]
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control", "placeholder": "Nombre del salón"}),
            "capacidad": forms.NumberInput(attrs={"class": "form-control", "min": 1}),
            "descripcion": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "precio_hora": forms.NumberInput(attrs={"class": "form-control", "step": "0.01", "min": 0}),
            "disponible": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }
        labels = {
            "nombre": "Nombre",
            "capacidad": "Capacidad",
            "descripcion": "Descripción",
            "precio_hora": "Precio por hora (GTQ)",
            "disponible": "Disponible",
        }
