from django.urls import path
from . import views

app_name = 'todos'

urlpatterns = [
    path('', views.TodoListCreateView.as_view(), name='bookmark-list-create'),
    path('<int:pk>/', views.TodoRetrieveUpdateDestroyView.as_view(), name='bookmark-detail'),
]