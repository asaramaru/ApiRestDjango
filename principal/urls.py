from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

'''app_name = "libros"

urlpatterns = [
    path('biblioteca/', views.principal, name='principal'),
    path('crearLibro/', views.crearLibros, name='crearLibros'),
    path('editarLibros/<id_libro>/', views.editarLibros, name='editarLibros'),
    path('eliminarLibros/<id_libro>/', views.eliminarLibros, name='eliminarLibros'),
    path("libros/", views.libro_list),
    path('libros/<id>',views.libro_detail),
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)'''

router = routers.DefaultRouter() #Treamos la funcion rutas por defecto para que podamos interactuar con la api
router.register(r'libros',views.LibroViewSet) 
'''Registramos en una url lo que buscamos en ese caso solo es libros y la r la mandamos para que se 
pueda interactuar de varias formas con la url, por ejemplo poder mandar un libros/1 para poder editar y que nos encuentre el registro''' 

urlpatterns = [
    path('',include(router.urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
#Incluimos las rutas