from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
	
	path('', views.index, name="index"),	
	path('pagos/', views.pagos, name="pagos"),
	path('pagos/print/', views.pagos_print, name="pagos_print"),
	path('registros/pago/<int:id>', views.registros_pago, name="registros_pago"),
	path('registros/', views.registros, name="registros"),
	path('registros/print/', views.registros_print, name="registros_print"),
	path('registros/nuevo', views.registros_nuevo, name="registros_nuevo"),
	path('registros/editar/<int:id>', views.registros_editar, name="registros_editar"),
	path('ponentes/', views.ponentes, name="ponentes"),
	path('ponentes/nuevo/', views.ponentes_nuevo, name="ponentes_nuevo"),
	path('ponentes/editar/<int:id>', views.ponentes_editar, name="ponentes_editar"),
	path('conferencias/', views.conferencias, name="conferencias"),
	path('conferencias/nuevo/', views.conferencias_nuevo, name="conferencias_nuevo"),
	path('conferencias/editar/<int:id>', views.conferencias_editar, name="conferencias_editar"),
	path('talleres/', views.talleres, name="talleres"),
	path('talleres/nuevo/', views.talleres_nuevo, name="talleres_nuevo"),
	path('talleres/editar/<int:id>', views.talleres_editar, name="talleres_editar"),
	path('lugares/', views.lugares, name="lugares"),
	path('lugares/nuevo/', views.lugares_nuevo, name="lugares_nuevo"),
	path('lugares/editar/<int:id>', views.lugares_editar, name="lugares_editar"),
	path('confirmacion/', views.confirmacion, name="confirmacion"),

]