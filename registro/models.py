from django.db import models

# Create your models here.

class Registro(models.Model):

	TIPO_REGISTRO = [
		('alumno', 'Alumno'),
		('exalumno', 'Exalumno'),
		('profesional', 'Profesional')
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
	
	nombre = models.CharField(max_length=255)
	apellidop = models.CharField(max_length=255)
	apellidom = models.CharField(max_length=255)
	nocontrol = models.CharField(max_length=255)
	rfc = models.CharField(max_length=255)
	email = models.EmailField(max_length=255)
	municipio = models.CharField(max_length=255)	
	estado = models.CharField(max_length=255, choices=ESTADOS)
	tipo_registro = models.CharField(max_length=255, choices=TIPO_REGISTRO)

	def __str__(self):
		return self.nombre