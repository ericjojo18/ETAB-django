from django.urls import path
from eleve.views import index, add, update

#nom de notre application dans l'url (localhost:8000/eleve/) par la variable app_name
app_name = "eleve"

urlpatterns = [
    path("", index, name="eleve"),
    
    path("ajout_eleve", add, name="add"),
    path("modif_eleve", update, name="update")
]