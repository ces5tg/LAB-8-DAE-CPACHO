from .models import *
from rest_framework import serializers

class SerieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Serie
        fields = ('id', 'name', 'release_date', 'rating', 'category')


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model= Categoria
        fields = ('id', 'nombre', 'pub_date')

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Producto
        fields = ('id', 'categoria', 'nombre', 'precio', 'stock' ,'pub_date')


         

