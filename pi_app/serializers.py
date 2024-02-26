from rest_framework import serializers, exceptions
from .models import Category,Products
from django.contrib.auth.models import User

class CategorySerializer(serializers.Serializer):
    name=serializers.CharField(max_length=50, min_length=4)
    id= serializers.IntegerField(read_only=True)



    def validate(self, attrs):
        name=attrs.get('name')
        if name== 'acid':
            raise exceptions.ValidationError('Please acid is not an accepted category')
        return attrs
    
    def create(self,validated_data):
        return Category.objects.create(name=validated_data['name'])
    
    def update(self, instance, validated_data):
        instance.name=validated_data.get('name', instance.name)
        instance.save()
        return instance
    
class CreateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Products
        fields=['name', 'description', 'price', 'discount_price','category','expired_date', 'production_date','rating','img']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Products
        fields=['id','name', 'description', 'category', 'expired_date', 'discount_price']     

class UserCreationSerializer(serializers.ModelSerializer):
    password=serializers.CharField(max_length=68, min_length=3, write_only=True)
    password2=serializers.CharField(max_length=68, min_length=3, write_only=True)
    class Meta:
        model= User
        fields=['username', 'email', 'password', 'password2']     
    
    def validate(self, attrs):
        user=User.objects.filter(username=attrs.get('username'))
        if user.exists():
            raise exceptions.ValidationError('username already exists, use a different username')
        password1=attrs.get('password')
        password2=attrs.get('password2')
        if password1 != password2:
            raise exceptions.ValidationError('password do not match')
        return super().validate(attrs)
    

    def create(self, validated_data):
        return User.objects.create_user(username=validated_data['username'], email=validated_data['email'], password=validated_data['password'])          