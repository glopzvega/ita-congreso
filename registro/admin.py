from django.contrib import admin

# Register your models here.

from .models import Registro, Ponente, Lugar, Conferencia

@admin.register(Ponente)
class AdminPonente(admin.ModelAdmin):
	# fields = ('id', 'imagen')
	list_display = ('id', 'nombre', 'titulo', 'intro')

@admin.register(Lugar)
class AdminLugar(admin.ModelAdmin):
	# fields = ('id', 'imagen')
	list_display = ('id', 'nombre')

@admin.register(Conferencia)
class AdminConferencia(admin.ModelAdmin):
	# fields = ('id', 'imagen')
	list_display = ('id', 'nombre', 'fecha_hora', 'ponente', 'lugar')	

@admin.register(Registro)
class AdminRegistro(admin.ModelAdmin):
	# fields = ('id', 'imagen')
	list_display = ('id', 'nombre', 'apellidop', 'apellidom', 'email', 'nocontrol', 'carrera', 'semestre', 'rfc', 'tipo_registro', 'state')
	list_filter = ('state', 'tipo_registro')