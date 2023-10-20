from django.shortcuts import render
from django.views.generic import TemplateView 
from django.http.response import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.models import User

class HomeView(TemplateView):
    #login_url = reverse_lazy('account_login')
    template_name = 'home.html'



