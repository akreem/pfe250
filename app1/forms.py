from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    class Meta():
        model = User
        fields = ['username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        # Applying CSS classes to the fields
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder':'Username'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder':'Password'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder':'Confirm Pasword'})

class funcform(forms.Form):
    choices = (
        ('configuration','Running Configuration'),
        ('route','Route'),
        ('interfaces','Interfaces'),
        ('vrf','VRF'),
        ('protocols','Protocols')
    )
    router = forms.CharField(label="Router",max_length=50)
    verification = forms.ChoiceField(label="Verification", choices=choices)
    def __init__(self, *args, **kwargs):
        super(funcform, self).__init__(*args, **kwargs)
        # Applying CSS classes to the fields
        self.fields['router'].widget.attrs.update({'class': 'form-control'})
        self.fields['verification'].widget.attrs.update({'class': 'form-control'})

class setinterfaceform(forms.Form):
    iprouter = forms.CharField(label="iprouter",max_length=50)
    interface = forms.CharField(label="interface",max_length=50)
    description = forms.CharField(label="description",max_length=50) 
    network = forms.CharField(label="network",max_length=50)
    Masque = forms.CharField(label="Masque",max_length=50)
    def __init__(self, *args, **kwargs):
        super(setinterfaceform, self).__init__(*args, **kwargs)
        # Applying CSS classes to the fields
        self.fields['iprouter'].widget.attrs.update({'class': 'form-control'})
        self.fields['interface'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'class': 'form-control'})
        self.fields['network'].widget.attrs.update({'class': 'form-control'})
        self.fields['Masque'].widget.attrs.update({'class': 'form-control'})

class changehostnameform(forms.Form):
    iprouter = forms.CharField(label="iprouter",max_length=50)
    hostname = forms.CharField(label="hostname",max_length=50)
    def __init__(self, *args, **kwargs):
        super(changehostnameform, self).__init__(*args, **kwargs)
        # Applying CSS classes to the fields
        self.fields['iprouter'].widget.attrs.update({'class': 'form-control'})
        self.fields['hostname'].widget.attrs.update({'class': 'form-control'})

class ospf_form(forms.Form):
    hostip = forms.CharField(label="hostip",max_length=50)
    ospfprocid = forms.CharField(label="ospfprocid",max_length=50)
    network_i = forms.CharField(label="network_i",max_length=50) 
    area_id = forms.CharField(label="area_id",max_length=50)
    def __init__(self, *args, **kwargs):
        super(ospf_form, self).__init__(*args, **kwargs)
        # Applying CSS classes to the fields
        self.fields['hostip'].widget.attrs.update({'class': 'form-control'})
        self.fields['ospfprocid'].widget.attrs.update({'class': 'form-control'})
        self.fields['network_i'].widget.attrs.update({'class': 'form-control'})
        self.fields['area_id'].widget.attrs.update({'class': 'form-control'})
        

class eigrp_form(forms.Form):
    hostip = forms.CharField(label="hostip",max_length=50)
    eigrpprocid = forms.CharField(label="eigrpprocid",max_length=50)
    network_i = forms.CharField(label="network_i",max_length=50)
    def __init__(self, *args, **kwargs):
        super(eigrp_form, self).__init__(*args, **kwargs)
        # Applying CSS classes to the fields
        self.fields['hostip'].widget.attrs.update({'class': 'form-control'})
        self.fields['eigrpprocid'].widget.attrs.update({'class': 'form-control'})
        self.fields['network_i'].widget.attrs.update({'class': 'form-control'})


class rip_form(forms.Form):
    hostip = forms.CharField(label="hostip",max_length=50)
    network_i = forms.CharField(label="network_i",max_length=50)
    def __init__(self, *args, **kwargs):
        super(rip_form, self).__init__(*args, **kwargs)
        # Applying CSS classes to the fields
        self.fields['hostip'].widget.attrs.update({'class': 'form-control'})
        self.fields['network_i'].widget.attrs.update({'class': 'form-control'})