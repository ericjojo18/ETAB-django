from django.shortcuts import render
from .forms import StudentForm

# Create your views here.


def index(request):
    return render(request, "eleve/index.html")

def add(request):
    form = StudentForm()
    context = {'Form': form}
    return render(request, "eleve/ajout_eleve.html", context )

def update(request):
    return render(request, "eleve/modif_eleve.html")


