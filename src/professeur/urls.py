from django.urls import path
from professeur.views import index, add, update

app_name = "professeur"
urlpatterns = [ 
    path('',index, name="professeur"),
    path('ajouter_professeur',add, name="add"),
    path('modifier_professeur',update, name="update")
]
