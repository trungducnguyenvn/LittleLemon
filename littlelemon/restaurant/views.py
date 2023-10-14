from django.shortcuts import render
from .models import Menu, BookingTable
from django.contrib.auth.models import User
from .serializers import MenuItemSerializer, BookingSerializer, UserSerializer

from rest_framework import status, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView 
from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated

# Create your views here.
def index(request):
    return render(request,'index.html', {})



@api_view(['GET', 'POST'])
def menu_item(request):
    items = Menu.objects.all()
    serialized_item = MenuItemSerializer(items, many=True)
    return Response(serialized_item.data)


class MenuItemView(ListAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer
    


class SingleMenuItem(RetrieveAPIView, DestroyAPIView,ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer



class BookingViewSet(viewsets.ModelViewSet):
    queryset = BookingTable.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


    # def get_permissions(self):
    #     permission_classes = []
    #     if self.request.method != 'GET':
    #         permission_classes = [IsAuthenticated]
        
    #     return [permission() for permission in permission_classes]



# authentication
@api_view()
@permission_classes([IsAuthenticated])
def secret_view(request):
    return Response({"message":"This view is protected"})









## class base view
# class BookList(APIView):
#     def get(self, request):
#         return Response({"message":"list of the bookings"}, status.HTTP_200_OK)
    
#     def post(self, request):
#         return Response({"message":"New booking added"}, status.HTTP_201_CREATED)
        

## class base view
# class Book(APIView):
#     def get(self, request, pk):
#         return Response({"message":"booking details " + str(pk)}, status.HTTP_200_OK)

#     def put(self, request, pk):
#         return Response({"booking_date":request.data.get('booking_date')}, status.HTTP_200_OK)