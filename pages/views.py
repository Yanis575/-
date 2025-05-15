from django.shortcuts import render


def info (request):
    pass
    templ = 'pages/info.html'
    return render(request, templ)