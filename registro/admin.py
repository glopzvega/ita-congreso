from django.contrib import admin

# Register your models here.

from .models import Registro, Ponente, Lugar, Conferencia, Horario

@admin.register(Ponente)
class AdminPonente(admin.ModelAdmin):
	# fields = ('id', 'imagen')
	list_display = ('id', 'nombre', 'titulo', 'resumen', 'activo')

@admin.register(Lugar)
class AdminLugar(admin.ModelAdmin):
	# fields = ('id', 'imagen')
	list_display = ('id', 'nombre')

@admin.register(Horario)
class AdminLugar(admin.ModelAdmin):
	# fields = ('id', 'imagen')
	list_display = ('id', 'lugar', 'sala', 'fecha', 'hora', 'hora_fin')

@admin.register(Conferencia)
class AdminConferencia(admin.ModelAdmin):
	# fields = ('id', 'imagen')
	list_display = ('id', 'nombre', 'fecha_hora', 'ponente', 'lugar')	

@admin.register(Registro)
class AdminRegistro(admin.ModelAdmin):
	# fields = ('id', 'imagen')
	list_display = ('id', 'fecha_registro', 'nombre', 'apellidop', 'apellidom', 'email', 'nocontrol', 'carrera', 'semestre', 'rfc', 'tipo_registro', 'state')
	list_filter = ('state', 'tipo_registro')