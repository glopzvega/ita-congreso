from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from decimal import Decimal
from datetime import datetime,timedelta
from .forms import RegistroModelForm, LugarModelForm, PonenteModelForm, ConferenciaModelForm, TallerModelForm

from .models import Lugar, Ponente, Conferencia, Taller, Registro, Horario
from django.contrib.auth.decorators import login_required

from django.core.mail import send_mail

# Create your views here.
# @user_passes_test(lambda u: u.is_superuser)
# @staff_member_required

def index(request):

	# if request.method == 'POST':
		
	# 	form = RegistroModelForm(request.POST, request.FILES)
		
	# 	if form.is_valid():
	# 		# commit=False tells Django that "Don't send this to database yet.
	# 		# I have more things I want to do with it."
	# 		registro = form.save(commit=False)
	# 		registro.save()
			
	# 		return redirect('confirmacion')
			
	# else:
	# 	form = RegistroModelForm()

	ponentes = Ponente.objects.filter(tipo__exact="ponente")
	profesores = Ponente.objects.filter(tipo__exact="profesor")
	conferencias = Conferencia.objects.filter(tipo__exact='conferencia')
	talleres = Taller.objects.filter()

	context = {
		"conferencias" : ponentes,
		"talleres" : talleres,
		# "ponentes" : ponentes,
		# "form" : form
	}

	return render(request, "registro/index.html", context)

def confirmacion(request):

	context = {
		
	}
	return render(request, "registro/confirmacion.html", context)

@login_required
def pagos(request):

	if not request.user.is_superuser:
		return redirect("registros")

	registros = Registro.objects.all()
	
	context = {
		"data" : registros
	}
	
	return render(request, "registro/pagos.html", context)

@login_required
def registros_pago(request, id):

	if not request.user.is_superuser:
		return redirect("registros")

	registro = get_object_or_404(Registro, pk=id)

	monto = request.GET.get("monto", 0)
	monto = Decimal(monto)
	if monto > 0:
		registro.fecha_pago = datetime.now().strftime("%Y-%m-%d")
		if registro.saldo <= monto:
			registro.state = "done"
			registro.saldo = 0
		else:
			registro.state = "open"
			registro.saldo = registro.saldo - monto
		registro.save()
	# registros = Registro.objects.all().values("id", "nombre", "apellidop", "apellidom", "fecha_pago", "email", "tipo", "identificacion", "semestre", "carrera", "state")

	send_mail(
	    'PAGO REGISTRADO',
	    'Se ha registrado tu pago para el congreso CIITYS 2018 por el monto de ' + str(monto),
	    'g.albertolopezvega@gmail.com',
	    [registro.email],
	    fail_silently=False,
	)

	res = { 
		"success" : True, 
		"data" : [
			{
				"id" : registro.id,
				"nombre" : registro.nombre,
				"apellidop" : registro.apellidop,
				"apellidom" : registro.apellidom,
				"fecha_pago" : registro.fecha_pago,
				"email" : registro.email,
				"tipo" : registro.tipo_registro,
				"nocontrol" : registro.nocontrol,
				"rfc" : registro.rfc,
				"semestre" : registro.semestre,
				"carrera" : registro.carrera,
				"saldo" : registro.saldo,
				"state" : registro.state,
			}
		]
	}
	
	# if registro.state != "done":
	# 	res["success"] = False
	
	return JsonResponse(res, safe=False)

	
	# context = {
	# 	"data" : registros
	# }
	
	# return render(request, "registro/pagos.html", context)

# @login_required
# def horarios(request, lugar_id):

# 	if not request.user.is_staff:
# 		return redirect("registros")

# 	horarios = Horario.objects.filter(lugar__exact=lugar_id).values("id", "lugar", "sala", "fecha", "hora", "hora_fin")
		
# 	data = list(horarios)
	
# 	return JsonResponse(data, safe=False)


@login_required
def registros(request):

	registros = Registro.objects.all()
	
	context = {
		"data" : registros
	}
	
	return render(request, "registro/registros.html", context)

@login_required
def registros_print(request):

	registros = Registro.objects.all()
	
	context = {
		"data" : registros
	}
	
	return render(request, "registro/registros_print.html", context)

@login_required
def pagos_print(request):

	if not request.user.is_superuser:
		return redirect("registros")

	registros = Registro.objects.all()
	
	context = {
		"data" : registros
	}
	
	return render(request, "registro/pagos_print.html", context)

def registros_nuevo(request):
	
	messages = []
	if request.method == 'POST':
		
		form = RegistroModelForm(request.POST, request.FILES)
		
		if form.is_valid():
			# commit=False tells Django that "Don't send this to database yet.
			# I have more things I want to do with it."
			registro = form.save(commit=False)
			existe = False

			if registro.nocontrol:
				r = Registro.objects.filter(nocontrol__exact=registro.nocontrol)
				if r:
					existe = True
					messages.append({"error" : "El No. de Control ya se había registrado anteriormente."})
			elif registro.rfc:
				r = Registro.objects.filter(rfc__exact=registro.rfc)
				if r:
					existe = True
					messages.append({"error" : "El RFC ya se había registrado anteriormente."})			

			if existe:

				context = {
					"form" : form, 					
					"messages" : messages
				}
				
				return render(request, "registro/registros_nuevo.html", context)

			registro.user = request.user
			
			registro.saldo = 500
			if registro.tipo_registro == "profesional":
				registro.saldo = 3000

			registro.state = "draft"
			registro.save()

			monto = registro.saldo

			send_mail(
			    'PRE REGISTRO REALIZADO',
			    'Se ha realizado su pre registro para el congreso CIITYS 2018, para continuar con su registro e inscribirse en uno de los talleres deberá realizar su pago por el monto de ' + str(monto),
			    'g.albertolopezvega@gmail.com',
			    [registro.email],
			    fail_silently=False,
			    html_message='Se ha realizado su pre registro para el congreso CIITYS 2018, para continuar con su registro e inscribirse en uno de los talleres deberá realizar su pago. <br> <b>REFERENCIA BANCARIA</b> <br> BANCO: <b>BANORTE</b><br>EMPRESA:<b>37333</b><br>REFERENCIAS: <b>E024CIITYS186</b><br>MONTO: <b>$' + str(monto) + '</b>'
			)
			
			return redirect('confirmacion')
			
	else:
		form = RegistroModelForm()

	context = {
		"form" : form,
		"messages" : messages
	}
	
	return render(request, "registro/registros_nuevo.html", context)

@login_required
def registros_editar(request, id):

	if not request.user.is_staff or not request.user.is_superuser:
		return redirect("registros")
	
	registro = get_object_or_404(Registro, pk=id)
	
	# Si accedo por medio de POST a esta vista
	if request.method == 'POST':
		# Obtengo la informacion enviada por POST y FILES
		form = RegistroModelForm(request.POST, instance=registro)
		# Valido el formulario
		if form.is_valid():
			# Guardo el formulario
			form.save()
			# Devuelvo el template
			return redirect('registros')
	
	# Si acceso por GET
	else:
		# Genero una instancia de mi ModelForm
		# Le paso como parametro el producto que voy a enviar
		form = RegistroModelForm(instance=registro)

	context = {
		"form" : form,
		"data" : registro
	}
	
	return render(request, "registro/registros_editar.html", context)

@login_required
def ponentes(request):

	registros = Ponente.objects.filter(tipo__exact="ponente")
	
	context = {
		"data" : registros
	}
	
	return render(request, "registro/ponentes.html", context)


@login_required
def ponentes_nuevo(request):

	if not request.user.is_staff:
		return redirect("registros")
	
	if request.method == 'POST':
		
		form = PonenteModelForm(request.POST, request.FILES, user=request.user)
		
		if form.is_valid():
			# commit=False tells Django that "Don't send this to database yet.
			# I have more things I want to do with it."
			registro = form.save(commit=False)
			registro.activo = True
			registro.save()
			
			return redirect('ponentes')
			
	else:
		form = PonenteModelForm(user=request.user)

	context = {
		"form" : form
	}
	
	return render(request, "registro/ponentes_nuevo.html", context)

def ponentes_detalle(request, id):
	
	registro = get_object_or_404(Ponente, pk=id)	

	context = {		
		"data" : registro
	}
	
	return render(request, "registro/ponentes_detalle.html", context)

@login_required
def ponentes_editar(request, id):

	if not request.user.is_staff:
		return redirect("registros")
	
	registro = get_object_or_404(Ponente, pk=id)
	
	# Si accedo por medio de POST a esta vista
	if request.method == 'POST':
		# Obtengo la informacion enviada por POST y FILES
		form = PonenteModelForm(request.POST, request.FILES, instance=registro, user=request.user)
		# Valido el formulario
		if form.is_valid():
			# Guardo el formulario
			ponente = form.save(commit=False)

			if request.FILES and request.FILES["foto"]:
				ponente.foto = request.FILES["foto"]
			# Guardo en la BD
			ponente.save()			
			# Devuelvo el template
			return redirect('ponentes')
	
	# Si acceso por GET
	else:
		# Genero una instancia de mi ModelForm
		# Le paso como parametro el producto que voy a enviar
		form = PonenteModelForm(instance=registro, user=request.user)

	context = {
		"form" : form,
		"data" : registro
	}
	
	return render(request, "registro/ponentes_editar.html", context)

# @login_required
# def profesores(request):

# 	registros = Ponente.objects.filter(tipo__exact="profesor")
	
# 	context = {
# 		"data" : registros
# 	}
	
# 	return render(request, "registro/profesores.html", context)


# @login_required
# def profesores_nuevo(request):

# 	if not request.user.is_staff:
# 		return redirect("registros")
	
# 	if request.method == 'POST':
		
# 		form = PonenteModelForm(request.POST, request.FILES)
		
# 		if form.is_valid():
# 			# commit=False tells Django that "Don't send this to database yet.
# 			# I have more things I want to do with it."
# 			registro = form.save(commit=False)
# 			registro.tipo = "profesor"
# 			registro.activo = True
# 			registro.save()
			
# 			return redirect('profesores')
			
# 	else:
# 		form = PonenteModelForm()

# 	context = {
# 		"form" : form
# 	}
	
# 	return render(request, "registro/profesores_nuevo.html", context)

# def profesores_detalle(request, id):
	
# 	registro = get_object_or_404(Ponente, pk=id)	

# 	context = {		
# 		"data" : registro
# 	}
	
# 	return render(request, "registro/profesores_detalle.html", context)

# @login_required
# def profesores_editar(request, id):

# 	if not request.user.is_staff:
# 		return redirect("registros")
	
# 	registro = get_object_or_404(Ponente, pk=id)
	
# 	# Si accedo por medio de POST a esta vista
# 	if request.method == 'POST':
# 		# Obtengo la informacion enviada por POST y FILES
# 		form = PonenteModelForm(request.POST, request.FILES, instance=registro)
# 		# Valido el formulario
# 		if form.is_valid():
# 			# Guardo el formulario
# 			ponente = form.save(commit=False)

# 			if request.FILES and request.FILES["foto"]:
# 				ponente.foto = request.FILES["foto"]
# 			# Guardo en la BD
# 			ponente.save()			
# 			# Devuelvo el template
# 			return redirect('profesores')
	
# 	# Si acceso por GET
# 	else:
# 		# Genero una instancia de mi ModelForm
# 		# Le paso como parametro el producto que voy a enviar
# 		form = PonenteModelForm(instance=registro)

# 	context = {
# 		"form" : form,
# 		"data" : registro
# 	}
	
# 	return render(request, "registro/profesores_editar.html", context)


# @login_required
# def conferencias(request):

# 	registros = Conferencia.objects.filter(tipo__exact='conferencia')
	
# 	context = {
# 		"data" : registros
# 	}
	
# 	return render(request, "registro/conferencias.html", context)

@login_required
def talleres(request):

	registros = Taller.objects.all()
	
	context = {
		"data" : registros
	}
	
	return render(request, "registro/talleres.html", context)

# @login_required
# def conferencias_nuevo(request):

# 	if not request.user.is_staff:
# 		return redirect("registros")
	
# 	if request.method == 'POST':
		
# 		form = ConferenciaModelForm(request.POST, request.FILES)
		
# 		if form.is_valid():
# 			# commit=False tells Django that "Don't send this to database yet.
# 			# I have more things I want to do with it."
# 			registro = form.save(commit=False)
# 			registro.tipo = 'conferencia'
# 			registro.save()
			
# 			return redirect('conferencias')
			
# 	else:
# 		form = ConferenciaModelForm()

# 	context = {
# 		"form" : form
# 	}
	
# 	return render(request, "registro/conferencias_nuevo.html", context)

@login_required
def talleres_nuevo(request):

	if not request.user.is_staff:
		return redirect("registros")
	
	if request.method == 'POST':
		form = TallerModelForm(request.POST, request.FILES)
		
		if form.is_valid():
			# commit=False tells Django that "Don't send this to database yet.
			# I have more things I want to do with it."
			registro = form.save(commit=False)
			registro.user = request.user
			# registro.tipo = 'taller'
			# fecha_ini = registro.fecha
			# fecha_ini = datetime.strptime(fecha_ini, "%Y-%m-%d")
			dias = timedelta(days=registro.duracion)
			registro.fecha_fin = registro.fecha + dias
			registro.save()
			
			return redirect('talleres')
			
	else:
		form = TallerModelForm()

	context = {
		"form" : form
	}
	
	return render(request, "registro/talleres_nuevo.html", context)

# @login_required
# def conferencias_editar(request, id):

# 	if not request.user.is_staff:
# 		return redirect("registros")
	
# 	registro = get_object_or_404(Conferencia, pk=id)
	
# 	# Si accedo por medio de POST a esta vista
# 	if request.method == 'POST':
# 		# Obtengo la informacion enviada por POST y FILES
# 		form = ConferenciaModelForm(request.POST, instance=registro)
# 		# Valido el formulario
# 		if form.is_valid():
# 			# Guardo el formulario
# 			form.save()
# 			# Devuelvo el template
# 			return redirect('conferencias')
	
# 	# Si acceso por GET
# 	else:
# 		# Genero una instancia de mi ModelForm
# 		# Le paso como parametro el producto que voy a enviar
# 		form = ConferenciaModelForm(instance=registro)

# 	context = {
# 		"form" : form,
# 		"data" : registro
# 	}
	
# 	return render(request, "registro/conferencias_editar.html", context)

@login_required
def talleres_editar(request, id):

	if not request.user.is_staff:
		return redirect("registros")
	
	registro = get_object_or_404(Taller, pk=id)
	
	# Si accedo por medio de POST a esta vista
	if request.method == 'POST':
		# Obtengo la informacion enviada por POST y FILES
		form = TallerModelForm(request.POST, instance=registro)
		# Valido el formulario
		if form.is_valid():
			# Guardo el formulario
			form.save()
			# Devuelvo el template
			return redirect('talleres')
	
	# Si acceso por GET
	else:
		# Genero una instancia de mi ModelForm
		# Le paso como parametro el producto que voy a enviar
		form = TallerModelForm(instance=registro)

	context = {
		"form" : form,
		"data" : registro
	}
	
	return render(request, "registro/talleres_editar.html", context)

# @login_required
# def lugares(request):
	
# 	lista = Lugar.objects.all()
	
# 	context = {
# 		"data" : lista
# 	}
	
# 	return render(request, "registro/lugares.html", context)

# @login_required
# def lugares_nuevo(request):

# 	if not request.user.is_staff:
# 		return redirect("registros")
	
# 	if request.method == 'POST':
		
# 		form = LugarModelForm(request.POST, request.FILES)
		
# 		if form.is_valid():
# 			# commit=False tells Django that "Don't send this to database yet.
# 			# I have more things I want to do with it."
# 			registro = form.save(commit=False)
# 			registro.save()
			
# 			return redirect('lugares')
			
# 	else:
# 		form = LugarModelForm()

# 	context = {
# 		"form" : form
# 	}
	
# 	return render(request, "registro/lugares_nuevo.html", context)

# @login_required
# def lugares_editar(request, id):

# 	if not request.user.is_staff or not request.user.is_superuser:
# 		return redirect("registros")

# 	registro = get_object_or_404(Lugar, pk=id)
	
# 	# Si accedo por medio de POST a esta vista
# 	if request.method == 'POST':
# 		# Obtengo la informacion enviada por POST y FILES
# 		form = LugarModelForm(request.POST, instance=registro)
# 		# Valido el formulario
# 		if form.is_valid():
# 			# Guardo el formulario
# 			form.save()
# 			# Devuelvo el template
# 			return redirect('lugares')
	
# 	# Si acceso por GET
# 	else:
# 		# Genero una instancia de mi ModelForm
# 		# Le paso como parametro el producto que voy a enviar
# 		form = LugarModelForm(instance=registro)

# 	# Devuelvo el template
# 	return render(request, 'registro/lugares_editar.html', {'form': form, "registro" : registro})

