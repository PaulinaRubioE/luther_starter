from django import forms
from .models import Contacto

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre','apellido','email','telefono','mensaje']
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}),
            'apellido': forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}),
            'email': forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Email'}),
            'telefono': forms.TextInput(attrs={'class':'form-control','placeholder':'Phone (optional)'}),
            'mensaje': forms.Textarea(attrs={'class':'form-control','rows':4,'placeholder':'Escribe tu mensaje...'}),
        }