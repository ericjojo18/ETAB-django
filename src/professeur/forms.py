from django import forms

class TeacherForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
    birth_date = forms.DateField()
    phone = forms.CharField(max_length=10)
    is_vacant = forms.BooleanField()
    matter = forms.CharField(max_length=30)
    next_class = forms.CharField(max_length=30)
    subject_next_meeting = forms.CharField(max_length=100)