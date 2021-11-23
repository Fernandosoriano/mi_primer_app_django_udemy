from django.shortcuts import get_object_or_404, redirect, render
from personas.models import Persona
from django.forms import modelform_factory
from personas.forms import PersonaForm

def detallePersona(request,id):
    # personaVar  = persona.objects.get(pk = id)

    # Para controlar que no nos arroje un error en caso de que
    # metamos un id que no exista y no saroje un error 404
    persona  =  get_object_or_404(Persona, pk = id)

    return render(request, 'personas/detalle.html', {'persona': persona})

# PersonaForm = modelform_factory(Persona, exclude = [])

def nuevaPersona(request):
    if request.method == 'POST':
        formaPersona = PersonaForm(request.POST) # con request.POST obtienes la información de los datos que envía el cliente desde el 
        # formulario al servidor   
        if formaPersona.is_valid():
            formaPersona.save()
            return redirect('index')
        # else:
        #     return render(request, 'personas/nuevo.html', {'formaPersona': formaPersona})
            
    
    else:   #caso de peticion tipo GET se te abre el formulario
        formaPersona = PersonaForm()
        
    return render(request, 'personas/nuevo.html', {'formaPersona': formaPersona})


def editarPersona(request, id):
    persona  =  get_object_or_404(Persona, pk = id)
    if request.method == 'POST':
        formaPersona = PersonaForm(request.POST, instance = persona) # con request.POST obtienes la información de los datos que envía el cliente desde el 
        # en este caso a diferencia de la petición post del método de nueva persona
        # especificas la instancia, esto hace que se haga un update, en vez de un insert
        # formulario al servidor, ya que aquí sí se incluye el id, y en el formulario solito
        # no, por eso aquí django nota la diferencia, si ya existe le id, hace un put
        # y sino, hace un insert a la BD  
        if formaPersona.is_valid():
            formaPersona.save()
            return redirect('index')
        # else:
        #     return render(request, 'personas/nuevo.html', {'formaPersona': formaPersona})
            
    
    else:   #caso de peticion tipo GET se te abre el formulario cuando le das click a editar persona
        formaPersona = PersonaForm(instance = persona)
        
    return render(request, 'personas/editar.html', {'formaPersona': formaPersona})



def eliminarPersona(request, id):
    persona  =  get_object_or_404(Persona, pk = id)
    if persona:
        persona.delete()
    return redirect('index')