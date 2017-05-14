from django.shortcuts import render

from entities.models import VideoWiki


def videos_show(request):
    title = 'Видео о танцах'
    videos = VideoWiki.objects.all()
    context = {
        'title': title,
        'videos': videos
    }
    return render(request, 'videos/videos.html', context)