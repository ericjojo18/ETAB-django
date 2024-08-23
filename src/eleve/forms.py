from django import forms


class StudentForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
    birth_date = forms.DateField()
    phone = forms.CharField(max_length=10)
    classrom = forms.CharField(max_length=10)
    registration_number = forms.CharField(max_length=30)
    
    
