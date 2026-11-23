from django.shortcuts import render

def pagina_login(request):
    return  render(request, 'aulatest/login.html')

def pagina_registro(request):
    return  render(request, 'aulatest/registrar.html')
