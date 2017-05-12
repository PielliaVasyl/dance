from django.shortcuts import render

from algoritms.instances_directions import instances_directions
from entities.models import DanceStyle


def dance_styles_show(request):
    title = 'Танцевальные стили'

    styles_directions = instances_directions(DanceStyle)

    context = {
        'title': title,
        'styles_directions': styles_directions
    }
    return render(request, 'dance_styles/dance_styles.html', context)
