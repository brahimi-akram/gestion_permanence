# Generated by Django 5.0.3 on 2024-07-13 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
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
