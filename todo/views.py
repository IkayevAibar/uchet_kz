from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from rest_framework.decorators import action

from todo.models import Task, User
from .serializers import UserSerializer, TaskSerializer, TaskExecuteSerializer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from todo import serializers

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    


class TasksViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Tasks to be viewed or edited.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.AllowAny]

    @action(detail=True, methods=['Post'], name='execute')
    def execute(self, request, *args, **kwargs):
        task = self.get_object()
        
        serializer = TaskExecuteSerializer(data=request.data)
        if serializer.is_valid():
            task.is_done = serializer.validated_data['is_done']
            task.save()
            return Response({'status': 'updated'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

