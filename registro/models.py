from django.db import models

# Create your models here.

class Ponente(models.Model):

	nombre = models.CharField(max_length=255)
	email = models.EmailField(max_length=255)
	telefono = models.CharField(max_length=20)
	titulo = models.CharField(max_length=50)
	resumen = models.CharField(max_length=255)
	intro = models.TextField()
	foto = models.ImageField(blank=True)

	def __str__(self):
		return self.titulo + " " + self.nombre

class Lugar(models.Model):
	nombre = models.CharField(max_length=255)

	def __str__(self):
		return self.nombre

class Conferencia(models.Model):
	nombre = models.CharField(max_length=255)	
	descripcion = models.TextField()
	ponente = models.ForeignKey(Ponente, models.SET_NULL, blank=True, null=True)
	lugar = models.ForeignKey(Lugar, models.SET_NULL, blank=True, null=True)
	fecha_hora = models.DateTimeField(blank=True, null=True)	
	duracion = models.DecimalField(max_digits=5, decimal_places=2, default=1)
	foto = models.ImageField(blank=True)	

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
		("1", "1 Primero"),
		("2", "2 Segundo"),
		("3", "3 Tercero"),
		("4", "4 Cuarto"),
		("5", "5 Quinto"),
		("6", "6 Sexto"),
		("7", "7 Septimo"),
		("8", "8 Octavo"),
		("9", "9 Noveno"),
		("10", "10 Decimo")		
	]

	STATES = [
		("draft", "Pendiente"),
		("done", "Confirmado")
	]
	
	nombre = models.CharField(max_length=255)
	apellidop = models.CharField(max_length=255)
	apellidom = models.CharField(max_length=255)
	nocontrol = models.CharField(max_length=255)
	rfc = models.CharField(max_length=255)
	carrera = models.CharField(max_length=255, choices=CARRERAS)
	semestre = models.CharField(max_length=255, choices=SEMESTRES)
	email = models.EmailField(max_length=255)
	telefono = models.CharField(max_length=20)
	municipio = models.CharField(max_length=255)	
	estado = models.CharField(max_length=255, choices=ESTADOS)
	tipo_registro = models.CharField(max_length=255, choices=TIPO_REGISTRO)
	state = models.CharField(max_length=255, choices=STATES)

	def __str__(self):
		return self.nombre