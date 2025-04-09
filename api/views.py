from django.shortcuts import render

from api.serializers import *
from .models import *
from rest_framework.generics import ListCreateAPIView
from api.permissions import IsAdmin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


# this method can only be used by Authenticated Admin users
class UserRegistrationView(ListCreateAPIView):
    
    # return all users for listing (GET) -> the logic of creation can't be here
    queryset = User.objects.all() 

    # choose the serializer that will be used based in user role informed in request
    def get_serializer_class(self):
        user = self.request.data.get('user')
        
        if user['role'] == 'admin':
            return ManagerSerializer
        elif user['role'] == 'manutentor':
            return MaintainerSerializer
        return UserSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid()
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

    


   
        

    
   
  
        




    
    



