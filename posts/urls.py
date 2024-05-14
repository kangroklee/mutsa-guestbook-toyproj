from django.urls import path
from posts.views import *

urlpatterns = [
    path('', PostListAPIView.as_view()),
    path('<int:pk>/', PostDeleteAPIView.as_view())
]