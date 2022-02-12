import email
from django.db import models
from random import choice

class Cidade(models.Model):
    cidade = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.cidade

class Bairro(models.Model):
    bairro = models.CharField(max_length=70)
    def __str__(self) -> str:
        return self.bairro

class Universidade(models.Model):
    nome = models.CharField(max_length=50)
    cidade = models.ForeignKey(Cidade, on_delete=models.DO_NOTHING)
    bairro = models.ForeignKey(Bairro, on_delete=models.DO_NOTHING)
    numero = models.IntegerField()
    cidade_estado = models.CharField(max_length=80)


    def __str__(self) -> str:
        return self.nome 

class Aviso(models.Model):
    aviso = models.TextField() 
    
    def __str__(self) -> str:
        return self.aviso


class Curso(models.Model):
    escolha = (
        ('G', 'Graduação'),
        ('P', 'Pós-graduação'),
        ('E', 'Escola'),
        ('I', 'Idioma'),
        ('C', 'Curso livre'),        
    ) 

    modalidades = (
        ('P', 'Presencial'),
        ('S', 'Semi-presencial'),
        ('E', 'Ead'),
        ('F', 'Flex'),
    ) 


    turnos = (
        ('M','Manhã'),
        ('T','Tarde'),
        ('N','Noite'),
    )

    img = models.FileField(upload_to='media')
    curso = models.CharField(max_length=50)
    tipo = models.CharField(max_length=1, choices=escolha)
    duracao = models.CharField(max_length=70)
    modalidade = models.CharField(max_length=1, choices=modalidades)
    turno = models.CharField(max_length=1, choices=turnos, blank=True)
    valor = models.FloatField()
    desconto = models.IntegerField(blank=True)
    universidade = models.ForeignKey(Universidade, on_delete=models.DO_NOTHING)
    aviso = models.ForeignKey(Aviso, on_delete=models.DO_NOTHING, blank=True)
  
   
    def __str__(self) -> str:
        return self.curso
  
class CadastroBolsa(models.Model):
    nome = models.CharField(max_length=100) 
    cpf = models.CharField(max_length=14, null=True)
    nascimento = models.CharField(max_length=8)
    email = models.EmailField()
    cep = models.CharField(max_length=8, null=True)
    cidade = models.CharField(max_length=80)
    estado = models.CharField(max_length=80, null=True)
    universidade = models.ForeignKey(Universidade, on_delete=models.DO_NOTHING)
    curso = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f'{self.nome} | {self.curso} |{self.universidade} '
