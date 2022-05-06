from django.urls import path
from .views import UserStory

urlpatterns = [
    path('',UserStory.as_view({'get':'list'}),name='story'),
]