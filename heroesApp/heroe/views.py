# Rest imports
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Models imports
from heroe.models import Hero

# Serializers imports
from heroe.serializer import HeroSerializer

# Helpers
from heroe.helpers.heroeErrors import hayHeroe

# Create your views here.
# Todo lo relacionado a la logica, a lo que vamos a recibir, las operaciones que vamos hacer, etc

class HeroApiView(APIView):
    
    def get(self, request):
        """
        Retorna un listado con todos los heroes almacenados en la base
        """
        # Request es un objeto que tiene metodos por eso le podemos poner un punto al aldo y llamarlos
        # Con esto vemos lo que el front nos pide
        # print(f'REQUEST --> {request}')
        
        # Conectamos el archivo de Views con elementos del archivo de Models
        # Se iguala  aHero porque es la clase que crea los objetos heroes
        # Cuando utilizamos el ORM debemos llamar el metodo objects para decirle que quiero trabajar con los objetos del modelo Heroe
        # Los objetos son los datos que nosotros tenemos
        # El all nos trae todos los objetos de este metodo
        # En heroes almacenamos todos los objetos de la base
        
        heroes = Hero.objects.all()

        # El values es un metodo para que me devuelva los datos que tengo
        # print(heroes.values())
        
        # Utilizamos la traduccion de nuestro serializador, le pasamos nuestros heroes y al mismo tiempo les decimos que son muchos valores
        heroes_serializer = HeroSerializer(heroes, many=True)
        
        # print(heroes_serializer)
        # print(heroes_serializer.data)
        
        # La data es la informacion que nosotros queramos devolver al frontend. 
        # Puede ser info de la BD, algun mensaje, o directamente nada. Lo que nosotros queramos

        return Response(
            data=heroes_serializer.data,
            status=status.HTTP_200_OK
            )

""" 
    def post(self,request):
        'Crea un nuevo registro/heroe'
        print('Primer post')
        # Mediante el serializer vamos a transformar el JSON a un objeto de BD
        # El serializaer hace una preconsulta a la base para chequear que este todo ok
        # Primero hace una validacion interna con nuestros parametros del heroe del modelo
        # Luego de hacer esas priemras comprobaciones hace una consulta interna a la base para saber si esta todo ok. Si hay algo mal a nosotros nos devuelve un error
        
        serializer = HeroSerializer(data=request.data)
        
        # Si la informacion que estamos recibiendo del front es valida a traves del serializador, guarda la informacion
        if serializer.is_valid():
            serializer.save()
        
            data = {
                'mesage':'El heroe fue creado de forma correcta.'
            }
            
            return Response(
                data = data,
                status = status.HTTP_201_CREATED
            )
        
        return Response (
                data = serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
        ) """

# Derorador
# Debemos poner el tipo de metodo que maneja nuestra vista
        
@api_view(['GET'])
def hero_api_view(request):
    heroes = Hero.objects.all()
    heroes_serializer = HeroSerializer(heroes, many=True)


    return Response(
        data=heroes_serializer.data,
        status=status.HTTP_200_OK
        )    
            
class CreateHeroeApiView(APIView):
    def post(self,request):
        """ Crea un nuevo registro/heroe"""
        # print('Segundo post')
        # Agreando el many = True estamos indicandole que vamos a trabajar con muchos
        serializer = HeroSerializer(data=request.data, many = True)
        
        if serializer.is_valid():
            serializer.save()
        
            data = {
                'mesage':'El heroe fue creado de forma correcta.'
            }
            
            return Response(
                data = data,
                status = status.HTTP_201_CREATED
            )
        
        return Response (
                data = serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
        )
        
class HeroeDetailApiView(APIView):     
    
    # Necesitamos identificar al heroe
    def get(self,request, pk):
        """ Nos devuelve mas info de un heroe en particular """
        # Debemos modificar el ORM para que nos traiga un objeto en cuestion
        
        # Bloque 1  
        try:
            
            # El filter es un filtro general. me va a traer todos los registros que cumplan con esa cualidad. Como trabajamos con el id solo nos va a traer con esa coincidencia
            # heroes = Hero.objects.filter()
            
            # El get trae solo un valor. El primero de todos. Si no encuentra ese valor nos tira un error
            heroe = Hero.objects.get(id = pk)
            heroe_serializer = HeroSerializer(heroe)

            return Response(
                data=heroe_serializer.data,
                status=status.HTTP_200_OK
                )
        # Bloque 2   
        except:
            data = {
                'message' : 'El heroe no existe'
            }
            return Response(
                data = data,
                status = status.HTTP_400_BAD_REQUEST
            )
        
    def put(self,request, pk):
        """ Modifica un registro """
        validacion, heroe = hayHeroe(pk)
        # heroe = Hero.objects.get(id = pk)
        if validacion == True:
            heroe_serializer = HeroSerializer(heroe, data=request.data)
            
            # Como estamos modificando informacion hay que coloca una instacia de validacion
            if heroe_serializer.is_valid():
                heroe_serializer.save()
            
                data = {
                    'mesage':'El heroe fue modificado de forma correcta.'
                }

                return Response(
                    data=heroe_serializer.data,
                    status=status.HTTP_200_OK
                    )
            
        return Response(
            data=heroe_serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )
        
    def delete(self,request, pk):
        """ Elimina un registro """
        
        # Mucho cuidado con esto porque se elimina de la base de datos de forma permanenete
        heroe = Hero.objects.get(id = pk)
        heroe.delete()
        
        data ={
            'message':'El heroe fue eliminado de forma correcta'
        }
        
        return Response(
            data = data,
            status = status.HTTP_200_OK
        )


@api_view(['GET','PUT','DELETE'])
def hero_detail_api_view(request,pk):
    try: 
        heroe = Hero.objects.get(id = pk)
        
    except:
            data = {
                'message' : 'El heroe no existe'
            }
            return Response(
                data = data,
                status = status.HTTP_400_BAD_REQUEST
            )
    
    # Detail
    # El metodo que estamos solicitando la sacamos de la request
    # La request es un objeto que en ella conteniene la info que nos estan pasando, una serie de parametros y ademas el metodo que se esta solicitando
    # El metodo es lo que debemos obtener
    if request.method == 'GET':

        heroe_serializer = HeroSerializer(heroe)

        return Response(
            data=heroe_serializer.data,
            status=status.HTTP_200_OK
            )

    # Update
    elif request.method == 'PUT':

        heroe_serializer = HeroSerializer(heroe, data=request.data)
        
        if heroe_serializer.is_valid():
            heroe_serializer.save()
        
            data = {
                'mesage':'El heroe fue modificado de forma correcta.'
            }

            return Response(
                data=heroe_serializer.data,
                status=status.HTTP_200_OK
                )

    # Delete
    elif request.method == 'DELETE':

        heroe.delete()
        
        data ={
            'message':'El heroe fue eliminado de forma correcta'
        }
        
        return Response(
            data = data,
            status = status.HTTP_200_OK
        )
