# Generated by Django 4.0.2 on 2022-02-07 19:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bairro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bairro', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cidade', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Universidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('numero', models.IntegerField()),
                ('cidade_estado', models.CharField(max_length=80)),
                ('bairro', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='home.bairro')),
                ('cidade', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='home.cidade')),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.FileField(upload_to='media')),
                ('curso', models.CharField(max_length=50)),
                ('tipo', models.CharField(choices=[('G', 'Graduação'), ('P', 'Pós-graduação'), ('E', 'Escola'), ('I', 'Idioma'), ('C', 'Curso livre')], max_length=1)),
                ('duracao', models.CharField(max_length=70)),
                ('modalidade', models.CharField(choices=[('P', 'Presencial'), ('S', 'Semi-presencial'), ('E', 'Ead'), ('F', 'Flex')], max_length=1)),
                ('turno', models.CharField(choices=[('M', 'Manhã'), ('T', 'Tarde'), ('N', 'Noite')], max_length=1)),
                ('valor', models.FloatField()),
                ('bairro', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='home.bairro')),
                ('cidade', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='home.cidade')),
                ('universidade', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='home.universidade')),
            ],
        ),
    ]
