from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ["nombres", "apellidos", "telefono", "email", "nit"]
        widgets = {
            "nombres":  forms.TextInput(attrs={"class": "form-control"}),
            "apellidos":forms.TextInput(attrs={"class": "form-control"}),
            "telefono": forms.TextInput(attrs={"class": "form-control"}),
            "email":    forms.EmailInput(attrs={"class": "form-control"}),
            "nit":      forms.TextInput(attrs={"class": "form-control"}),
        }
