import datetime

from django.shortcuts import render, get_object_or_404

from algoritms.entity_schedule import entity_schedule
from entities.models import Event


def event_scheme_show(request):
    title = 'Расписание мероприятий'

    events_months = entity_schedule(Event)

    context = {
        'title': title,
        'events_months': events_months
    }
    return render(request, 'event_scheme/event-scheme.html', context)


def event_show(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    title = '%s' % (event.title,)
    context = {
        'title': title,
        'event': event

    }
    return render(request, 'event_scheme/event-single.html', context)
