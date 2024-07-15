import holidays
from .models import *
import sqlite3
def create_holidays():
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()

    # Name of the table you want to clear
    table_name = 'main_permanence'

    # Delete all rows from the table
    cursor.execute(f"DELETE FROM {table_name}")

    # Reset the auto-increment counter
    # This step may be slightly different depending on the SQLite version
    cursor.execute(f"DELETE FROM sqlite_sequence WHERE name='{table_name}'")

    # Commit the changes and close the connection
    conn.commit()
    conn.close()
    algeria_holidays=holidays.DZ()
    # If you want to get holidays for a specific year
    year = 2024
    algeria_holidays = holidays.Algeria(years=year)
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
        if estimated!=None:
            perma.description=True
        else:
            perma.description=False
        perma.save()