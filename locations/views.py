from django.shortcuts import render

from entities.models import DanceHall, DanceStudio, DanceShop, PlaceInMap


def locations_show(request):
    location = request.GET.get('location', '')

    instances = ''
    location_set = {'place', 'studio', 'shop', 'hall_for_rent'}

    is_wrong_location = location not in location_set

    title = {
        'place': 'Танцевальные места на карте',
        'studio': 'Танцевальные школы на карте',
        'shop': 'Магазины танцевальной одежды на карте',
        'hall_for_rent': 'Танцевальные залы для аренды'
    }.get(location, 'Неверно указан тип локаций')

    location_title = {
        'place': 'Танцевальные места',
        'studio': 'Танцевальные школы',
        'shop': 'Магазины танцевальной одежды',
        'hall_for_rent': 'Танцевальные залы для аренды'
    }.get(location, 'Неверно указан тип локаций')

    if not is_wrong_location:
        entity = {
            # 'place': PlaceInMap,
            'studio': DanceStudio,
            'shop': DanceShop,
            'hall_for_rent': DanceHall
        }.get(location, '')

        if entity:
            if entity is PlaceInMap:
                instances = entity.objects.filter(show_in_map_section=True)
            else:
                instances = entity.objects.all()
        else:
            is_wrong_location = True

    context = {
        'title': title,
        'is_wrong_location': is_wrong_location,
        'instances': instances,
        'location_title': location_title
    }
    return render(request, 'locations/locations.html', context)
