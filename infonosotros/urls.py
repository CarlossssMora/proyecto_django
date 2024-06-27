from django.urls import path
from . import views
#Hacemos referencia al archivo views de la app
urlpatterns=[
    path('', views.vista_alumnos)
]