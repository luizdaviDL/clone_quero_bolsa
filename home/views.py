from operator import le
import re
from django.shortcuts import redirect, render,HttpResponse
from .models import Aviso, CadastroBolsa, Curso, Universidade
def home(request):
    status = request.GET.get('status')
    cursos = Curso.objects.all()    
    return render(request, 'home.html',{'cursos':cursos,
                                        'status':status,
                                        })


def detalhes(request,id):
    curso_dt = Curso.objects.filter(id=id)
    aviso = Aviso.objects.filter(aviso = id)
    
    return render(request, 'detalhes.html',{'curso_dt':curso_dt,
                                            'aviso':aviso}) 


def garantir_bolsa(request, id):
    if request.session.get('usuario'):
        curso = Curso.objects.filter(id=id)   
        usuario_logado = request.session.get('usuario')
        return render(request, 'garantir_bolsa.html', {'curso':curso,
                                                       'usuario_logado':usuario_logado})
    else:
        return redirect('/auth/cadastro?status=7')                                               


def cadastro_bolsa(request,id):
    if request.session.get('usuario'):
        id=id
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        nascimento = request.POST.get('nascimento')
        email = request.POST.get('email')
        cep = request.POST.get('cep')
        cidade = request.POST.get('cidade')
        estado = request.POST.get('estado') 
        universidade = request.POST.get('universidade')
        curso = request.POST.get('curso')

        univer_get = Universidade.objects.get(id=universidade) 

   
        cadastro = CadastroBolsa(nome=nome,
                                cpf=cpf,
                                nascimento=nascimento,
                                email=email,
                                cep=cep,
                                cidade=cidade,
                                estado=estado,                                
                                universidade=univer_get,
                                curso=curso)
        cadastro.save()     
        return redirect('/home?status=1')                 
                                                      

    else:
        return redirect('/auth/cadastro?status=7')                                   
        
    
       


    
