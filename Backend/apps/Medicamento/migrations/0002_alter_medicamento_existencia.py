# Generated by Django 5.0.1 on 2024-02-12 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Medicamento', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicamento',
            name='existencia',
            field=models.IntegerField(default=0),
        ),
    ]
