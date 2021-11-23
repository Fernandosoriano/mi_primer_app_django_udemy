# from django.http.response import HttpResponse
from django.shortcuts import render
from personas.models import Persona

# Create your views here.
# def bienvenido(request):
    # return HttpResponse ("Hola mundo desde django")
def bienvenido(request):
    # cada clase de modelo tiene acceso a un atributo llamado objects, manejador, que te permite  traer información de la BD
    no_personas = Persona.objects.count() # con count obtienes el número de personas desde la BD
    # te trae todos los objetos de tipo persona que tienes en tu tabla de base de datos
    # personas = Persona.objects.all()
    personas = Persona.objects.order_by('-id', 'nombre') #si le pones un - orden por id de manera descendente
    # y puedes agreagar ordenamiento con diferentes campos
    
    # mensajes = {'msg1': 'valor mensaje 1', 'msg2':'valor mensaje 2'}
    return render (request,'bienvenido.html',{'no_personas':no_personas, 'personas': personas})

# def despedirse(request):
#     return HttpResponse ("Despedida desde django")
# def contacto(request):
#     return HttpResponse ("celular: 5545834881, correo: fersoriano@ciencias.unam.mx")  
