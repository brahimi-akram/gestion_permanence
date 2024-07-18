import holidays
from .models import *

from datetime import datetime
def create_holidays():
    
    # If you want to get holidays for a specific year
    year = datetime.now().date().year
    future_years = [year for year in range(year - 10, year + 10)]
    for years in future_years :
        object = Permanence.objects.filter(date_debut__year = years)
        if object.count() == 0 : 

            algeria_holidays = holidays.Algeria(years=years)
            fr_sa_days=[]

            for month in range(1, 13):
                for day in range(1, 32):
                    try:
                        date_obj = datetime(years, month, day).date()
                        weekday = date_obj.weekday()  # Monday is 0 and Sunday is 6

                        # Check if the day is Friday (4) or Saturday (5)
                        if weekday == 4 or weekday == 5:
                            # Exclude the day if it's a holiday
                            if date_obj not in algeria_holidays:
                                perm=Permanence()
                                if weekday == 4:
                                    perm.nom='الجمعة'
                                else:
                                    perm.nom='السبت'
                                perm.date_debut=date_obj
                                perm.description=False
                                perm.save()
                                fr_sa_days.append(date_obj)
                    except ValueError:
                        continue  # Handles days that don't exist in some months
                    
            translation_dict = {
                "New Year's Day": "رأس السنة",
                "Labor Day": "عيد العمال",
                "Independence Day": "عيد الاستقلال",
                "Eid al-Fitr": "عيد الفطر",
                "Eid al-Adha": "عيد الأضحى",
                "Islamic New Year": "رأس السنة الهجرية",
                "Mawlid al-Nabi": "المولد النبوي",
                "Amazigh New Year":"رأس السنة الأمازيغية",
                "Ashura":'عاشوراء',
                "Prophet's Birthday":"المولد النبوي",
                "Revolution Day":"ذكرى إندلاع الثورة التحريرية"
                # Add more translations as needed
            }
            duplicates=['','اليوم الأول','اليوم الثاني','اليوم الثالث']
            for date, name in sorted(algeria_holidays.items()):
                perma=Permanence()
                perma.date_debut=date
                try:
                    name,estimated=name.split('(')
                    name,estimated=name.split("Holiday")

                except:
                    name=name
                    estimated=None
                name=name.strip()
                same_name_instances=Permanence.objects.filter(nom__icontains=translation_dict[name])

                if same_name_instances.count()==0:
                    perma.nom=translation_dict[name.strip()]
                elif same_name_instances.count()==1:
                    old_instance=same_name_instances[0]
                    old_instance.nom=f'{duplicates[same_name_instances.count()]} {translation_dict[name.strip()]}'
                    old_instance.save()
                    perma.nom=f'{duplicates[same_name_instances.count()+1]} {translation_dict[name]}'
                    # print(duplicates[same_name_instances.count()])
                    # print(perma.nom,same_name_instances[0].nom)
                else:
                    perma.nom=f'{duplicates[same_name_instances.count()+1]} {translation_dict[name]}'

                perma.description=True

                perma.save()