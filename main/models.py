from django.db import models
from datetime import datetime, timedelta
# Create your models here.
class Cadre (models.Model):
    id = models.AutoField(primary_key= True)
    nom = models.CharField(max_length= 40)
    prenom = models.CharField(max_length = 40)
    poste = models.CharField(max_length= 60)
    email = models.EmailField(unique= True , max_length= 100)
    active = models.BooleanField(default = True)
    def __str__(self) :
        return f'{self.nom} {self.prenom}'
    
class Permanence (models.Model) :
    id = models.AutoField(primary_key = True)
    date_debut = models.DateField(unique = True)
    nom = models.CharField(max_length= 60)
    description = models.BooleanField()
    nombre_cadre = models.IntegerField(default= 0)
    
    def __str__(self) :
        return f'{self.nom} {self.date_debut}'
    
class Affectation (models.Model) : 
    permanence =  models.ForeignKey(Permanence,on_delete=models.DO_NOTHING)
    cadre = models.ForeignKey(Cadre, on_delete = models.DO_NOTHING)
    heure_debut = models.TimeField()
    heure_fin = models.TimeField()
    def __str__(self) : 
        return f'{self.permanence} {self.cadre} {self.heure_debut} {self.heure_fin}'
    

    
