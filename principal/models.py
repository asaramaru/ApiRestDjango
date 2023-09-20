from django.db import models

# Create your models here.
#Creamos el modelo de la base de datos Libro
class Libro(models.Model):
	autor = models.CharField(max_length=100)
	titulo = models.CharField(max_length=50, unique=True)
	genero = models.CharField(max_length=200)
	descripcion = models.CharField(max_length=500)
	publicacion = models.DateField()
	created = models.DateTimeField(auto_now=True)
	updated = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = "libro"
		verbose_name_plural = "libros"

	def __str__(self):
		return self.titulo