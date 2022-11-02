# Rest imports
from rest_framework import serializers

# Models 
# El serializador lo que hace es trabajar con el modelo de la base. Es como si hiciera una doble autenticación
# Por un lado trabajamos con el querySet y por otro contrasta con el tipo de dato que le asignamos al modelo

from heroe.models import Hero

# Serializer
# El Serializer es una clase. Es buena practica ponerle el nombre de con lo que nosotros vamos a traducir o el tipo de modelo

class HeroSerializer(serializers.ModelSerializer): 
    
    # Hiper parámetros. Aca vamos a hacer la configuración principal de como se va a manejar  el serializer
    # A esa configuracion le debemos indicar el modelos y los campos que nosotros queremos traducir
    class Meta:
        model = Hero
        # De esta forma le indicamos que queremos trabajar con todos lso campos
        # Si quisieramos trabajar solo con algunos abrimos una tupla y le indicamos el nombre de los campos deseados en formato string
        fields = '__all__'