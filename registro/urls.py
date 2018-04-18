from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
	
	path('', views.index, name="index"),	
	path('administracion/', views.administracion, name="administracion"),
	path('ponentes/', views.ponentes, name="ponentes"),
	path('ponentes/nuevo/', views.ponentes_nuevo, name="ponentes_nuevo"),
	path('ponentes/editar/', views.ponentes_editar, name="ponentes_editar"),
	path('conferencias/', views.conferencias, name="conferencias"),
	path('conferencias/nuevo/', views.conferencias, name="conferencias_nuevo"),
	path('conferencias/editar/', views.conferencias, name="conferencias_editar"),
	path('lugares/', views.lugares, name="lugares"),
	path('lugares/nuevo/', views.lugares_nuevo, name="lugares_nuevo"),
	path('lugares/editar/<int:id>', views.lugares_editar, name="lugares_editar"),
	path('confirmacion/', views.confirmacion, name="confirmacion"),

]