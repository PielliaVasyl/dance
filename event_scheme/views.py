from django.shortcuts import render, get_object_or_404

from algoritms.entity_schedule import entity_schedule
from entities.models import Event


def events_show(request, archive=False):
    title = 'Расписание мероприятий'

    events_months = entity_schedule(Event, archive=archive)

    context = {
        'title': title,
        'events_months': events_months,
        'archive': archive
    }
    return render(request, 'events/events.html', context)


def event_show(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    title = '%s' % (event.title,)
    context = {
        'title': title,
        'event': event

    }
    return render(request, 'events/event-single.html', context)
