from django.urls import path,include
from . import views
from .views import ChangePasswordView
from knox import views as knox_views
urlpatterns = [
    path('login/',views.login_api),
    path('user/',views.get_user_data), 
    path('register/',views.register_api), 
    path('logout/',knox_views.LogoutView.as_view()),
    path('logoutall/',knox_views.LogoutAllView.as_view()),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
]
