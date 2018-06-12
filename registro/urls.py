from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
	
	path('', views.index, name="index"),	
	path('confirmacion/', views.confirmacion, name="confirmacion"),
	
	path('pagos/', views.pagos, name="pagos"),
	path('pagos/print/', views.pagos_print, name="pagos_print"),

	path('horarios/<int:lugar_id>', views.horarios, name="horarios"),
	
	path('registros/pago/<int:id>', views.registros_pago, name="registros_pago"),
	path('registros/', views.registros, name="registros"),
	path('registros/print/', views.registros_print, name="registros_print"),
	path('registros/nuevo', views.registros_nuevo, name="registros_nuevo"),
	path('registros/editar/<int:id>', views.registros_editar, name="registros_editar"),
	
	path('ponentes/', views.ponentes, name="ponentes"),
	path('ponentes/nuevo/', views.ponentes_nuevo, name="ponentes_nuevo"),
	path('ponentes/editar/<int:id>', views.ponentes_editar, name="ponentes_editar"),
	path('ponentes/detalle/<int:id>', views.ponentes_detalle, name="ponentes_detalle"),
	
	# path('profesores/', views.profesores, name="profesores"),
	# path('profesores/nuevo/', views.profesores_nuevo, name="profesores_nuevo"),
	# path('profesores/editar/<int:id>', views.profesores_editar, name="profesores_editar"),
	# path('profesores/detalle/<int:id>', views.profesores_detalle, name="profesores_detalle"),
	
	# path('conferencias/', views.conferencias, name="conferencias"),
	# path('conferencias/nuevo/', views.conferencias_nuevo, name="conferencias_nuevo"),
	# path('conferencias/editar/<int:id>', views.conferencias_editar, name="conferencias_editar"),
	
	path('talleres/', views.talleres, name="talleres"),
	path('talleres/nuevo/', views.talleres_nuevo, name="talleres_nuevo"),
	path('talleres/editar/<int:id>', views.talleres_editar, name="talleres_editar"),
	
	# path('lugares/', views.lugares, name="lugares"),
	# path('lugares/nuevo/', views.lugares_nuevo, name="lugares_nuevo"),
	# path('lugares/editar/<int:id>', views.lugares_editar, name="lugares_editar"),
	
]