from django.shortcuts import render
from main.models import Information

def main(request):
    context = {
        'title':'ГЛАВНАЯ СТРАНИЦА'
    }
    return render(request, 'main/main.html', context)


def about(request):
    content = Information.objects.all()
    context = {
        # 'title':'ИНФОРМАЦИЯ'
        'content': content

    }
    return render(request, 'main/about.html', context)


def index(request):
    return render(request, 'main/index.html')

def media(request):
    return render(request, 'main/media.html')
