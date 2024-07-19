
from django.forms import formset_factory
from django.http import HttpResponse, JsonResponse
from django.urls import reverse
import pandas as pd
from django.shortcuts import  get_object_or_404, render, redirect
from .forms import *
from .models import *
from datetime import datetime
from .utils import *
from itertools import groupby
from operator import attrgetter


# Create your views here.
def ajouter_cader (request):
    if request.method == 'GET':
        return render (request, 'ajouter_cader.html')
    if request.method == 'POST':
        
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        poste = request.POST.get('poste')
        email = request.POST.get('email')
        
        if nom and prenom and poste and email : 
            Cadre.objects.create (nom = nom, prenom=prenom, poste = poste, email= email)
            return render(request, 'ajouter_cader.html')
       
    return render(request, 'ajouter_cader.html')
 
 
def afficher_liste (request) :
    if request.method == 'GET':
        filter_param = request.GET.get('filter')
    
        emails = Cadre.objects.filter(active=True).values_list('email', flat=True)
        email_list = ','.join(emails)
        if filter_param == 'inactive':
            cadres = Cadre.objects.filter(active=False)
            return render(request, 'afficher_liste.html', {'cadres': cadres, 'email_list': email_list})

        else :
            cadres = Cadre.objects.filter(active=True)
            return render(request, 'afficher_liste.html', {'cadres': cadres, 'email_list': email_list})
        
    elif request.method == 'POST':
        if 'excel_file' in request.FILES:
            excel_file = request.FILES['excel_file']
            df = pd.read_excel(excel_file)
            
            for index, row in df.iterrows():
                Cadre.objects.create(
                    nom=row['nom'],
                    prenom=row['prenom'],
                    poste=row['poste'],
                    email=row['email']
                )
            
            return redirect(afficher_liste)  # Rediriger vers la vue 'afficher_liste' après l'importation
        
         



def modifier_cadre (request, id ):
    if request.method == 'GET':
        cadre = Cadre.objects.get(pk = id)
        return render(request, 'modifier_cadre.html', {'cadre' : cadre})
    else:
       
        cadre = Cadre.objects.get(pk = id)
        nom = request.POST.get('nom')
        prenom = request.POST.get('prenom')
        poste = request.POST.get('poste')
        email = request.POST.get('email')
        if nom and prenom and poste and email : 
            cadre.nom = nom
            cadre.prenom = prenom
            cadre.poste = poste
            cadre.email = email
            cadre.save()
    return redirect (afficher_liste) 



def masque_cadre (request, id):
    if request.method == 'GET':
        cadre = Cadre.objects.get(pk = id )
        cadre.active = False
        cadre.save()
        return redirect(afficher_liste)



def desmasque_cadre (request, id):
    if request.method == 'GET':
        cadre = Cadre.objects.get(pk = id )
        cadre.active = True
        cadre.save()
        return redirect(reverse('afficher liste') + '?filter=inactive')


    
def home (request):
    
    return render(request, 'home.html')




def importer_de_excel(request):
    if request.method == 'POST':
        excel_file = request.FILES['excel_file']
        df = pd.read_excel(excel_file)
        
        for index, row in df.iterrows():
            Cadre.objects.create(
                nom=row['Nom'],
                prenom=row['Prénom'],
                poste=row['Poste'],
                email=row['Email']
            )
        
        employees = Cadre.objects.all()
        return render(request, 'afficher_liste.html ', {'df': df})
    return render(request, 'afficher_liste.html')


def trouver_permanence(request):
    if request.method=='GET':
        
        #create_holidays()
        
        tout_permaneneces=Permanence.objects.all().order_by('date_debut')
        return render(request,"trouver_permanence.html",{'perma':tout_permaneneces})
    else:
        perma_id=request.POST.get('perma_id')
        permanence=Permanence.objects.get(pk=perma_id)
        permanence.nombre_cadre=int(request.POST.get('numWorkers'))
        permanence.save()
        return redirect(add_permanence,perma_id)
    
    
def add_permanence(request,id):
    permanence=Permanence.objects.get(pk=id)
    if request.method=='GET':
        forms=[]
        forms=[(nombre+1,AffectationForm()) for nombre in range(0,permanence.nombre_cadre)]
        cadres=Cadre.objects.all()
        #for nombre in range(0, permanence.nombre_cadre):
            #forms.append(nombre+1)
            #forms.append(AffectationForm())
        return render(request,'add_permanence.html',{'forms':forms,'cadres':cadres})
    else:
        print(request.POST)
        for i in range (0, permanence.nombre_cadre):
            afffectation = Affectation()
            afffectation.cadre = Cadre.objects.get(pk = request.POST.get(f'worker_{i+1}'))
            afffectation.permanence = permanence
            afffectation.heure_debut = datetime.strptime(request.POST.getlist('heure_debut')[i], '%H:%M').time()
            afffectation.heure_fin = datetime.strptime(request.POST.getlist('heure_fin')[i], '%H:%M').time()
            afffectation.save()
            
            
            print(request.POST)
        return redirect(trouver_permanence)



def afficher_affectation(request):
    month_names = {
        "1": "جانفي", "2": "فيفري", "3": "مارس", "4": "أفريل",
        "5": "ماي", "6": "جوان", "7": "جويلية", "8": "أوت",
        "9": "سبتمبر", "10": "أكتوبر", "11": "نوفمبر", "12": "ديسمبر"
    }

    if request.method == 'POST':
        month = request.POST.get('month')
        year = request.POST.get('year')
    else:  
        month = request.GET.get('month')
        year = request.GET.get('year')

    current_year = datetime.now().year
    years = range(current_year - 10, current_year + 10)  # Example of year range
    
    permanences = Permanence.objects.filter(date_debut__month=month, date_debut__year=year).order_by('date_debut')
    
    grouped_affectations = {}
    for perma in permanences :
        grouped_affectations[perma] = Affectation.objects.filter(permanence = perma)
        
    month_name = month_names.get(month, "")  # Get the month name from the dictionary
    context = {
        'years': years,
        'grouped_affectations': grouped_affectations,
        'selected_month': month_name,  # Use the month name
        'selected_year': year, 
        
    }
    return render(request, 'afficher_affectation.html', context)


