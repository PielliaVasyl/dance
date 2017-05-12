from django.shortcuts import render

from algoritms.instances_directions import instances_directions
from entities.models import LinkShouldKnow, PersonShouldKnow, OrganizationShouldKnow


def should_know_show(request):
    title = 'Полезно знать'

    instances_directions_link = instances_directions(LinkShouldKnow)
    instances_directions_person = instances_directions(PersonShouldKnow)
    instances_directions_organization = instances_directions(OrganizationShouldKnow)

    context = {
        'title': title,
        'instances_directions_link': instances_directions_link,
        'instances_directions_person': instances_directions_person,
        'instances_directions_organization': instances_directions_organization
    }
    return render(request, 'should_know/should-know.html', context)
