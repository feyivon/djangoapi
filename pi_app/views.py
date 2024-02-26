from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, exceptions, permissions
from django.contrib.auth.models import User
from .serializers import CategorySerializer, ProductSerializer,CreateProductSerializer, UserCreationSerializer
from .serializers import Category,Products
from rest_framework import generics

# Create your views here.
class AddCategoryEndpoint(APIView):

    def get(self,request, *args, **kwargs):
        category=Category.objects.all()
        serializer=CategorySerializer(category, many=True)
        return Response(serializer.data, status.HTTP_200_OK)


    def post(self, request, *args, **kwargs):
        request.data
        serializer=CategorySerializer(data=request.data)
        if serializer.is_valid():#calls the validate method in our serializer
            serializer.save()#calls the create(post) or update(put) method depending on the request type
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class ProductEndpoint(APIView):
#     def get(self, request, *args, **kwargs):
#         products=Products.objects.all()
#         serializer= ProductSerializer(products, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def post(self, request, *args, **kwargs):
#         request.data    
#         serializer= CreateProductSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductListEndpoint(generics.ListAPIView):
    serializer_class=ProductSerializer
    queryset=Products.objects.all()

    def get_queryset(self):
        queryset=super().get_queryset()
        category=self.request.query_params.get('category')
        if category is not None:
            queryset=queryset.filter(category__name=category)
        return queryset    

class UpgradedProductEndpoint(generics.ListCreateAPIView):
    queryset=Products.objects.all()
    serializer_class=CreateProductSerializer

class SingleProductEndpoint(generics.RetrieveAPIView):
    queryset=Products.objects.all()
    serializer_class=CreateProductSerializer
    lookup_field='pk'    
    
class UpgradedCategoryEndpoint(generics.ListCreateAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer

class SingleCategoryEndpoint(generics.RetrieveAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    lookup_field='pk'

class CategoryDeleteEndpoint(generics.DestroyAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    lookup_field='pk'
    



class ProductDetailEndpoint(APIView):
    def get_object(self, pk):
        try:
            product=Products.objects.get(id=pk)
            return product
        except Products.DoesNotExist:
            raise exceptions.NotFound('Product does not exist')



    def get(self, request, *args, **kwargs):
        product=self.get_object(self.kwargs['product_id'])
        serializer=ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)   
    
    def put(self, request, *args, **kwargs):
        product=Products.objects.get(id=self.kwargs['product_id'])
        serializer=CreateProductSerializer(instance=product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, *args, **kwargs):
        product=Products.objects.get(id=self.kwargs['product_id'])
        product.delete()
        return Response({'message':'product deleted succesfully'}, status=status.HTTP_200_OK)
    
class UserRegisterEndpoint(generics.CreateAPIView):
    queryset=User.objects.all()
    permission_classes=[permissions.AllowAny]
    serializer_class=   UserCreationSerializer
