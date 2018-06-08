from django import forms

class LoginForm(forms.Form):
	username = forms.CharField(label='User Name', max_length=64)
	password = forms.CharField(widget=forms.PasswordInput())

class SignupForm(forms.Form):
    username = forms.CharField(label="User Name", max_length=64)
    email = forms.EmailField(max_length=200, help_text='Required')
    password = forms.CharField(widget=forms.PasswordInput())

