from django.shortcuts import render
from blog.data import posts

def blog(request):
    print('Prompt This')

    variavel_qualquer = {
        'text': 'Enviado da view blog',
        'title': 'Bloguinho - ',
        'dados': posts
    }

    return render(
        request,
        'blog/index.html',
        variavel_qualquer
    )

def exemplo(request):
    print(request)

    variavel_qualquer = {
        'text': 'Enviado da view blog/exemplo',
        'title': 'Exemplo - '
    }

    return render(
        request,
        'blog/exemplo.html',
        variavel_qualquer
    )

def post(request, id):
    print('Prompt This')

    variavel_qualquer = {
        'text': 'Enviado do view blog/post, precisa de um <id>',
        'title': 'Bloguinho - ',
        'dados': posts,
    }

    return render(
        request,
        'blog/index.html',
        variavel_qualquer
    )