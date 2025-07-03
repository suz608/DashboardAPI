from .models import Bookmark
from .serializers import BookmarkSerializer
from rest_framework import generics, permissions

class BookmarkListCreateView(generics.ListCreateAPIView):
    queryset = Bookmark.objects.all().order_by('-date_created')
    serializer_class = BookmarkSerializer
    permission_classes = [permissions.IsAuthenticated] 
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class BookmarkRetrieveUpdateDestory(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer
    lookup_field = "pk"
    permission_classes = [permissions.IsAuthenticated] 