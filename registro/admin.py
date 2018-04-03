from django.contrib import admin

# Register your models here.

from .models import Registro

@admin.register(Registro)
class AdminRegistro(admin.ModelAdmin):
	# fields = ('id', 'imagen')
	list_display = ('id', 'nombre', 'apellidop', 'apellidom', 'email', 'nocontrol', 'rfc', 'tipo_registro')
