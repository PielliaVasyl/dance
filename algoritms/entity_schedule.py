import datetime
from dateutil.rrule import rrule, MONTHLY

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


def entity_schedule(entity):
    # Dividing instances into months
    month_year_set_start_date = \
        set((instance_date.month, instance_date.year,) for instance_date in entity.objects.dates('start_date', 'month'))
    month_year_set_end_date = \
        set((instance_date.month, instance_date.year,) for instance_date in entity.objects.dates('end_date', 'month'))
    month_year_list_start_end_date = sorted(month_year_set_start_date | month_year_set_end_date)

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
    return instances_months
