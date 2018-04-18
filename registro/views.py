from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import RegistroModelForm, LugarModelForm

from .models import Lugar, Ponente, Conferencia, Registro

# Create your views here.

def index(request):

	if request.method == 'POST':
		
		form = RegistroModelForm(request.POST, request.FILES)
		
		if form.is_valid():
			# commit=False tells Django that "Don't send this to database yet.
			# I have more things I want to do with it."
			registro = form.save(commit=False)
			registro.save()
			
			return redirect('confirmacion')
			
	else:
		form = RegistroModelForm()

	context = {
		"form" : form
	}

	return render(request, "registro/index.html", context)

def administracion(request):
	
	context = {

	}
	
	return render(request, "registro/admin.html", context)

def ponentes(request):
	
	context = {

	}
	
	return render(request, "registro/ponentes.html", context)


def ponentes_nuevo(request):
	
	context = {

	}
	
	return render(request, "registro/ponentes.html", context)

def ponentes_editar(request):
	
	context = {

	}
	
	return render(request, "registro/ponentes.html", context)

def conferencias(request):
	
	context = {

	}
	
	return render(request, "registro/conferencias.html", context)

def conferencias_nuevo(request):
	
	context = {

	}
	
	return render(request, "registro/conferencias.html", context)

def conferencias_editar(request):
	
	context = {

	}
	
	return render(request, "registro/conferencias.html", context)

def lugares(request):
	
	lista = Lugar.objects.all()
	
	context = {
		"data" : lista
	}
	
	return render(request, "registro/lugares.html", context)

def lugares_nuevo(request):
	
	if request.method == 'POST':
		
		form = LugarModelForm(request.POST, request.FILES)
		
		if form.is_valid():
			# commit=False tells Django that "Don't send this to database yet.
			# I have more things I want to do with it."
			registro = form.save(commit=False)
			registro.save()
			
			return redirect('lugares')
			
	else:
		form = LugarModelForm()

	context = {
		"form" : form
	}
	
	return render(request, "registro/lugares_nuevo.html", context)

def lugares_editar(request, id):

	registro = get_object_or_404(Lugar, pk=id)
	
	# Si accedo por medio de POST a esta vista
	if request.method == 'POST':
		# Obtengo la informacion enviada por POST y FILES
		form = LugarModelForm(request.POST, instance=registro)
		# Valido el formulario
		if form.is_valid():
			# Guardo el formulario
			form.save()
			# Devuelvo el template
			return redirect('lugares')
	
	# Si acceso por GET
	else:
		# Genero una instancia de mi ModelForm
		# Le paso como parametro el producto que voy a enviar
		form = LugarModelForm(instance=registro)

	# Devuelvo el template
	return render(request, 'registro/lugares_editar.html', {'form': form, "registro" : registro})

def confirmacion(request):

	context = {
		
	}
	return render(request, "registro/confirmacion.html", context)