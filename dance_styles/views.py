from django.shortcuts import render

from entities.models import DanceStyle


def dance_styles_show(request):
    title = 'Танцевальные стили'

    dance_styles = DanceStyle.objects.all()
    directions = {'BAL', 'LAT'}
    dance_direction_show = {
        'BAL': 'Балет',
        'LAT': 'Латина'
    }
    styles_directions = []
    for direction in directions:
        dances_for_particular_direction = dance_styles.filter(dance_direction=direction)
        if dances_for_particular_direction:
            dance_style_direction = {'dance_direction': dance_direction_show.get(direction, direction),
                                     'dance_styles': dances_for_particular_direction}
            styles_directions.append(dance_style_direction)

    context = {
        'title': title,
        'styles_directions': styles_directions
    }
    return render(request, 'dance_styles/dance_styles.html', context)
