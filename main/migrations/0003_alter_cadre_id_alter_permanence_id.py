# Generated by Django 5.0.6 on 2024-07-13 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_name_permanence_nom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadre',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='permanence',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
