from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    # path('', home, name='home'),
    # path('dashboard/', dashboard, name='dashboard'),
    path('add_todo/', views.add_todo, name='add_todo'),
    path('gettodos/', views.get_todos, name='get_todos'),
    path('deletetodos/<int:pk>/', views.delete_todo, name='delete_todo')
]