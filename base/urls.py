from django.contrib import admin
from django.urls import path, include
from .views import LoginView, HomeView, RegisterView

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('home/', HomeView.as_view(), name='home'),
    path('registrar/', RegisterView.as_view(), name='register'),
]