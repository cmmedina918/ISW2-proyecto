# Generated by Django 5.1.7 on 2025-03-14 21:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turnosApp', '0006_sexo'),
    ]

    operations = [
        migrations.AddField(
            model_name='turno',
            name='sexo',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='turnosApp.sexo'),
        ),
    ]
