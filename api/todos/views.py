from rest_framework import generics, permissions
from .models import Todo
from .serializers import TodoSerializer
from django.contrib.auth.decorators import login_required

class TodoListCreateView(generics.ListCreateAPIView):
    queryset = Todo.objects.all().order_by('-date_created')
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated] 

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class TodoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    lookup_field = "pk"
    permission_classes = [permissions.IsAuthenticated]