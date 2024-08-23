from django import forms
from .models import User

class UserForm(forms.Form):
    pseudo = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30)
    creat_at = forms.DateTimeField()


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['pseudo', 'password',]
        
       # exclude = ['creat_at']
        