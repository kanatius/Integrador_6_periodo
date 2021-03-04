# Generated by Django 3.1.7 on 2021-03-04 00:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('nome_sem_acentos', models.CharField(max_length=255)),
                ('estado_sigla', models.CharField(max_length=2)),
                ('estado', models.CharField(max_length=255)),
                ('estado_sem_acentos', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Imovel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=500)),
                ('tipo', models.CharField(max_length=55)),
                ('status', models.CharField(max_length=55)),
                ('valor_mensal', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ImovelImagem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uri_arquivo', models.FileField(upload_to='')),
                ('imovel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imagens', to='imovel.imovel')),
            ],
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logradouro', models.CharField(max_length=255)),
                ('bairro', models.CharField(max_length=255)),
                ('numero', models.IntegerField(blank=True, null=True)),
                ('ponto_de_referencia', models.CharField(blank=True, max_length=55, null=True)),
                ('cidade', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='imovel.cidade')),
                ('imovel', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='imovel.imovel')),
            ],
        ),
    ]
