from django import forms
from .models import Reserva

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ["salon", "cliente", "fecha_evento", "hora_inicio", "hora_fin", "total", "estado"]
        widgets = {
            "salon":       forms.Select(attrs={"class": "form-select"}),
            "cliente":     forms.Select(attrs={"class": "form-select"}),
            "fecha_evento":forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "hora_inicio": forms.TimeInput(attrs={"class": "form-control", "type": "time"}),
            "hora_fin":    forms.TimeInput(attrs={"class": "form-control", "type": "time"}),
            "total":       forms.NumberInput(attrs={"class": "form-control", "step": "0.01"}),
            "estado":      forms.TextInput(attrs={"class": "form-control"}),
        }

    def clean(self):
        cleaned = super().clean()
        hi = cleaned.get("hora_inicio")
        hf = cleaned.get("hora_fin")
        if hi and hf and hf <= hi:
            self.add_error("hora_fin", "La hora de fin debe ser mayor que la hora de inicio.")
        return cleaned
