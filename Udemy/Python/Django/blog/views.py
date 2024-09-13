from django.http import HttpResponse
# from django.shortcuts import render

def blog(request):
    print(request)
    print('Este print retorna no terminal')
    return HttpResponse('Mensage Response for Blog')

def exemplo(request):
    print(request)
    print('Este print retorna no terminal')
    return HttpResponse('Mensage Response for Blog Exemplo')