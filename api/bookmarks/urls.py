from django.urls import path
from . import views

app_name = 'bookmarks'

urlpatterns = [
    path('', views.BookmarkListCreateView.as_view(), name='bookmark-list-create'),
    path('<int:pk>/', views.BookmarkRetrieveUpdateDestory.as_view(), name='bookmark-detail'),
]