from django.shortcuts import render

from entities.models import DanceStyle


def dance_styles_show(request):
    title = 'Танцевальные стили'
    styles_directions = [{'dance_direction': 'Бальные танцы', 'dance_styles': ['1']},
                         {'dance_direction': 'Латина', 'dance_styles': ['2']}
                         ]
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



    instances_months = []
    if month_year_list_start_end_date:
        first_date = datetime.date(month_year_list_start_end_date[0][1], month_year_list_start_end_date[0][0], 1)
        last_date = datetime.date(month_year_list_start_end_date[-1][1], month_year_list_start_end_date[-1][0], 1)
        dates = [(dt.month, dt.year) for dt in rrule(MONTHLY, dtstart=first_date, until=last_date)]

        for month, year in dates:
            instances = [instance for instance in entity.objects.filter(
                start_date__gte=datetime.datetime(year, month, 1), end_date__lt=datetime.datetime(year, month + 1, 1)
            ) | entity.objects.filter(
                start_date__lt=datetime.datetime(year, month + 1, 1), end_date__gte=datetime.datetime(year, month, 1)
            ) | entity.objects.filter(
                start_date__isnull=True,
                end_date__gte=datetime.datetime(year, month, 1),
                end_date__lt=datetime.datetime(year, month + 1, 1)
            ) | entity.objects.filter(
                end_date__isnull=True,
                start_date__gte=datetime.datetime(year, month, 1),
                start_date__lt=datetime.datetime(year, month + 1, 1)
            )
                      ]

            if instances:
                instances_months.append({'month': '%s %s' % (MONTH_INT_TO_STR[str(month)], year),
                                        'instances': instances
                                        })