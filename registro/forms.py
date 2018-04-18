from django import forms
from django.forms import ModelForm, NumberInput, TextInput, Textarea

from .models import Registro, Ponente, Conferencia, Lugar

class PonenteModelForm(ModelForm):

	class Meta:
		model = Ponente
		fields = '__all__'

class LugarModelForm(ModelForm):

	class Meta:
		model = Lugar
		fields = '__all__'

class ConferenciaModelForm(ModelForm):

	class Meta:
		model = Conferencia
		fields = '__all__'

class RegistroModelForm(ModelForm):

	# rfc = forms.CharField(required=False)
	# nocontrol = forms.CharField(required=False)

	class Meta:
		model = Registro
		fields = ("tipo_registro", "nombre", "apellidop", "apellidom", "nocontrol", "rfc", "carrera", "semestre", "email", "municipio", "estado")
		# fields = "__all__" #("precio",)
		# exlude = ("imagen",)
		labels = {
			'nombre' : 'Nombre(s)',
			'apellidop' : 'Apellido Paterno',
			'apellidom' : 'Apellido Materno',
			'nocontrol' : 'No Control',
			'rfc' : 'Rfc',
		}
		widgets = {
			# 'descripcion' : Textarea(attrs={'cols':80, 'rows':5}),
			# 'precio': NumberInput(attrs={'min': 0}), 
			# 'cantidad': NumberInput(attrs={'min': 0}),            
		}

	def __init__(self, *args, **kwargs):
		super(RegistroModelForm, self).__init__(*args, **kwargs)
		self.fields['rfc'].required = False
		self.fields['nocontrol'].required = False