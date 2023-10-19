from django.shortcuts import render
from django.views.generic import TemplateView 
from django.http.response import HttpResponse
from django.contrib.auth.models import User

class LoginView(TemplateView):

    template_name = 'login.html'

def login(request):
    return render(request, 'login.html')
class HomeView(TemplateView):

    template_name = 'home.html'

class RegisterView(TemplateView):

    template_name = 'register.html'

    def register(request):
        if request.method == 'GET':
            return render(request, 'register.html')



