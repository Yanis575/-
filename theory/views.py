from django.shortcuts import render


def index(request):
    pass
    templ = 'theory/index.html'
    return render(request, templ)