from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from .serializer import UserModelSerializer
from rest_framework.response import Response
from django.contrib.auth import get_user_model
User = get_user_model

class UserModelViewSet (viewsets.ModelViewSet):
    queryset = User.objects.all ()
    serializer_class = UserModelSerializer 

    def get (self):
        user = User.objects.all ()
        serializer = UserModelSerializer (user, many=True)
        return Response (serializer.data)
    
    def post (self,request):
        serializer= UserModelSerializer (data=request.data)
        if serializer.is_valid():
            serializer.save ()
            return Response(serializer.data ,status=status.HTTP_201_CREATED)
        else:
            return Response (serializer.data,status=status.HTTP_204_NO_CONTENT)

    def permissions (self):
        if self.action in ['create']:
            return [permissions.AllowAny()]
        elif self.action in ['destroy','list']:
            return [permissions.IsAdminUser()]
        else:
            return [permissions.IsAdminUser()],[permissions.IsAuthenticated()]




