import datetime

from dateutil.rrule import rrule, MONTHLY
from django.shortcuts import render

from entities.models import DanceClass
from event_scheme.views import MONTH_INT_TO_STR


def classes_show(request):
    title = 'Танцевальные группы и открытые уроки'

    # Dividing classes into months
    month_year_set_start_date = \
        set((event_date.month, event_date.year,) for event_date in DanceClass.objects.dates('start_date', 'month'))
    month_year_set_end_date = \
        set((event_date.month, event_date.year,) for event_date in DanceClass.objects.dates('end_date', 'month'))
    month_year_list_start_end_date = sorted(month_year_set_start_date | month_year_set_end_date)

    classes_months = []
    if month_year_list_start_end_date:
        first_date = datetime.date(month_year_list_start_end_date[0][1], month_year_list_start_end_date[0][0], 1)
        last_date = datetime.date(month_year_list_start_end_date[-1][1], month_year_list_start_end_date[-1][0], 1)
        dates = [(dt.month, dt.year) for dt in rrule(MONTHLY, dtstart=first_date, until=last_date)]

        for month, year in dates:
            classes = [event for event in DanceClass.objects.filter(
                start_date__gte=datetime.datetime(year, month, 1), end_date__lt=datetime.datetime(year, month + 1, 1)
            ) | DanceClass.objects.filter(
                start_date__lt=datetime.datetime(year, month + 1, 1), end_date__gte=datetime.datetime(year, month, 1)
            ) | DanceClass.objects.filter(
                start_date__isnull=True,
                end_date__gte=datetime.datetime(year, month, 1),
                end_date__lt=datetime.datetime(year, month + 1, 1)
            ) | DanceClass.objects.filter(
                end_date__isnull=True,
                start_date__gte=datetime.datetime(year, month, 1),
                start_date__lt=datetime.datetime(year, month + 1, 1)
            )
                      ]

            if classes:
                classes_months.append({'month': '%s %s' % (MONTH_INT_TO_STR[str(month)], year),
                                      'classes': classes
                                      })

    context = {
        'title': title,
        'classes_months': classes_months
    }
    return render(request, 'classes/classes.html', context)
