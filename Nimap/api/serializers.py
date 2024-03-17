from rest_framework import serializers
from .models import Client, Project,User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'user_name']

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'project_name']

class ClientSerializer(serializers.ModelSerializer):
    # projects = ProjectSerializer(many=True, read_only=True)

    class Meta:
        model = Client
        fields = ['id', 'client_name', 'created_at', 'created_by', 'updated_at']

class ClientwithallSerializer(serializers.ModelSerializer):
    projects = ProjectSerializer(many=True, read_only=True)

    class Meta:
        model = Client
        fields = ['id', 'client_name','projects', 'created_at', 'created_by', 'updated_at']





class ProjectSerializer2(serializers.ModelSerializer):
    users = UserSerializer(many=True, read_only=True)
    # client = ClientSerializer(source='project', read_only=True)
    class Meta:
        model = Project
        fields = ['id', 'project_name','client', 'users','created_at', 'created_by']   #'client', 'users', 


class ProjectSerializer2(serializers.ModelSerializer):
    users = UserSerializer(many=True, read_only=True)
    # client = ClientSerializer(source='project', read_only=True)
    class Meta:
        model = Project
        fields = ['id', 'project_name','client', 'users','created_at', 'created_by']




















      
   
        


    
    
