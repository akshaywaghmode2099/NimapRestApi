from django.shortcuts import render
from rest_framework.decorators import api_view
# Create your views here.
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Client,Project, User
from .serializers import ClientSerializer,ClientwithallSerializer,ProjectSerializer,ProjectSerializer2


class ClientDetail(generics.RetrieveAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    lookup_field = 'id'


class ClientwithprojectDetail(generics.RetrieveAPIView):    
    queryset = Client.objects.all()
    serializer_class = ClientwithallSerializer
    lookup_field = 'id'


class ClientCreate(generics.CreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ClientUpdate(generics.RetrieveUpdateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    lookup_field = 'id'


class ClientDelete(generics.DestroyAPIView):
    queryset = Client.objects.all()

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
    


class ProjectDetail(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer2
    lookup_field = 'id'




