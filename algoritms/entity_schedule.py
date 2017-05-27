import datetime
from dateutil.rrule import rrule, MONTHLY
from django.db.models.query_utils import Q


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


def _get_filtered_instances(instances, filters=None):
    if filters is not None:
        for key, value in filters.items():
            if key == 'dance_styles':
                instances = [i for i in instances
                             if not set([str(j.pk) for j in i.dance_styles.all()]).isdisjoint(value)]
            if key == 'event_types':
                instances = [i for i in instances
                             if not set([str(j.pk) for j in i.event_types.all()]).isdisjoint(value)]
            if key == 'dance_class_types':
                instances = [i for i in instances
                             if not set([str(j.pk) for j in i.dance_class_types.all()]).isdisjoint(value)]
            if key == 'cities':
                instances = [i for i in instances
                             if not set([str(j.city.pk) for j in i.locations.all() if j.city]).isdisjoint(value)]

            if key == 'price_types':
                instances = [i for i in instances
                             if not set([str(j.pk) for j in i.price_types.all()]).isdisjoint(value)]
            if key == 'dance_studios':
                instances = [i for i in instances if i.dance_studio and str(i.dance_studio.pk) in value]
            if key == 'experience_levels':
                instances = [i for i in instances
                             if not set([str(j.pk) for j in i.experience_levels.all()]).isdisjoint(value)]

            if key == 'place_types':
                instances = [i for i in instances
                             if not set([str(j.pk) for j in i.place_types.all()]).isdisjoint(value)]

            if key == 'shop_types':
                instances = [i for i in instances
                             if not set([str(j.pk) for j in i.shop_types.all()]).isdisjoint(value)]

            if key == 'titles':
                instances = [i for i in instances if i.pk and str(i.pk) in value]
            if key == 'directions':
                instances = [i for i in instances
                             if i.dance_style.direction and str(i.dance_style.direction.pk) in value]
            if key == 'count_types':
                instances = [i for i in instances
                             if not set([str(j.pk) for j in i.count_types.all()]).isdisjoint(value)]
            if key == 'between_partners_distances':
                instances = [i for i in instances
                             if not set([str(j.pk) for j in i.between_partners_distances.all()]).isdisjoint(value)]
            if key == 'average_prices':
                instances = [i for i in instances
                             if not set([str(j.pk) for j in i.average_prices.all()]).isdisjoint(value)]
    if instances:
        instances = set(instances)
    return instances


def entity_schedule(entity, archive=False, filters=None):
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

        today = datetime.date.today()
        begin_of_current_month = today.replace(day=1)
        if archive is True:
            if first_date > begin_of_current_month:
                return instances_months
            if last_date >= begin_of_current_month:
                last_month = begin_of_current_month - datetime.timedelta(days=1)
                last_date = last_month.replace(day=1)
        else:
            if last_date < begin_of_current_month:
                return instances_months
            if first_date < begin_of_current_month:
                first_date = today.replace(day=1)

        dates = [(dt.month, dt.year) for dt in rrule(MONTHLY, dtstart=first_date, until=last_date)]

        for month, year in dates:
            instances = [instance for instance in entity.objects
            .filter(Q(start_date__gte=datetime.datetime(year, month, 1),
                      end_date__lt=datetime.datetime(year, month + 1, 1)) |
                    Q(start_date__lt=datetime.datetime(year, month + 1, 1),
                      end_date__gte=datetime.datetime(year, month, 1)) |
                    Q(start_date__isnull=True, end_date__gte=datetime.datetime(year, month, 1),
                      end_date__lt=datetime.datetime(year, month + 1, 1)) |
                    Q(end_date__isnull=True, start_date__gte=datetime.datetime(year, month, 1),
                      start_date__lt=datetime.datetime(year, month + 1, 1)))
            ]

            instances = _get_filtered_instances(instances, filters)

            if instances:
                instances_months.append({'month': '%s %s' % (MONTH_INT_TO_STR[str(month)], year),
                                         'instances': instances,
                                         })
    return instances_months
