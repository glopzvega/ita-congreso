from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Ponente(models.Model):

	TIPOS = [
		("ponente", "Ponente"),
		("profesor", "Profesor"),
	]
	nombre = models.CharField(max_length=255)
	email = models.EmailField(max_length=255)
	telefono = models.CharField(max_length=20)
	titulo = models.CharField(max_length=50)
	resumen = models.CharField(max_length=255)
	intro = models.TextField()
	foto = models.ImageField(blank=True)
	activo = models.BooleanField()
	tipo = models.CharField(max_length=255, choices=TIPOS, default="ponente")

	def __str__(self):
		return self.titulo + " " + self.nombre

class Lugar(models.Model):
	nombre = models.CharField(max_length=255)

	def __str__(self):
		return self.nombre

class Horario(models.Model):
	
	lugar = models.ForeignKey(Lugar, on_delete=models.CASCADE)
	sala = models.CharField(max_length=255)
	fecha = models.DateField()
	hora = models.TimeField()
	hora_fin = models.TimeField()

	def __str__(self):
		return self.sala + " " + str(self.fecha) + " " + str(self.hora) + " - " + str(self.hora_fin)

class Conferencia(models.Model):

	CARRERAS = [
		("arquitectura", "Arquitectura"),
		("bioquimica", "Ingeniería Bioquímica"),
		("electromecanica", "Ingeniería Electromecánica"),
		("sistemas", "Ingeniería en Sistemas Computacionales"),
		("gestion", "Ingenieria en Gestión Empresarial"),
		("administracion", "Licenciatura en Administración"),
		("contabilidad", "Contador Público"),
	]

	fecha_registro = models.DateField(auto_now_add=True)
	fecha_modificacion = models.DateField(auto_now=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	nombre = models.CharField(max_length=255)	
	requisitos = models.CharField(max_length=255, blank=True, null=True)
	objetivo = models.TextField()
	descripcion = models.TextField()
	ponente = models.ForeignKey(Ponente, models.CASCADE, null=True)
	lugar = models.ForeignKey(Lugar, models.CASCADE, null=True)
	sala = models.CharField(max_length=255, null=True)
	fecha_hora = models.DateField()	
	duracion = models.IntegerField()
	fecha_fin = models.DateField()
	hora = models.TimeField()	
	hora_fin = models.TimeField()
	carrera = models.CharField(max_length=255, choices=CARRERAS)	
	foto = models.ImageField(blank=True, null=True)
	tipo = models.CharField(max_length=20, choices=[("conferencia", "Conferencia"), ("taller", "Taller")])	
	horario = models.ForeignKey(Horario, on_delete=models.SET_NULL, null=True)

	def __str__(self):
		return self.nombre

class Registro(models.Model):

	TIPO_REGISTRO = [
		('alumno', 'Alumno del ITA'),
		('exalumno', 'Exalumno del ITA'),
		('alumno2', 'Alumno de otra institución'),
		('profesional', 'Profesionista')
	]

	ESTADOS = [
		("AGU","Aguascalientes"),
		("BCN","Baja California"),
		("BCS","Baja California Sur"),
		("CAM","Campeche"),
		("CHH","Chihuahua"),
		("CHP","Chiapas"),
		("COA","Coahuila"),
		("COL","Colima"),
		("DIF","Ciudad de México"),
		("DUR","Durango"),
		("GRO","Guerrero"),
		("GUA","Guanajuato"),
		("HID","Hidalgo"),
		("JAL","Jalisco"),
		("MEX","México"),
		("MIC","Michoacán"),
		("MOR","Morelos"),
		("NAY","Nayarit"),
		("NLE","Nuevo León"),
		("OAX","Oaxaca"),
		("PUE","Puebla"),
		("QUE","Querétaro"),
		("ROO","Quintana Roo"),
		("SIN","Sinaloa"),
		("SLP","San Luis Potosí"),
		("SON","Sonora"),
		("TAB","Tabasco"),
		("TAM","Tamaulipas"),
		("TLA","Tlaxcala"),
		("VER","Veracruz"),
		("YUC","Yucatán"),
		("ZAC","Zacatecas"),
	]

	CARRERAS = [
		("sistemas", "Ingeniería en Sistemas Computacionales"),
		("bioquimica", "Ingeniería Bioquímica"),
		("electromecanica", "Ingeniería Electromecánica"),
		("arquitectura", "Arquitectura"),
		("administracion", "Licenciatura en Administración"),
		("contabilidad", "Contador Público"),
		("gestion", "Ingenieria en Gestión Empresarial"),
	]

	SEMESTRES = [
		("1", "1"),
		("2", "2"),
		("3", "3"),
		("4", "4"),
		("5", "5"),
		("6", "6"),
		("7", "7"),
		("8", "8"),
		("9", "9"),
		("10", "10"),
		("11", "11"),
		("12", "12")		
	]

	STATES = [
		("draft", "Pendiente"),
		("done", "Confirmado")
	]

	fecha_registro = models.DateField(auto_now_add=True)
	fecha_modificacion = models.DateField(auto_now=True)
	fecha_pago = models.DateField(null=True, blank=True)
	# user = models.ForeignKey(User, on_delete=models.CASCADE)
	nombre = models.CharField(max_length=255)
	apellidop = models.CharField(max_length=255)
	apellidom = models.CharField(max_length=255)
	nocontrol = models.CharField(max_length=255, null=True, blank=True)
	rfc = models.CharField(max_length=255, null=True, blank=True)
	institucion = models.CharField(max_length=255)
	carrera = models.CharField(max_length=255, choices=CARRERAS, null=True, blank=True)
	semestre = models.CharField(max_length=255, choices=SEMESTRES, null=True, blank=True)
	email = models.EmailField(max_length=255)
	telefono = models.CharField(max_length=10)
	municipio = models.CharField(max_length=255)	
	estado = models.CharField(max_length=255, choices=ESTADOS)
	tipo_registro = models.CharField(max_length=255, choices=TIPO_REGISTRO)
	state = models.CharField(max_length=255, choices=STATES)

	def __str__(self):
		return self.nombre