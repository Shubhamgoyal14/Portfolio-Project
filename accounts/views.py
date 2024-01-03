# views.py
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth import authenticate
from django.contrib import messages
#from django.contrib.auth.forms import UserCreationForm 
def Home(request):
    return render(request, 'project_index.html')
def register(request):
    form = RegisterForm()
    if request.method=="POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You're Successfully Registered! ")
            # index_link = '<a href="/"><h3>Return to Homepage</h3></a>'
            # content = '<h1>User has been created successfully!</h1>'
            # full_content = content + index_link
            return redirect(login)
    context={
        'form':form
    }
    return render(request, 'register.html', context)

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponse

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)  # Pass the user object to the login function
            messages.success(request, "You're logged in successfully!")
            return redirect('/')  # Replace 'register/' with the desired URL
        else:
            return HttpResponse("Username or Password is incorrect!")

    # If the request method is not POST, render the login form
    return render(request, 'login.html')

  