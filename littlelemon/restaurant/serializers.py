from .models import Menu, BookingTable
from django.contrib.auth.models import User
from rest_framework import serializers



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email' , 'groups']


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['menu_id', 'title', 'price', 'inventory']


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingTable
        fields = '__all__'






# class MenuItemSerializer(serializers.Serializer):
#     menu_id = serializers.IntegerField()
#     title = serializers.CharField(max_length=255)