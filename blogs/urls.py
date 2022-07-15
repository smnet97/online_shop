from django.urls import path
from .views import PostListView

app_name = 'blogs'

urlpatterns = [
    path('', PostListView.as_view(), name='posts')
]