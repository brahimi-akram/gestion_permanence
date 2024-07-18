# Generated by Django 5.0.6 on 2024-07-12 17:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cadre',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=40)),
                ('prenom', models.CharField(max_length=40)),
                ('poste', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Permanence',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('date_debut', models.DateField(unique=True)),
                ('name', models.CharField(max_length=60)),
                ('description', models.BooleanField()),
                ('nombre_cadre', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Affection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heure_debut', models.TimeField()),
                ('heure_fin', models.TimeField()),
                ('cadre', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.cadre')),
                ('premanence', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='main.permanence')),
            ],
        ),
    ]
