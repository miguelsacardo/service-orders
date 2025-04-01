from django.shortcuts import render

from api.serializers import UserSerializer
from .models import *
from rest_framework.generics import ListCreateAPIView
from api.permissions import IsAdmin
from rest_framework.permissions import IsAuthenticated


# this method can only be used by Authenticated Admin users
class UserRegistrationView(ListCreateAPIView):
    permission_classes = [IsAuthenticated, IsAdmin]
    queryset = User.objects.all()
    serializer_class = UserSerializer
  
        




    
    



