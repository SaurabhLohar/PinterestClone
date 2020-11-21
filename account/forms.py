from django.contrib.auth.forms import UserCreationForm, AuthenticationForm,UserChangeForm
from django.contrib.auth.models import User 
from django import forms


class UserRegisterForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username','email','password1','password2']

class UserChange(UserChangeForm):
	class Meta:
		model = User
		fields = ['first_name','last_name','email']