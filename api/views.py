from django.shortcuts import render, get_object_or_404

from api.serializers import *
from .models import *
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from api.permissions import IsAdmin
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status


# this method can only be used by Authenticated Admin users
# user creation and listing
class UserRegistrationView(ListCreateAPIView):
    
    # return all users for listing (GET) -> the logic of creation can't be here
    def get_queryset(self):
        return User.objects.all()

    # choose the serializer that will be used based in user role informed in request
    def get_serializer_class(self):
        user = self.request.data.get('user')
        
        if user == None:
            return UserSerializer
        elif user['role'] == 'admin':
            return ManagerSerializer
        elif user['role'] == 'manutentor':
            return MaintainerSerializer
        elif user['role'] == 'user':
            return ResponsibleSerializer
        return UserSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid()
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class UserDetailView(RetrieveUpdateDestroyAPIView):
    
    permission_classes = [AllowAny]

    queryset = User.objects.all()
    lookup_field = "userId" 
    # by default, queryset search for an attribute 'pk' in url, so to make it use 'userId,
    # i use the lookup_field
    

    def patch(self, request, userId):
        user = get_object_or_404(User, userId=userId)
        
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# environment
class EnvironmentRegistrationView(ListCreateAPIView):
    permission_classes = [AllowAny]

    queryset = Environment.objects.all()
    serializer_class = EnvironmentSerializer

class EnvironmentDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]

    queryset = Environment.objects.all()
    serializer_class = EnvironmentSerializer

# patrimony
class PatrimonyRegistrationView(ListCreateAPIView):
    permission_classes = [AllowAny]

    queryset = Patrimony.objects.all()
    serializer_class = PatrimonySerializer

class PatrimonyDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]

    queryset = Patrimony.objects.all()
    serializer_class = PatrimonySerializer

# service orders
class ServiceOrderRegistrationView(ListCreateAPIView):
    permission_classes = [AllowAny]

    queryset = ServiceOrder.objects.all()
    serializer_class = ServiceOrderSerializer

class ServiceOrderDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]

    queryset = ServiceOrder.objects.all()
    serializer_class = ServiceOrderSerializer
        
    

    


   
        

    
   
  
        




    
    



