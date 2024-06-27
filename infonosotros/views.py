from django.shortcuts import render
from django.http import HttpResponse
from .models import alumno
# Create your views here.k
def vista_alumnos(request):
    #Obtenemos la lista de objetos, es decir, los datos de la consulta
    alumnosia = alumno.objects.all()
    #Mandamos a llamar al archivo index.html
    return render(request, 'index.html', {
        'alumnos' : alumnosia
    })
    #Como tercer argumento mandamos un diccionario con las {}
    #Dentro de ese diccionario 'alumnos' es una variable que podemos pasarsela al html
    #alumnosia es la lista que le asignamos 'alumnos'