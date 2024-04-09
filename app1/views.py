from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import SignupForm

# Create your views here.
@login_required(login_url='login')
def home(request):
    return render(request, "home.html")

# signup page
def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        if request.user.is_authenticated:
            return HttpResponseRedirect('/')
        else:
            form = SignupForm()
            return render(request, 'signup.html', {'form': form})


# login page
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)    
            return HttpResponseRedirect('/')
        else:
            messages.success(request, ("Username or Password is incorrect"))
            return HttpResponseRedirect('/login')  
    else:
        if request.user.is_authenticated:
            return HttpResponseRedirect('/')
        else:
            return render(request, 'login.html')
    

# logout page
def user_logout(request):
    logout(request)
    return redirect('login')