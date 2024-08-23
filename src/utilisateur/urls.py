from django.urls import path
from utilisateur.views import index, add, update, login

app_name = "utilisateur"
urlpatterns = [
    path('',index, name="utilisateur"),
    path('ajouter_utilisateur',add, name="add"),
    path('modifier_utilisateur',update, name="update"),
    path('login',login)
]

