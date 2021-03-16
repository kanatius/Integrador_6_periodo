# Generated by Django 3.1.7 on 2021-03-16 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imovel', '0002_auto_20210316_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imovel',
            name='status',
            field=models.CharField(choices=[('Disponível', 'Disponível'), ('Alugado', 'Alugado')], default='Disponível', max_length=100),
        ),
        migrations.AlterField(
            model_name='imovel',
            name='tipo',
            field=models.CharField(choices=[('Casa', 'Casa'), ('Apartamento', 'Apartamento'), ('Sobrado', 'Sobrado'), ('Kitnet', 'Kitnet'), ('Edícula', 'Edícula'), ('Flat', 'Flat')], default='Casa', max_length=100),
        ),
    ]
