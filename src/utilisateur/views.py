from django.shortcuts import render
from .forms import UserForm

# Create your views here.

def index(request):
    return render(request,"utilisateur/index.html")

def add(request):
    
    if request.method == 'POST':
        #print(request.POST)
        
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            print(user_form.cleaned_data)
            user_form.save()
        
        
    user_form = UserForm()
    context = {'user_form':user_form}
    return render(request, "utilisateur/ajout_user.html", context)

def update(request):
    return render(request, "utilisateur/modif_user.html")
def login(request):
    return render(request,"utilisateur/login.html")