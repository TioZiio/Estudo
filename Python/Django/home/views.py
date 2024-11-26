from django.shortcuts import render

def home(request):
    print('Prompt This')

    variavel_qualquer = {
            'text': 'Estamos na HOME',
            'title': 'Home -'
        }

    return render(
        request,
        'home/index.html',
        variavel_qualquer
    )