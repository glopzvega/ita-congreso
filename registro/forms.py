from django import forms
from django.forms import ModelForm, NumberInput, TextInput, Textarea

from .models import Registro, Ponente, Conferencia, Lugar, Horario, Taller

class PonenteModelForm(ModelForm):

	class Meta:
		model = Ponente
		labels = {
			'horario' : 'Lugar y Fecha',					
		}
		fields = ("ponencia", "horario", "titulo", "nombre", "email", "telefono", "resumen", "activo", "intro")

class LugarModelForm(ModelForm):

	class Meta:
		model = Lugar
		fields = '__all__'

class HorarioModelForm(ModelForm):

	class Meta:
		model = Horario
		fields = '__all__'

class ConferenciaModelForm(ModelForm):

	class Meta:
		model = Conferencia
		labels = {
			'nombre' : 'Titulo',
			'duracion' : 'Duración (Horas)',
			'fecha_hora' : 'Fecha',
			'hora' : 'Hora de Inicio',
			'hora_fin' : 'Hora de Término',			
		}
		fields = ("nombre", "ponente", "lugar", "horario", "fecha_hora", "hora", "hora_fin", "foto", "descripcion")

	def __init__(self, *args, **kwargs):
		super(ConferenciaModelForm, self).__init__(*args, **kwargs)
		self.fields['ponente'].queryset = Ponente.objects.filter(tipo__exact="ponente")

class TallerModelForm(ModelForm):

	class Meta:
		model = Taller
		labels = {
			'nombre' : 'Nombre del Taller',			
			'fecha' : 'Fecha de Inicio',
			'duracion' : 'Duración (Dias)',
			'hora' : 'Hora de Inicio',
			'hora_fin' : 'Hora de Termino',
			'profesor' : 'Instructor',
			'requisitos' : 'Requisitos del Participante',
			'descripcion' : 'Programa'
		}
		fields = ("nombre", "profesor", "salon", "fecha", "duracion", "hora", "hora_fin",  "requisitos", "foto", "objetivo", "descripcion")
	# def __init__(self, *args, **kwargs):
	# 	super(TallerModelForm, self).__init__(*args, **kwargs)
	# 	self.fields['ponente'].queryset = Ponente.objects.filter(tipo__exact="profesor")

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
			'nocontrol' : 'Matrícula o No. de Control',
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