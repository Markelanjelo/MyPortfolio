from django.shortcuts import render


def firstPage(request):
    return render(request, 'MarkelMain/firstPage.html', {'title': 'Welcome to my portfolio page'})

def about(request):
    return render(request, 'MarkelMain/main.html')