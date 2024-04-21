from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import SignupForm, funcform, setinterfaceform, changehostnameform, ospf_form, eigrp_form
from .functions import HostnameFunc, set_interface, changehostname, ospf, eigrp

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

#hostname view
def hostname(response):
    
    if response.method == 'POST':
        form = funcform(response.POST)
        if form.is_valid():
            router = form.cleaned_data['router']
            verification = form.cleaned_data['verification']
            job = HostnameFunc(router,verification)
            return HttpResponse(f'Job result : {job}')
    else:
        form = funcform()

    context={'form': form}
    return render(response,"hostname.html",context)

#set_interface view
def set_interface(response):
    if response.method == 'POST':
        form = setinterfaceform(response.POST)
        if form.is_valid():

            iprouter = form.cleaned_data['iprouter']
            interface = form.cleaned_data['interface']
            description = form.cleaned_data['description']
            network = form.cleaned_data['network']
            Masque = form.cleaned_data['Masque']

            job = set_interface(iprouter,interface,description,network,Masque)
            return HttpResponse(f'Job result : {job}')
    else:
        form = setinterfaceform()

    context={'form': form}
    return render(response,"set_interface.html",context)

#changehostname view
def changehostname(response):
    if response.method == 'POST':
        form = changehostnameform(response.POST)
        if form.is_valid():
            iprouter = form.cleaned_data['iprouter']
            hostname = form.cleaned_data['hostname']
            job = changehostname(iprouter,hostname)
            return HttpResponse(f'Job result : {job}')
    else:
        form = changehostnameform()

    context={'form': form}
    return render(response,"changehostname.html",context)

#ospf view
def ospf(response):
    if response.method == 'POST':
        form = ospf_form(response.POST)
        if form.is_valid():

            hostip = form.cleaned_data['hostip']
            ospfprocid = form.cleaned_data['ospfprocid']
            network_i = form.cleaned_data['network_i']
            area_id = form.cleaned_data['area_id']

            job = ospf(hostip,ospfprocid,network_i,area_id)
            return HttpResponse(f'Job result : {job}')
    else:
        form = ospf_form()

    context={'form': form}
    return render(response,"ospf.html",context)

#eigrp view
def eigrp(response):
    if response.method == 'POST':
        form = eigrp_form(response.POST)
        if form.is_valid():

            hostip = form.cleaned_data['hostip']
            eigrpprocid = form.cleaned_data['eigrpprocid']
            network_i = form.cleaned_data['network_i']

            job = eigrp(hostip,eigrpprocid,network_i)
            return HttpResponse(f'Job result : {job}')
    else:
        form = eigrp_form()

    context={'form': form}
    return render(response,"eigrp.html",context)

