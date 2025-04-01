from django.shortcuts import render

from api.serializers import UserSerializer
from .models import *
from rest_framework.generics import ListCreateAPIView
# from django.contrib.auth import authenticate, login
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework.authtoken.models import Token
# from rest_framework.permissions import IsAuthenticated



class UserRegistrationView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # afterward, here will be the permission_classes
    



