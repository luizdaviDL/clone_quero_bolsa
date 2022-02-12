from django.shortcuts import render, HttpResponse,redirect
from .models import Usuario
import hashlib


def cadastro(request):
    status = request.GET.get('status')
    return render(request, 'cadastro.html', {'status':status}) 

def login(request):
    status = request.GET.get('status')
    return render(request, 'login.html', {'status':status}) 


def valida_cadastro(request):
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    usuario_inst = Usuario.objects.filter(email=email)

    if len(nome.strip()) ==0 or len(email.strip()) ==0:
        return redirect('/auth/cadastro?status=1')

    if len(senha) < 8 or len(senha) > 12:
        return redirect('/auth/cadastro?status=2')
    

    if len(usuario_inst) > 0:
        return redirect('/auth/cadastro?status=3') 
    
    try:
        senha_a = hashlib.sha256(senha.encode()).hexdigest()
        usuario_save = Usuario(nome=nome, email=email, senha=senha_a)
        usuario_save.save()
        return redirect('/auth/cadastro?status=4')

    except:
        return  redirect('/auth/cadastro?status=5')



def valida_login(request):
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    senha_1 = hashlib.sha256(senha.encode()).hexdigest()
    usuario_log = Usuario.objects.filter(email=email, senha=senha_1)
    

    if len(email) ==0 or len(senha) ==0:
        return redirect('/auth/login?status=1')

    if len(senha) <8 or len(senha) >12:
        return redirect('/auth/login?status=2')

    if len(usuario_log) ==0:
         return redirect('/auth/login?status=3')

    elif len(usuario_log) >0:
        request.session['usuario'] = usuario_log[0].id
        return redirect('/home/garantir_bolsa1')

def sair(request):
    request.session.flush()
    return redirect('/home')