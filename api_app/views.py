from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from .serializers import ProductsSerializer, StoresSerializer
from .models import Products,Stores
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

def index(request):
    return render(request, 'index.html')


# list products = get_all_objects -> serialize_into_json -> return response
# list stores = get_all_objects -> serialize_into_json -> return response
# list products at a store = get_particular_store(pk)-> get_product_objects_at_the_store -> serialize -> return response
# detail a store = get_particular_store(pk) -> serialize ->return response
# detail a product = get_particular_store(pk) -> get_partiular_product(pk) -> serialize and return resposne
# add a store : 



class StoresList(APIView):
    """API endpoint that allows stores to be viewed or edited"""  

    def get(self,request,format=None):
        stores = Stores.objects.all()
        serializer = StoresSerializer(stores, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StoresSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






class ProductList(APIView):
    """API endpoint that allows products to be viewed or edited"""

    def get(self,request,pk=None):
        if pk:
            prod = get_object_or_404(Products.objects.all(), pk=pk)
            serializer = ProductsSerializer(prod)
            return Response({"prod": serializer.data})
        products = Products.objects.all()
        serializer = ProductsSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



