import datetime

from dateutil.rrule import rrule, MONTHLY
from django.shortcuts import render

from entities.models import Event

MONTH_INT_TO_STR = {
    '1': 'Январь',
    '2': 'Февраль',
    '3': 'Март',
    '4': 'Апрель',
    '5': 'Май',
    '6': 'Июнь',
    '7': 'Июль',
    '8': 'Август',
    '9': 'Сентябрь',
    '10': 'Октябрь',
    '11': 'Ноябрь',
    '12': 'Декабрь'
}


def event_scheme_show(request):
    title = 'Расписание мероприятий'

    # Dividing events into months
    month_year_set_start_date = \
        set((event_date.month, event_date.year,) for event_date in Event.objects.dates('start_date', 'month'))
    month_year_set_end_date = \
        set((event_date.month, event_date.year,) for event_date in Event.objects.dates('end_date', 'month'))
    month_year_list_start_end_date = sorted(month_year_set_start_date | month_year_set_end_date)

    events_months = []
    if month_year_list_start_end_date:
        first_date = datetime.date(month_year_list_start_end_date[0][1], month_year_list_start_end_date[0][0], 1)
        last_date = datetime.date(month_year_list_start_end_date[-1][1], month_year_list_start_end_date[-1][0], 1)
        dates = [(dt.month, dt.year) for dt in rrule(MONTHLY, dtstart=first_date, until=last_date)]

        for month, year in dates:
            events = [event for event in Event.objects.filter(
                start_date__gte=datetime.datetime(year, month, 1), end_date__lt=datetime.datetime(year, month+1, 1)
                ) | Event.objects.filter(
                start_date__lt=datetime.datetime(year, month+1, 1), end_date__gte=datetime.datetime(year, month, 1)
                ) | Event.objects.filter(
                start_date__isnull=True,
                end_date__gte=datetime.datetime(year, month, 1),
                end_date__lt=datetime.datetime(year, month+1, 1)
                ) | Event.objects.filter(
                end_date__isnull=True,
                start_date__gte=datetime.datetime(year, month, 1),
                start_date__lt=datetime.datetime(year, month+1, 1)
                )
                      ]

            if events:
                events_months.append({'month': '%s %s' % (MONTH_INT_TO_STR[str(month)], year),
                                      'events': events
                                      })

    context = {
        'title': title,
        'events_months': events_months
    }
    return render(request, 'event_scheme/event-scheme.html', context)
