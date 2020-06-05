from django import forms
from django.contrib.auth.forms import AuthenticationForm,UsernameField,UserCreationForm
from django.contrib.auth.models import User


class Loginform(forms.Form):
    username=UsernameField(widget=forms.TextInput(attrs={'autofocus': True,'class':'form-input','id':'email','placeholder':"Username"}))
    password=forms.CharField(
        #label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password','id':'password','class':'form-input','placeholder':'Password'}),
    )

topics=[
        ('Business','Business'),
        ('Sports','Sports'),
        ('Technology','Technology'),
        ('Entertainment','Entertainment'),

]
    
class new_user(UserCreationForm):
    email=forms.EmailField(widget=forms.EmailInput(attrs={'id':'email','class':'form-input','placeholder':'Email id'}))
    topics2=forms.MultipleChoiceField(choices=topics)
    

    class Meta:

        model=User

        fields=['username','email','password1','password2','topics2']

    def __init__(self,*args,**kwargs):
        super(new_user,self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-input'
        self.fields['username'].widget.attrs['id'] = 'name'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['password1'].widget.attrs['class'] = 'form-input'
        self.fields['password1'].widget.attrs['id'] = 'password'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['class'] = 'form-input'
        self.fields['password2'].widget.attrs['id'] = 'password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        






# class myUserCreationForm(UserCreationForm):

# class Meta:
#     model=User
#     fields = ('username', 'password1', 'password2')

# def __init__(self, *args, **kwargs):
#     super(myUserCreationForm, self).__init__(*args, **kwargs)

#     self.fields['username'].widget.attrs['class'] = 'form-control'
#     self.fields['password1'].widget.attrs['class'] = 'form-control'
#     self.fields['password2'].widget.attrs['class'] = 'form-control'







# class new_user(UserCreationForm):
#     email=forms.EmailField()
#     date_of_birth=forms.DateField()
#     GENDER=[('Male','Male'),('Female','Female'),]
#     Gender = forms.ChoiceField(choices=GENDER, widget=forms.RadioSelect)
#     #Name=models.CharField(max_length=100)
#     Name=forms.CharField(max_length=100)

#     class Meta:
#         model=User
#         fields=['username','Gender','email','date_of_birth','password1','password2']
