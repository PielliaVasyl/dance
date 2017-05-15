from django.shortcuts import render

from algoritms.instances_directions import instances_groups
from entities.models import AudioWikiPlaylist


def audios_show(request):
    title = 'Треки для танцев'

    audios_directions = instances_groups(AudioWikiPlaylist)

    context = {
        'title': title,
        'audios_directions': audios_directions
    }
    return render(request, 'audios/audios.html', context)
