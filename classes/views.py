from django.shortcuts import render

from algoritms.entity_schedule import entity_schedule
from classes.forms import DanceClassFilterForm
from entities.models import DanceClass


def classes_show(request, archive=False):
    title = 'Танцевальные группы и открытые уроки'

    filters = None

    form = DanceClassFilterForm(request.POST or None)
    if form.is_valid():
        dance_class_types = form.cleaned_data.get('dance_class_types')
        dance_styles = form.cleaned_data.get('dance_styles')
        price_types = form.cleaned_data.get('price_types')
        dance_studios = form.cleaned_data.get('dance_studios')
        experience_levels = form.cleaned_data.get('experience_levels')
        if dance_class_types or dance_styles or price_types or dance_studios or experience_levels:
            filters = {}
            if dance_class_types:
                filters['dance_class_types'] = dance_class_types
            if dance_styles:
                filters['dance_styles'] = dance_styles
            if price_types:
                filters['price_types'] = price_types
            if dance_studios:
                filters['dance_studios'] = dance_studios
            if experience_levels:
                filters['experience_levels'] = experience_levels

    classes_months = entity_schedule(DanceClass, archive=archive, filters=filters)

    context = {
        'title': title,
        'instances_months': classes_months,
        'form': form,
        'archive': archive
    }

    return render(request, 'classes/classes.html', context)
