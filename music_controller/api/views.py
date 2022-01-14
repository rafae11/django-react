from django.shortcuts import render
from rest_framework import generics
from .serializers import RoomSerializer
from .models import Room

#generics.CreateAPIView can input parameters to save to the database
#generics.ListAPIView can show items in the database 

class RoomView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer