from django.shortcuts import render

from algoritms.instances_directions import instances_directions
from entities.models import DanceStyle, DanceStyleInSection


def dance_styles_show(request):
    title = 'Танцевальные стили'

    styles_directions = instances_directions(DanceStyleInSection)

    context = {
        'title': title,
        'styles_directions': styles_directions
    }
    return render(request, 'dance_styles/dance-styles.html', context)
