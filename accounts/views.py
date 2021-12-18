from django.shortcuts import render
from .forms import CustomUserCreationForms
from django.urls import reverse_lazy
from django.views.generic import CreateView

class SignUpView(CreateView):
    form_class = CustomUserCreationForms
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

# Create your views here.
