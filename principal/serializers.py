from rest_framework import serializers
from .models import Libro

class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = ['id','autor','titulo','genero','descripcion','publicacion']

#En esta parte estamos recogiendo todo lo que vamos a mostrar en la api y con ellos guiarnos para la creacion del libro