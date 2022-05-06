from django.urls import path
from .views import Profiles

urlpatterns = [
    path('profile/',Profiles.as_view({"get":"list",}),name='profiles'),
]