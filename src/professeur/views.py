from django.shortcuts import render
from .forms import TeacherForm

# Create your views here.

def index(request):
    return render(request, "professeur/index.html")

def add(request):
    form = TeacherForm()
    content = {'Form': form}
    return render(request,"professeur/ajout_prof.html", content )

def update(request):
    return render(request, "professeur/modif_prof.html")