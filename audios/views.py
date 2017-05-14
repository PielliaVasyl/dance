from django.shortcuts import render

from entities.models import AudioWiki


def audios_show(request):
    title = 'Видео о танцах'
    audios = AudioWiki.objects.all()
    context = {
        'title': title,
        'audios': audios
    }
    return render(request, 'audios/audios.html', context)