from django.shortcuts import render

from entities.models import Event


def event_scheme_show(request):
    title = 'EventScheme'
    events = Event.objects.all()
    context = {
        'title': title,
        'events': events
    }
    return render(request, 'event_scheme.html', context)
