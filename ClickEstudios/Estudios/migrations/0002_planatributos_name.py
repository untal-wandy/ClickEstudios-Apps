# Generated by Django 5.1 on 2024-08-11 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Estudios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='planatributos',
            name='name',
            field=models.CharField(default='Profesional', max_length=100),
        ),
    ]
