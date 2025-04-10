from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['username', 'email', 'role', 'password', 'ni', 'name', 'area', 'cargo']
        extra_kwargs = {'password':{'write_only':True}}

    def create (self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
class ManagerSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Manager 
        fields = '__all__'
    
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data)
        manager = Manager.objects.create(user=user, **validated_data)
        return manager
    
class MaintainerSerializer(serializers.ModelSerializer):
    user = UserSerializer() 

    class Meta:
        model = Maintainer
        many = True
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data)
        maintainer = Maintainer.objects.create(user=user, **validated_data)
        return maintainer
    
class ResponsibleSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Responsible
        many = True
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data)
        responsible = Responsible.objects.create(user=user, **validated_data)
        return responsible
    
class EnvironmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Environment
        many = True
        fields = '__all__'

class PatrimonySerializer(serializers.ModelSerializer):

    class Meta:
        model = Patrimony
        many = True
        fields = '__all__'

class ServiceOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = ServiceOrder
        many = True
        fields = '__all__'