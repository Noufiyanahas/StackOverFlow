from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from api.serializers import UserSerializer
from rest_framework.response import Response


# Create your views here.
class UserView(ViewSet):
    def create(self,request,*args,**kwargs):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
