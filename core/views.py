from django.shortcuts import render

# Importamos el Modelo=Tabla
from .models  import Discos
# Importamos el archivo serializers datos nativos
from .serializers import discos_serializer

# Importamos la restframework se encarga de convertir a JSON
from rest_framework import generics

class DiscosAllViewset(generics.ListAPIView):
    #select * from discos
    queryset = Discos.objects.all()
    serializer_class = discos_serializer



    
