from rest_framework import serializers
from .models import TodoList

class ListToDosSerializer(serializers.ModelSerializer):

    class Meta:
        model = TodoList
        fields = ['pk','work']