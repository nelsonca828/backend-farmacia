# Generated by Django 5.0.1 on 2024-02-14 02:33

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Medicamento', '0002_alter_medicamento_existencia'),
    ]

    operations = [
        migrations.CreateModel(
            name='LibroVenc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lote', models.IntegerField(default=0, null=True)),
                ('fechavenc', models.DateField(default=django.utils.timezone.now)),
                ('cantidadLote', models.IntegerField(default=0)),
                ('cantidadRestante', models.IntegerField(default=models.IntegerField(default=0), null=True)),
                ('medicamento', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='Medicamento.medicamento')),
            ],
        ),
    ]