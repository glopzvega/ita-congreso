from django import forms
from django.forms import ModelForm, NumberInput, TextInput, Textarea

from .models import Registro

class RegistroModelForm(ModelForm):

	rfc = forms.CharField(required=False)
	nocontrol = forms.CharField(required=False)

	class Meta:
		model = Registro
		fields = ("tipo_registro", "nombre", "apellidop", "apellidom", "nocontrol", "rfc", "email", "municipio", "estado")
		# fields = "__all__" #("precio",)
		# exlude = ("imagen",)
		widgets = {
			# 'descripcion' : Textarea(attrs={'cols':80, 'rows':5}),
            # 'precio': NumberInput(attrs={'min': 0}), 
            # 'cantidad': NumberInput(attrs={'min': 0}),            
        }