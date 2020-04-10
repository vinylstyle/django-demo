from rest_framework import serializers
from api_todo.models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'created', 'title', 'description']