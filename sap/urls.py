from django.contrib import admin
from django.urls import path
from personas.views import detallePersona, nuevaPersona, editarPersona, eliminarPersona
# from  webapp.views import bienvenido, despedirse,contacto
from  webapp.views import bienvenido


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('bienvenido/', bienvenido)  # el 2 param es el nombre de la función que quieres madar a llamar
    path('', bienvenido, name = 'index'),
    # path('despedida', despedirse),
    # path('contacto', contacto)
    path('detalle_persona/<int:id>',detallePersona),
    path('nueva_persona', nuevaPersona),
    path('editar_persona/<int:id>', editarPersona),
    path('eliminar_persona/<int:id>', eliminarPersona)

]
