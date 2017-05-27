from django.http.response import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from algoritms.entity_schedule import entity_schedule
from entities.models import Event
from event_scheme.forms import EventsFilterForm


def events_show(request, archive=False):
    title = 'Расписание мероприятий'

    filters = None
    form = EventsFilterForm(request.POST or None)
    if form.is_valid():
        event_types = form.cleaned_data.get('event_types')
        dance_styles = form.cleaned_data.get('dance_styles')
        cities = form.cleaned_data.get('cities')
        if event_types or dance_styles or cities:
            filters = {}
            if event_types:
                filters['event_types'] = event_types
            if dance_styles:
                filters['dance_styles'] = dance_styles
            if cities:
                filters['cities'] = cities
    events_months = entity_schedule(Event, archive=archive, filters=filters)

    context = {
        'title': title,
        'events_months': events_months,
        'form': form,
        'archive': archive
    }
    return render(request, 'events/events.html', context)


def event_show(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    title = '%s' % (event.title,)

    form = EventsFilterForm(request.POST or None)

    context = {
        'title': title,
        'event': event,
        'form': form
    }
    return render(request, 'events/event-single.html', context)
