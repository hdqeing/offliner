from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegistrationForm

def index(request):
    return HttpResponse("Hello, welcome to the offliner app, a place for meet up with people offline")

def register_user(request):
    if request.method =='POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserRegistrationForm()
    return render(request=request, template_name='meetup/register.html', context={'register_form':form})

