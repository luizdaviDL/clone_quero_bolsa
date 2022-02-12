# Generated by Django 4.0.2 on 2022-02-08 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_remove_curso_turno_curso_modalidade_1_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curso',
            name='turno_3',
        ),
        migrations.AddField(
            model_name='curso',
            name='turno',
            field=models.CharField(choices=[('M', 'Manhã'), ('T', 'Tarde'), ('N', 'Noite')], default=1, max_length=1),
            preserve_default=False,
        ),
    ]
