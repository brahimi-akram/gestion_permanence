from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect
from .models import *
from .utils import *
from .forms import *

def trouver_permanence(request):
    if request.method=='GET':
        #create_holidays()
        tout_permaneneces=Permanence.objects.all()
        return render(request,"select_perma.html",{'perma':tout_permaneneces})
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
        return render(request,'add_permanence.html',{'forms':forms,'cadres':cadres})
    else:
        return JsonResponse( {"cc":permanence.nom})
    
# Create your views here.
