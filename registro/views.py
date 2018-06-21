from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from decimal import Decimal
from datetime import datetime,timedelta
import pytz
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
def resumen(request):
	registros = Registro.objects.all()
	
	c_sistemas = 0
	c_sistemas_hombre = 0
	c_sistemas_mujer = 0

	c_bioquimica = 0
	c_bioquimica_hombre = 0
	c_bioquimica_mujer = 0
	
	c_electromecanica = 0
	c_electromecanica_hombre = 0
	c_electromecanica_mujer = 0
	
	c_arquitectura = 0
	c_arquitectura_hombre = 0
	c_arquitectura_mujer = 0
	
	c_administracion = 0
	c_administracion_hombre = 0
	c_administracion_mujer = 0
	
	c_contabilidad = 0
	c_contabilidad_hombre = 0
	c_contabilidad_mujer = 0
	
	c_gestion = 0
	c_gestion_hombre = 0
	c_gestion_mujer = 0

	c_otra = 0
	c_otra_hombre = 0
	c_otra_mujer = 0
	
	c_profesionista = 0
	c_profesionista_hombre = 0
	c_profesionista_mujer = 0

	c_total = 0
	c_total_hombre = 0
	c_total_mujer = 0

	o_sistemas = 0
	o_sistemas_hombre = 0
	o_sistemas_mujer = 0
	
	o_bioquimica = 0
	o_bioquimica_hombre = 0
	o_bioquimica_mujer = 0
	
	o_electromecanica = 0
	o_electromecanica_hombre = 0
	o_electromecanica_mujer = 0
	
	o_arquitectura = 0
	o_arquitectura_hombre = 0
	o_arquitectura_mujer = 0
	
	o_administracion = 0
	o_administracion_hombre = 0
	o_administracion_mujer = 0
	
	o_contabilidad = 0
	o_contabilidad_hombre = 0
	o_contabilidad_mujer = 0
	
	o_gestion = 0
	o_gestion_hombre = 0
	o_gestion_mujer = 0

	o_otra = 0
	o_otra_hombre = 0
	o_otra_mujer = 0
	
	o_profesionista = 0
	o_profesionista_hombre = 0
	o_profesionista_mujer = 0
	
	o_total = 0
	o_total_hombre = 0
	o_total_mujer = 0

	p_sistemas = 0
	p_sistemas_hombre = 0
	p_sistemas_mujer = 0
	
	p_bioquimica = 0
	p_bioquimica_hombre = 0
	p_bioquimica_mujer = 0
	
	p_electromecanica = 0
	p_electromecanica_hombre = 0
	p_electromecanica_mujer = 0
	
	p_arquitectura = 0
	p_arquitectura_hombre = 0
	p_arquitectura_mujer = 0
	
	p_administracion = 0
	p_administracion_hombre = 0
	p_administracion_mujer = 0
	
	p_contabilidad = 0
	p_contabilidad_hombre = 0
	p_contabilidad_mujer = 0
	
	p_gestion = 0
	p_gestion_hombre = 0
	p_gestion_mujer = 0

	p_otra = 0
	p_otra_hombre = 0
	p_otra_mujer = 0
	
	p_profesionista = 0
	p_profesionista_hombre = 0
	p_profesionista_mujer = 0
	
	p_total = 0
	p_total_hombre = 0
	p_total_mujer = 0

	i_subtotal_sistemas = 0
	i_subtotal_bioquimica = 0
	i_subtotal_electromecanica = 0
	i_subtotal_arquitectura = 0
	i_subtotal_administracion = 0
	i_subtotal_contabilidad = 0
	i_subtotal_gestion = 0
	i_subtotal_otra = 0
	i_subtotal_profesionista = 0
	i_total = 0

	for el in registros:

		if el.genero == "hombre":
			if el.carrera == "sistemas": 
				c_sistemas += 1
				c_sistemas_hombre += 1
			elif el.carrera == "bioquimica": 
				c_bioquimica += 1
				c_bioquimica_hombre += 1
			elif el.carrera == "electromecanica": 
				c_electromecanica += 1
				c_electromecanica_hombre += 1
			elif el.carrera == "arquitectura": 
				c_arquitectura += 1
				c_arquitectura_hombre += 1
			elif el.carrera == "administracion": 
				c_administracion += 1
				c_administracion_hombre += 1
			elif el.carrera == "contabilidad": 
				c_contabilidad += 1
				c_contabilidad_hombre += 1
			elif el.carrera == "gestion": 
				c_gestion += 1
				c_gestion_hombre += 1
			elif el.carrera == "otra": 
				c_otra += 1
				c_otra_hombre += 1
			elif el.carrera == "profesionista": 
				c_profesionista += 1
				c_profesionista_hombre += 1

			c_total_hombre += 1

		else:
			if el.carrera == "sistemas": 
				c_sistemas += 1
				c_sistemas_mujer += 1
			elif el.carrera == "bioquimica": 
				c_bioquimica += 1
				c_bioquimica_mujer += 1
			elif el.carrera == "electromecanica": 
				c_electromecanica += 1
				c_electromecanica_mujer += 1
			elif el.carrera == "arquitectura": 
				c_arquitectura += 1
				c_arquitectura_mujer += 1
			elif el.carrera == "administracion": 
				c_administracion += 1
				c_administracion_mujer += 1
			elif el.carrera == "contabilidad": 
				c_contabilidad += 1
				c_contabilidad_mujer += 1
			elif el.carrera == "gestion": 
				c_gestion += 1
				c_gestion_mujer += 1
			elif el.carrera == "otra": 
				c_otra += 1
				c_otra_mujer += 1
			elif el.carrera == "profesionista": 
				c_profesionista += 1
				c_profesionista_mujer += 1

			c_total_mujer += 1

		c_total += 1

	registros_open = registros.filter(state="open")

	for el in registros_open:
		if el.genero == "hombre":
			if el.carrera == "sistemas": 
				o_sistemas += 1
				o_sistemas_hombre += 1
				i_subtotal_sistemas += el.pagado
			elif el.carrera == "bioquimica": 
				o_bioquimica += 1
				o_bioquimica_hombre += 1
				i_subtotal_bioquimica += el.pagado			
			elif el.carrera == "electromecanica": 
				o_electromecanica += 1
				o_electromecanica_hombre += 1
				i_subtotal_electromecanica += el.pagado			
			elif el.carrera == "arquitectura": 
				o_arquitectura += 1
				o_arquitectura_hombre += 1
				i_subtotal_arquitectura += el.pagado	
			elif el.carrera == "administracion": 
				o_administracion += 1
				o_administracion_hombre += 1
				i_subtotal_administracion += el.pagado		
			elif el.carrera == "contabilidad": 
				o_contabilidad += 1
				o_contabilidad_hombre += 1
				i_subtotal_contabilidad += el.pagado	
			elif el.carrera == "gestion": 
				o_gestion += 1
				o_gestion_hombre += 1
				i_subtotal_gestion += el.pagado
			elif el.carrera == "otra": 
				o_otra += 1
				o_otra_hombre += 1
				i_subtotal_otra += el.pagado	
			elif el.carrera == "profesionista": 
				o_profesionista += 1
				o_profesionista_hombre += 1
				i_subtotal_profesionista += el.pagado			

			o_total_hombre += 1

		else:
			if el.carrera == "sistemas": 
				o_sistemas += 1
				o_sistemas_mujer += 1
				i_subtotal_sistemas += el.pagado
			elif el.carrera == "bioquimica": 
				o_bioquimica += 1
				o_bioquimica_mujer += 1
				i_subtotal_bioquimica += el.pagado
			elif el.carrera == "electromecanica": 
				o_electromecanica += 1
				o_electromecanica_mujer += 1
				i_subtotal_electromecanica += el.pagado
			elif el.carrera == "arquitectura": 
				o_arquitectura += 1
				o_arquitectura_mujer += 1
				i_subtotal_arquitectura += el.pagado
			elif el.carrera == "administracion": 
				o_administracion += 1
				o_administracion_mujer += 1
				i_subtotal_administracion += el.pagado
			elif el.carrera == "contabilidad": 
				o_contabilidad += 1
				o_contabilidad_mujer += 1
				i_subtotal_contabilidad += el.pagado
			elif el.carrera == "gestion": 
				o_gestion += 1
				o_gestion_mujer += 1
				i_subtotal_gestion += el.pagado
			elif el.carrera == "otra": 
				o_otra += 1
				o_otra_mujer += 1
				i_subtotal_otra += el.pagado
			elif el.carrera == "profesionista": 
				o_profesionista += 1
				o_profesionista_mujer += 1
				i_subtotal_profesionista += el.pagado

			o_total_mujer += 1

		i_total += el.pagado
		o_total += 1

	registros_done = registros.filter(state="done")

	for el in registros_done:
		if el.genero == "hombre":
			if el.carrera == "sistemas": 
				p_sistemas += 1
				p_sistemas_hombre += 1
				i_subtotal_sistemas += el.pagado
			elif el.carrera == "bioquimica": 
				p_bioquimica += 1
				p_bioquimica_hombre += 1
				i_subtotal_sistemas += el.pagado
			elif el.carrera == "electromecanica": 
				p_electromecanica += 1
				p_electromecanica_hombre += 1
				i_subtotal_electromecanica += el.pagado
			elif el.carrera == "arquitectura": 
				p_arquitectura += 1
				p_arquitectura_hombre += 1
				i_subtotal_arquitectura += el.pagado
			elif el.carrera == "administracion": 
				p_administracion += 1
				p_administracion_hombre += 1
				i_subtotal_administracion += el.pagado
			elif el.carrera == "contabilidad": 
				p_contabilidad += 1
				p_contabilidad_hombre += 1
				i_subtotal_contabilidad += el.pagado
			elif el.carrera == "gestion": 
				p_gestion += 1
				p_gestion_hombre += 1
				i_subtotal_gestion += el.pagado
			elif el.carrera == "otra": 
				p_otra += 1
				p_otra_hombre += 1
				i_subtotal_otra += el.pagado
			elif el.carrera == "profesionista": 
				p_profesionista += 1
				p_profesionista_hombre += 1
				i_subtotal_profesionista += el.pagado

			p_total_hombre += 1

		else:
			if el.carrera == "sistemas": 
				p_sistemas += 1
				p_sistemas_mujer += 1
				i_subtotal_sistemas += el.pagado
			elif el.carrera == "bioquimica": 
				p_bioquimica += 1
				p_bioquimica_mujer += 1
				i_subtotal_bioquimica += el.pagado
			elif el.carrera == "electromecanica": 
				p_electromecanica += 1
				p_electromecanica_mujer += 1
				i_subtotal_electromecanica += el.pagado
			elif el.carrera == "arquitectura": 
				p_arquitectura += 1
				p_arquitectura_mujer += 1
				i_subtotal_arquitectura += el.pagado
			elif el.carrera == "administracion": 
				p_administracion += 1
				p_administracion_mujer += 1
				i_subtotal_administracion += el.pagado
			elif el.carrera == "contabilidad": 
				p_contabilidad += 1
				p_contabilidad_mujer += 1
				i_subtotal_contabilidad += el.pagado
			elif el.carrera == "gestion": 
				p_gestion += 1
				p_gestion_mujer += 1
				i_subtotal_gestion += el.pagado
			elif el.carrera == "otra": 
				p_otra += 1
				p_otra_mujer += 1
				i_subtotal_otra += el.pagado
			elif el.carrera == "profesionista": 
				p_profesionista += 1
				p_profesionista_mujer += 1
				i_subtotal_otra += el.pagado

			p_total_mujer += 1

		i_total += el.pagado
		p_total += 1	
	
	contadores = [
		("Ingeniería en Sistemas Computacionales", c_sistemas, o_sistemas, p_sistemas, c_sistemas_hombre, c_sistemas_mujer, o_sistemas_hombre, o_sistemas_mujer, p_sistemas_hombre, p_sistemas_mujer, i_subtotal_sistemas),
		("Ingeniería Bioquímica", c_bioquimica, o_bioquimica, p_bioquimica, c_bioquimica_hombre, c_bioquimica_mujer, o_bioquimica_hombre, o_bioquimica_mujer, p_bioquimica_hombre, p_bioquimica_mujer, i_subtotal_bioquimica),
		("Ingeniería Electromecánica", c_electromecanica, o_electromecanica, p_electromecanica, c_electromecanica_hombre, c_electromecanica_mujer, o_electromecanica_hombre, o_electromecanica_mujer, p_electromecanica_hombre, p_electromecanica_mujer, i_subtotal_electromecanica),
		("Arquitectura", c_arquitectura, o_arquitectura, p_arquitectura, c_arquitectura_hombre, c_arquitectura_mujer, o_arquitectura_hombre, o_arquitectura_mujer, p_arquitectura_hombre, p_arquitectura_mujer, i_subtotal_arquitectura),
		("Licenciatura en Administración", c_administracion, o_administracion, p_administracion, c_administracion_hombre, c_administracion_mujer, o_administracion_hombre, o_administracion_mujer, p_administracion_hombre, p_administracion_mujer, i_subtotal_administracion),
		("Contador Público", c_contabilidad, o_contabilidad, p_contabilidad, c_contabilidad_hombre, c_contabilidad_mujer, o_contabilidad_hombre, o_contabilidad_mujer, p_contabilidad_hombre, p_contabilidad_mujer, i_subtotal_contabilidad),
		("Ingenieria en Gestión Empresarial", c_gestion, o_gestion, p_gestion, c_gestion_hombre, c_gestion_mujer, o_gestion_hombre, o_gestion_mujer, p_gestion_hombre, p_gestion_mujer, i_subtotal_gestion),
		("Alumno de Otra Institución", c_otra, o_otra, p_otra, c_otra_hombre, c_otra_mujer, o_otra_hombre, o_otra_mujer, p_otra_hombre, p_otra_mujer, i_subtotal_otra),
		("Profesionista", c_profesionista, o_profesionista, p_profesionista, c_profesionista_hombre, c_profesionista_mujer, o_profesionista_hombre, o_profesionista_mujer, p_profesionista_hombre, p_profesionista_mujer, i_subtotal_profesionista),
	]	

	mx_tz = pytz.timezone("America/Mexico_City")
	fecha =  datetime.now(mx_tz).strftime("%Y-%m-%d %H:%M")
	context = {
		"data" : contadores,
		"fecha" : fecha,
		"total" : c_total,
		"total_i" : i_total,
		"total_h" : c_total_hombre,
		"total_m" : c_total_mujer,
		"total_o" : o_total,
		"total_o_h" : o_total_hombre,
		"total_o_m" : o_total_mujer,
		"total_p" : p_total,
		"total_p_h" : p_total_hombre,
		"total_p_m" : p_total_mujer,
	}

	return render(request, "registro/resumen.html", context)

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
def horarios(request):

	if not request.user.is_staff or not request.user.is_superuser:
		return redirect("registros")

	horarios = Horario.objects.all().order_by("fecha", "hora", "sala")
	sala = ""
	if request.GET.get("sala", False):
		sala = request.GET.get("sala", False)
		horarios = horarios.filter(sala__exact="Salón " + sala)

	dia = ""
	if request.GET.get("dia", False):
		dia = request.GET.get("dia", False)
		horarios = horarios.filter(dia__exact=dia)

	data = []
	conferencias = Ponente.objects.all()
	for row in horarios:
		conf = conferencias.filter(horario__exact=row)
		item = {
			"name" : row.user.username[:3].upper(),
			"ponente" : "",
			"sala" : row.sala,
			"dia" : row.dia,
			"fecha" : row.fecha,
			"hora" : row.hora,
			"hora_fin" : row.hora_fin,
		}
		if conf:
			item["name"] = conf[0].ponencia
			item["ponente"] = conf[0].nombre

		data.append(item)
	
	context = {
		"data" : data,
		"sala" : sala,
		"dia" : dia
	}
	
	return render(request, "registro/horarios.html", context)

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

		registro.pagado = monto
		registro.save()
	# registros = Registro.objects.all().values("id", "nombre", "apellidop", "apellidom", "fecha_pago", "email", "tipo", "identificacion", "semestre", "carrera", "state")

	send_mail(
	    'PAGO REGISTRADO',
	    'Se ha registrado tu pago para el congreso CIITYS 2018 por el monto de ' + str(monto),
	    'glopzvega@iozoft.com',
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
				"pagado" : registro.pagado,
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
			    'glopzvega@iozoft.com',
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

