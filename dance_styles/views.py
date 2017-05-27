from django.shortcuts import render, get_object_or_404

from algoritms.instances_directions import instances_directions
from dance_styles.forms import DanceStyleFilterForm
from entities.models import DanceStyle, DanceStyleInSection


def dance_styles_show(request):
    title = 'Танцевальные стили'

    filters = None
    form = DanceStyleFilterForm(request.POST or None)
    if form.is_valid():
        titles = form.cleaned_data.get('titles')
        directions = form.cleaned_data.get('directions')
        count_types = form.cleaned_data.get('count_types')
        between_partners_distances = form.cleaned_data.get('between_partners_distances')
        average_prices = form.cleaned_data.get('average_prices')
        attendee_ages = form.cleaned_data.get('attendee_ages')
        if titles or directions or count_types or between_partners_distances or average_prices or attendee_ages:
            filters = {}
            if titles:
                filters['titles'] = titles
            if directions:
                filters['directions'] = directions
            if count_types:
                filters['count_types'] = count_types
            if between_partners_distances:
                filters['between_partners_distances'] = between_partners_distances
            if average_prices:
                filters['average_prices'] = average_prices
            if attendee_ages:
                filters['attendee_ages'] = attendee_ages

    styles_directions = instances_directions(DanceStyleInSection, filters=filters)

    context = {
        'title': title,
        'styles_directions': styles_directions,
        'form': form,
    }
    return render(request, 'dance_styles/dance-styles.html', context)


def dance_style_show(request, dance_style_id):
    dance_style = get_object_or_404(DanceStyleInSection, pk=dance_style_id)
    title = '%s' % (dance_style.title,)

    form = DanceStyleFilterForm(request.POST or None)
    # city_num = 1
    # try:
    #     city_num = dance_style.locations.all()[0].city.pk
    # except:
    #     pass

    context = {
        'title': title,
        'dance_style': dance_style,
        'form': form,
        # 'city_num': city_num
    }
    return render(request, 'dance_styles/dance-style-single.html', context)
