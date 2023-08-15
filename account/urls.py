from django.urls import path
from rest_framework.authtoken.views import ObtainAuthToken

from .views import UserRegisterView, LogoutView

urlpatterns = [
    path('register-user/', UserRegisterView.as_view()),
    path('login/', ObtainAuthToken.as_view()),
    path('logout/', LogoutView.as_view(), name='logout'),
]