from rest_framework import serializers
from .models import User, Task

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['email']

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ['title', 'desc', 'deadline', 'is_done']

class TaskExecuteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ['is_done']

