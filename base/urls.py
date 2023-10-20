
from django.urls import path, include
from .views import HomeView
from django.views.generic import RedirectView


urlpatterns = [
    path('', RedirectView.as_view(pattern_name='account_login')),
    path('home/', HomeView.as_view(), name='home'),
]