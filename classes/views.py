from django.shortcuts import render

from algoritms.entity_schedule import entity_schedule
from entities.models import DanceClass


def classes_show(request):
    title = 'Танцевальные группы и открытые уроки'

    classes_months = entity_schedule(DanceClass)

    context = {
        'title': title,
        'classes_months': classes_months
    }
    return render(request, 'classes/classes.html', context)
