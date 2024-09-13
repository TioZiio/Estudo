from django.http import HttpResponse
# from django.shortcuts import render

def home(request):
    print('Prompt This')
    return HttpResponse('Mensage Response for page home')