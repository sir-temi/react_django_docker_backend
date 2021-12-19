from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.http import HttpResponse, response
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import TodoList
from .serialisers import ListToDosSerializer


# def home():
#     return HttpResponse("<h1>You are welcome to this place --- DOCKER</h1>")


# @login_required(login_url='/account/login/')
# def dashboard(request):
#     return render(request, 'account/dashboard.html')


@api_view(['GET', 'POST'])
def add_todo(request):
    data = request.data
    try:
        data['save']
    except KeyError:
        return Response(int(data['result']) * 10 if str(data['result']).isdigit() else "This is not a number")
    else:
        TodoList.objects.create(
            work=data['result']
        )
        return Response(
            status=status.HTTP_201_CREATED
        )


@api_view(['GET'])
def get_todos(request):
    todos = TodoList.objects.all()
    serializer = ListToDosSerializer(todos, many=True)
    print(serializer.data)
    return Response(
        serializer.data,
        status=status.HTTP_200_OK,
    )


@api_view(['DELETE'])
def delete_todo(request, pk):
    todo = TodoList.objects.get(pk=pk)
    todo.delete()
    return Response(
        status=status.HTTP_200_OK
    )
