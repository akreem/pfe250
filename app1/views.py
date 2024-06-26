from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .forms import SignupForm, funcform, setinterfaceform, changehostnameform, ospf_form, eigrp_form, rip_form, L3VPNOSPF_form, L3VPNRIP_form,L3VPNEIGRP_form, creationvrf_form, clientrip_form, clientospf_form, resform,clienteigrp_form, deleteVRF_form, deleteRoutage_form
from .functions import HostnameFunc, set_interfaceFunc, changehostnameFunc, ospfFunc, eigrpFunc, rip_Func, vrfcreate, clientrip, clientospf, get_results, clienteigrp, supp_routage, supp_vrf
from django.contrib.auth.forms import PasswordChangeForm

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

# changepassword 
@login_required(login_url='login')
def changepassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important to update the session
            messages.success(request, 'Your password was successfully changed!')
            return redirect('/')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'changepassword.html', {'form': form})
    

# logout page
def user_logout(request):
    logout(request)
    return redirect('login')

#hostname view
@login_required(login_url='login')
def results(response):
    if response.method == 'POST':
        form = resform(response.POST)
        if form.is_valid():
            hostname = form.cleaned_data['router']
            job = get_results(hostname)
            #job = HostnameFunc(router,verification)
            return HttpResponse(f'Job result : {job}')
    else:
        form = resform()

    context={'form': form}
    return render(response,"results.html",context)

#set_interface view
@login_required(login_url='login')
def set_interface(response):
    if response.method == 'POST':
        form = setinterfaceform(response.POST)
        if form.is_valid():

            iprouter = form.cleaned_data['iprouter']
            interface = form.cleaned_data['interface']
            description = form.cleaned_data['description']
            network = form.cleaned_data['network']
            Masque = form.cleaned_data['Masque']

            job = set_interfaceFunc(iprouter,interface,description,network,Masque)
            return HttpResponse(f'Job result : {job}')
    else:
        form = setinterfaceform()

    context={'form': form}
    return render(response,"set_interface.html",context)

#changehostname view
@login_required(login_url='login')
def changehostname(response):
    if response.method == 'POST':
        form = changehostnameform(response.POST)
        if form.is_valid():
            iprouter = form.cleaned_data['iprouter']
            hostname = form.cleaned_data['hostname']
            job = changehostnameFunc(iprouter,hostname)
            return HttpResponse(f'Job result : {job}')
    else:
        form = changehostnameform()

    context={'form': form}
    return render(response,"changehostname.html",context)

#ospf view
@login_required(login_url='login')
def ospf(response):
    if response.method == 'POST':
        form = ospf_form(response.POST)
        if form.is_valid():

            hostip = form.cleaned_data['hostip']
            ospfprocid = form.cleaned_data['ospfprocid']
            network_i = form.cleaned_data['network_i']
            area_id = form.cleaned_data['area_id']

            job = ospfFunc(hostip,ospfprocid,network_i,area_id)
            return HttpResponse(f'Job result : {job}')
    else:
        form = ospf_form()

    context={'form': form}
    return render(response,"ospf.html",context)

#eigrp view
@login_required(login_url='login')
def eigrp(response):
    if response.method == 'POST':
        form = eigrp_form(response.POST)
        if form.is_valid():

            hostip = form.cleaned_data['hostip']
            eigrpprocid = form.cleaned_data['eigrpprocid']
            network_i = form.cleaned_data['network_i']

            job = eigrpFunc(hostip,eigrpprocid,network_i)
            return HttpResponse(f'Job result : {job}')
    else:
        form = eigrp_form()

    context={'form': form}
    return render(response,"eigrp.html",context)

#eigrp view
@login_required(login_url='login')
def rip(response):
    if response.method == 'POST':
        form = rip_form(response.POST)
        if form.is_valid():
            hostip = form.cleaned_data['hostip']
            network_i = form.cleaned_data['network_i']

            job = rip_Func(hostip,network_i)
            return HttpResponse(f'Job result : {job}')
    else:
        form = rip_form()

    context={'form': form}
    return render(response,"rip.html",context)


#l3vpn view
@login_required(login_url='login')
def l3vpn(response):
    if response.method == 'POST':
        form = rip_form(response.POST)
        if form.is_valid():
            hostip = form.cleaned_data['hostip']
            network_i = form.cleaned_data['network_i']

            job = rip_Func(hostip,network_i)
            return HttpResponse(f'Job result : {job}')
    else:
        form = rip_form()

    context={'form': form}
    return render(response,"rip.html",context)

#ospf_ospf view
@login_required(login_url='login')
def l3vpn_ospf(response):
    if response.method == 'POST':
        form = L3VPNOSPF_form(response.POST)
        if form.is_valid():
            return HttpResponse('Job result :')
    else:
        form = L3VPNOSPF_form()

    context={'form': form}
    return render(response,"L3VPNOSPF.html",context)


#rip_RIP view
@login_required(login_url='login')
def l3vpn_rip(response):
    if response.method == 'POST':
        form = L3VPNRIP_form(response.POST)
        if form.is_valid():
            return HttpResponse('Job result :')
    else:
        form = L3VPNRIP_form()

    context={'form': form}
    return render(response,"L3VPNRIP.html",context)

#eigrp_RIP view
@login_required(login_url='login')
def l3vpn_eigrp(response):
    if response.method == 'POST':
        form = L3VPNEIGRP_form(response.POST)
        if form.is_valid():
            return HttpResponse('Job result :')
    else:
        form = L3VPNEIGRP_form()

    context={'form': form}
    return render(response,"L3VPNEIGRP.html",context)

#creation_vrf view
@login_required(login_url='login')
def creation_vrf(response, client):
    if response.method == 'POST':
        form = creationvrf_form(response.POST)
        if form.is_valid():
            hostip = form.cleaned_data['hostip']
            vrf_id = form.cleaned_data['nom_vrf']
            rd_id = form.cleaned_data['rd']
            rt_id = form.cleaned_data['rt']
            interface = form.cleaned_data['interface_pe']
            ip_int = form.cleaned_data['adresse_ip_pe']
            masque = form.cleaned_data['masque']

            job = vrfcreate(hostip,vrf_id,rd_id,rt_id,interface,ip_int,masque)

            return HttpResponseRedirect(f'/client_{client}')
    else:
        form = creationvrf_form()

    context={'form': form, 'client': client.upper()}
    return render(response,"creationvrf.html",context)


#client_rip view
@login_required(login_url='login')
def client_rip(response):
    if response.method == 'POST':
        form = clientrip_form(response.POST)
        if form.is_valid():
            hostip = form.cleaned_data['hostip']
            vrf = form.cleaned_data['vrf']
            network_i = form.cleaned_data['network_i']
            
            job = clientrip(hostip,vrf,network_i)

            return HttpResponse(f'Job result :{job}')
    else:
        form = clientrip_form()

    context={'form': form}
    return render(response,"client_rip.html",context)

#client_ospf view
@login_required(login_url='login')
def client_ospf(response):
    if response.method == 'POST':
        form = clientospf_form(response.POST)
        if form.is_valid():
            hostip = form.cleaned_data['hostip']
            vrf = form.cleaned_data['vrf']
            network_i = form.cleaned_data['network_i']
            ospfprocid = form.cleaned_data['ospf_id']
            area_id = form.cleaned_data['area_id']
            
            job = clientospf(hostip,vrf,ospfprocid,network_i,area_id)

            return HttpResponse(f'Job result :{job}')
    else:
        form = clientospf_form()

    context={'form': form}
    return render(response,"client_ospf.html",context)

#client_eigrp view 
@login_required(login_url='login')
def client_eigrp(response):
    if response.method == 'POST':
        form = clienteigrp_form(response.POST)
        if form.is_valid():
            hostip = form.cleaned_data['hostip']
            vrf = form.cleaned_data['vrf']
            eigrpprocid = form.cleaned_data['eigrpprocid']
        
            job = clienteigrp(hostip,vrf,eigrpprocid)

            return HttpResponse(f'Job result :{job}')
    else:
        form = clienteigrp_form()

    context={'form': form}
    return render(response,"client_eigrp.html",context)


#delete_protocol view 
@login_required(login_url='login')
def delete_protocol(response):
    if response.method == 'POST':
        form = deleteRoutage_form(response.POST)
        if form.is_valid():
            hostip = form.cleaned_data['hostip']
            p = form.cleaned_data['protocol']

            job = supp_routage(hostip,p)

            return HttpResponse(f'Job result :{job}')
    else:
        form = deleteRoutage_form()

    context={'form': form}
    return render(response,"deleteroutage.html",context)


#delete_vrf view 
@login_required(login_url='login')
def delete_vrf(response):
    if response.method == 'POST':
        form = deleteVRF_form(response.POST)
        if form.is_valid():
            hostip = form.cleaned_data['hostip']
            vrf = form.cleaned_data['vrf']

            job = supp_vrf(hostip,vrf)

            return HttpResponse(f'Job result :{job}')
    else:
        form = deleteVRF_form()

    context={'form': form}
    return render(response,"deletevrf.html",context)



