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
        ('Running Configuration','Running Configuration'),
        ('Route','Route'),
        ('Interfaces','Interfaces'),
        ('VRF','VRF'),
        ('Protocols','Protocols')
    )
    router = forms.CharField(label="router",max_length=50)
    verification = forms.MultipleChoiceField(label="verification", choices=choices, widget=forms.CheckboxSelectMultiple)
            