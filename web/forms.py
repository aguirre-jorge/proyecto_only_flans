from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Flan

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for campo in self.fields.values():
            campo.widget.attrs["class"] = "form-control"

class FlanForm(forms.ModelForm):
    class Meta:
        model = Flan
        fields = ["nombre", "descripcion", "precio", "descuento_inscrito", "imagen", "destacado"]
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "descripcion": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
            "precio": forms.NumberInput(attrs={"class": "form-control", "min": 0}),
            "descuento_inscrito": forms.NumberInput(attrs={"class": "form-control", "min": 0, "max": 100, "step": "0.01"}),
            "imagen": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "destacado": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }