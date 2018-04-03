from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import RegistroModelForm

# Create your views here.

def index(request):

	context = {
		
	}
	return render(request, "registro/index.html", context)

def registrar(request):

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

	return render(request, "registro/formulario.html", context)	

def confirmacion(request):

	context = {
		
	}
	return render(request, "registro/confirmacion.html", context)