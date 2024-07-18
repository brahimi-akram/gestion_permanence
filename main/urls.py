
from django.contrib import admin
from django.urls import path,include
from main import views
urlpatterns = [
    path ('', views.home, name = 'home'),
    path ('ajouter_cader/', views.ajouter_cader, name = 'ajouter cadre'),
    path ('afficher_liste/', views.afficher_liste, name = 'afficher liste'),
    path ('modifier_cader/<int:id>/', views.modifier_cadre, name = 'modifier cadre'),
    path ('masque_cadre/<int:id>/', views.masque_cadre, name = 'masque cadre'),
    path ('desmasque_cadre/ <int:id>', views.desmasque_cadre, name ='desmasque cadre'),
    path ('importer_de_excel/', views.importer_de_excel,  name = 'importer de excel'),
    path('trouver_permanence/',views.trouver_permanence, name='trouver permanence'),
    path('add_affectation/<int:id>/',views.add_permanence, name='add permanence'),
    path('afficher_affectation/', views.afficher_affectation, name ='afficher affectation'),
]
