from django.shortcuts import render

def blog(request):
    print('Prompt This')

    variavel_qualquer = {
        'text': 'Enviado da view blog',
        'title': 'Bloguinho - '
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