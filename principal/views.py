#Agregamos las librerias necesarias para la creacion de la api y para que funcione el proyecto
from django.shortcuts import render, redirect
from .models import Libro
from .serializers import LibroSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

# Create your views here.
#Funcion para ver la lista de libros
'''def principal(request):
	libro = Libro.objects.all()
	return render(request,'principal/biblioteca.html',{
		'libro':libro,
		})

#Creacion del libor, se trae los datos de la plantilla crear libros y lo creamos
def crearLibros(request):
	if request.method == 'POST':
		autor = request.POST['autor']
		titulo = request.POST['title']
		descripcion = request.POST['description']
		genero = request.POST['type']
		imagen = request.FILES['img']
		publicacion = request.POST['year_publication']
		libro = Libro.objects.create(titulo=titulo, descripcion=descripcion,publicacion=publicacion,
			imagen=imagen, genero=genero, autor=autor)
		return redirect('principal')
	return render(request,'principal/crearLibro.html')

#Editamos el libro por la informacion suministrada con el ID
def editarLibros(request,id_libro):
	libro= Libro.objects.get(id=id_libro)
	if request.method == 'POST':
		libro.autor = request.POST['autor']
		libro.titulo = request.POST['title']
		libro.descripcion = request.POST['description']
		libro.genero = request.POST['type']
		imagen = request.FILES['img'] or ""
		if imagen != "":
			libro.imagen = imagen
		if request.POST['year_publication'] != "":
			libro.publicacion = request.POST['year_publication']
		libro.save()
		return redirect('principal')
	return render(request,'principal/editarLibro.html',{'libro':libro})

#Si le das clic en eliminar se elimina el registro
def eliminarLibros(request,id_libro):
	libro= Libro.objects.get(id=id_libro)
	libro.delete()
	return redirect('principal')'''

"""@api_view(['GET','POST'])
def libro_list(request,format=None):
	if request.method == 'GET':
		libros = Libro.objects.all()
		serializer= LibroSerializer(libros, many = True)
		return JsonResponse({'libros': serializer.data})

	if request.method == 'POST':
		serializer = LibroSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET','PUT', 'DELETE']) 
def libro_detail(request,id,format=None):
   
    try:
        libro=Libro.objects.get(pk=id)
    except Libro.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LibroSerializer(libro)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = LibroSerializer(libro, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        libro.delete()
        return Response(status.HTTP_204_NO_CONTENT)"""

#Basado en la pagina https://www.django-rest-framework.org/api-guide/viewsets/#viewset
class LibroViewSet(viewsets.ModelViewSet): #Se crea funcion para la api, con solo esto al invocarla vamos a poder hacer todo
	queryset = Libro.objects.all()  #Colocamos como variable ya preescrita segun la documentacion y que nos mande la lista de todos los libros
	serializer_class = LibroSerializer #Serializer nos ayudara a colocor todo en json

	def get_queryset(self):
		genero = self.request.query_params.get('genero')
		fecha_inicio = self.request.query_params.get('fecha_inicio')
		fecha_fin = self.request.query_params.get('fecha_fin')
		
		if genero and fecha_inicio and fecha_fin:
			filtro = Libro.objects.filter(
            genero=genero,
            publicacion__range=(fecha_inicio, fecha_fin)
			)			
			
		return filtro