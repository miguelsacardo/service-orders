from django.shortcuts import render

from api.serializers import UserSerializer, ManagerSerializer
from .models import *
from rest_framework.generics import ListCreateAPIView
from api.permissions import IsAdmin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


# this method can only be used by Authenticated Admin users
class UserRegistrationView(ListCreateAPIView):
    #  permission_classes = [IsAuthenticated, IsAdmin]
    # def post(self, request, *args, **kwargs):
    #     role = request.data.get('role')

    #     if role == 'admin':
    #         queryset = Manager.objects.all()
    #         serializer_class = ManagerSerializer
            
        
    def get_serializer_class(self):
        role = self.request.data.get('role')

        manager = Manager.objects.all()
        if role == 'admin':
            serializer_class = ManagerSerializer(manager).data
            return serializer_class
       
    # if User.role == 'admin':
    #     queryset = Admin.objects.all()
    #     serializer_class = AdminSerializer
    # def get_queryset(self):
    #     if self.request.user.role == 'admin':
    #         queryset = Manager.objects.all()
    #     return queryset
        
    # def get_serializer_class(self):
    #     if self.request.user.role == 'admin':
    #         manager = self.request.user.manager_account
    #         serializer_class = ManagerSerializer(manager).data
    #     return serializer_class
    


   
        

    
   
  
        




    
    



