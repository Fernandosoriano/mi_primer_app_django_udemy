from django.db import models

# Create your models here.
class Domicilio(models.Model):
    calle    = models.CharField(max_length=255)
    no_calle = models.IntegerField()
    pais     = models.CharField(max_length=255)

    def __str__(self):
        return f'Domicilio {self.id}: {self.calle} {self.no_calle} {self.pais}'

class Persona (models.Model):
    nombre    = models.CharField(max_length=255)
    apellido  = models.CharField(max_length=255)
    email     = models.CharField(max_length=255)
    domicilio = models.ForeignKey(Domicilio, on_delete = models.SET_NULL, null=True)
    # on_delete define qué pasa con el domicilio de la persona, en caso de que borres el
    # registro de la tabla Domicilio, en este caso le dices que lo ponga nulo
    # y para que el modelo acepte valores nulos, lo pones en True
    
    
    # puedes modificar la forma  en que se ve la info de tus objetos creados
    # que al  final son registros en la tabla de sql
    # usando el siguiente método de __str__

    def __str__(self):
        return f'Persona {self.id}: {self.nombre} {self.apellido} {self.email}'


