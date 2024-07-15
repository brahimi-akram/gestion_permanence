from django.contrib import admin
from django.urls import path,include
from main import views

urlpatterns = [
    path('',views.trouver_permanence,name='trouver_permanenece'),
    path('add_affectation/<int:id>/',views.add_permanence,name='add_permanence')
]