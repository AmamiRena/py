from django.shortcuts import render,redirect

# Create your views here.
from django.contrib.auth import login
from django.views.generic import CreateView
from .models import User
from .forms import SignUpForm

class UserSignupView(CreateView):
    model=User
    form_class=SignUpForm
    template_name='authentication/signup.html'
    def form_valid(self,form):
        user=form.save()
        login(self.request,user)
        return redirect('home')
