from django.urls import path
from api_todo import views

urlpatterns = [
    path('todos/', views.todo_list),
    path('todos/<int:pk>/', views.todo_detail),
]