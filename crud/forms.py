from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,PasswordChangeForm,PasswordResetForm,SetPasswordForm
from django.contrib.auth.models import User
from django.utils.translation import gettext,gettext_lazy  as _
from django.contrib.auth import password_validation
from .models import Task

class PositionForm(forms.Form):
    position = forms.CharField()



class CustomerRegistrationsForms(UserCreationForm):
    password1 = forms.CharField( label='password:',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField( label='confirm password(again):',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email = forms.CharField( label='Email:',required=True,widget=forms.EmailInput(attrs={'class':'form-control'}))
    # phone_number=forms.CharField(label='phone number:',widget=forms.IntegerField(attrs={'class':'form-control'}))
    phone_number=forms.CharField(label = "Phone Number:",max_length=10)
    profile_image=forms.ImageField(label='Photo', required=False)
    


    class Meta:
        model = User
        fields=['username','email','password1','password2','phone_number','profile_image']

            
    def __init__(self,*args,**kwargs) :
        super(CustomerRegistrationsForms,self).__init__(*args,**kwargs)   
        self.fields['phone_number'].widget.attrs['class']='form-control'
        self.fields['username'].widget.attrs['class']='form-control'
        


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'})) 
    password = forms.CharField(label=_("Password"),widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))       
