from django import forms
from django.forms import ModelForm, NumberInput, TextInput, Textarea

from .models import Registro, Ponente, Conferencia, Lugar

class PonenteModelForm(ModelForm):

	class Meta:
		model = Ponente
		fields = ("titulo", "nombre", "email", "telefono", "resumen", "activo", "intro")

class LugarModelForm(ModelForm):

	class Meta:
		model = Lugar
		fields = '__all__'

class ConferenciaModelForm(ModelForm):

	class Meta:
		model = Conferencia
		labels = {
			'nombre' : 'Titulo',
			'duracion' : 'Duración (Horas)',
			'fecha_hora' : 'Fecha',
			'hora' : 'Hora de Inicio',			
		}
		fields = ("nombre", "ponente", "lugar", "fecha_hora", "hora", "duracion", "foto", "descripcion")

class TallerModelForm(ModelForm):

	class Meta:
		model = Conferencia
		labels = {
			'nombre' : 'Nombre',
			'duracion' : 'Duración (Horas)',
			'fecha_hora' : 'Fecha',
			'hora' : 'Hora de Inicio',		
			'ponente' : 'Instructor'	
		}
		fields = ("nombre", "ponente", "lugar", "fecha_hora", "hora", "duracion", "foto", "descripcion")


class RegistroModelForm(ModelForm):

	# rfc = forms.CharField(required=False)
	# nocontrol = forms.CharField(required=False)

	class Meta:
		model = Registro
		fields = ("tipo_registro", "nombre", "apellidop", "apellidom", "nocontrol", "rfc", "institucion", "carrera", "semestre", "email", "telefono", "municipio", "estado")
		# fields = "__all__" #("precio",)
		# exlude = ("imagen",)
		labels = {
			'nombre' : 'Nombre(s)',
			'apellidop' : 'Apellido Paterno',
			'apellidom' : 'Apellido Materno',
			'nocontrol' : 'No Control',
			'rfc' : 'RFC',
			'telefono' : 'Teléfono (con Clave Lada)',
			'institucion' : 'Empresa / Institución',

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
		self.fields['telefono'].required = False