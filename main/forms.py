from .models import *
from django import forms

class PermanenceForm(forms.ModelForm):
    class Meta:
        model = Permanence
        fields = ['nom', 'date_debut','description','nombre_cadre']
        labels = {
            'date_debut':'التاريخ',
            'nom': 'الاسم',
            'description':'مناسبة',
            'nombre_cadre':'عدد العمال' ,
        }

class AffectationForm(forms.ModelForm):
    class Meta:
        model = Affectation
        fields =['heure_debut','heure_fin']
        labels ={
            'heure_debut':'بداية المداومة',
            'heure_fin':'نهاية المداومة'
        }
        widgets = {
            'heure_debut': forms.TimeInput(format='%H:%M', attrs={'type': 'time'}),
            'heure_fin': forms.TimeInput(format='%H:%M', attrs={'type': 'time'})
        }