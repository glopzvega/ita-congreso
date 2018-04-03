from django.conf.urls import url

from . import views

urlpatterns = [
	
	url(r'^$', views.index, name="index"),
	url(r'^registrar/', views.registrar, name="registrar"),
	url(r'^confirmacion/', views.confirmacion, name="confirmacion"),

]