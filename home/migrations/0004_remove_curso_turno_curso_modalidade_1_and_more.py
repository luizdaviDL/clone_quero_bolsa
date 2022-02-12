# Generated by Django 4.0.2 on 2022-02-08 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_remove_aviso_universidade_curso_aviso'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curso',
            name='turno',
        ),
        migrations.AddField(
            model_name='curso',
            name='modalidade_1',
            field=models.CharField(blank=True, choices=[('P', 'Presencial'), ('S', 'Semi-presencial'), ('E', 'Ead'), ('F', 'Flex')], max_length=1),
        ),
        migrations.AddField(
            model_name='curso',
            name='modalidade_2',
            field=models.CharField(blank=True, choices=[('P', 'Presencial'), ('S', 'Semi-presencial'), ('E', 'Ead'), ('F', 'Flex')], max_length=1),
        ),
        migrations.AddField(
            model_name='curso',
            name='modalidade_3',
            field=models.CharField(blank=True, choices=[('P', 'Presencial'), ('S', 'Semi-presencial'), ('E', 'Ead'), ('F', 'Flex')], max_length=1),
        ),
        migrations.AddField(
            model_name='curso',
            name='turno_1',
            field=models.CharField(blank=True, choices=[('M', 'Manhã'), ('T', 'Tarde'), ('N', 'Noite')], max_length=1),
        ),
        migrations.AddField(
            model_name='curso',
            name='turno_2',
            field=models.CharField(blank=True, choices=[('M', 'Manhã'), ('T', 'Tarde'), ('N', 'Noite')], max_length=1),
        ),
        migrations.AddField(
            model_name='curso',
            name='turno_3',
            field=models.CharField(blank=True, choices=[('M', 'Manhã'), ('T', 'Tarde'), ('N', 'Noite')], max_length=1),
        ),
    ]
