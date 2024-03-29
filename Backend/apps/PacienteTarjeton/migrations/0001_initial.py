# Generated by Django 5.0.1 on 2024-02-01 03:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Medicamento', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PacienteTarjeton',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombrePaciente', models.CharField(max_length=30)),
                ('apellidoPaciente1', models.CharField(max_length=30)),
                ('apellidoPaciente2', models.CharField(max_length=30)),
                ('enfermedad', models.CharField(max_length=30)),
                ('medicamento', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Medicamento.medicamento')),
            ],
        ),
    ]
