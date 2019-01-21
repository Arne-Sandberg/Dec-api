from rest_framework import serializers
from .models import Products, Stores

class ProductsSerializer(serializers.ModelSerializer):
    """serializer to map the Products model into JSON format"""

    class Meta:
        """Meta class to map the serializers fields with the Model fields"""
        model = Products
        fields = '__all__'
        read_only_fields = ('product_id','product_name')


class StoresSerializer(serializers.ModelSerializer):
    """serializer to map the Stroes model into JSON format"""
    class Meta:
        """Meta class to map the serialziers fields with the model fields"""
        model= Stores
        fields = ('store_id','store_name','store_city')
        read_only_fields = ('store_id', 'store_name')

    
