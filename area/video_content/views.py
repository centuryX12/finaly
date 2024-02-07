from django.shortcuts import render

from video_content.models import Iggy

def video_stream(request):
    content = Iggy.objects.all()
    context = {
        'content':content
    }

    return render(request, 'video_content/video_stream.html', context)
