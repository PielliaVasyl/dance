from django.shortcuts import render


def dance_styles_show(request):
    title = 'Танцевальные стили'
    styles_directions = [{'dance_direction': 'Бальные танцы', 'dance_styles': ['1']},
                         {'dance_direction': 'Латина', 'dance_styles': ['2']}
                         ]

    context = {
        'title': title,
        'styles_directions': styles_directions
    }
    return render(request, 'dance_styles/dance_styles.html', context)
