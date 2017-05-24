from django.shortcuts import render, get_object_or_404

from entities.models import DanceHall, DanceStudio, DanceShop, PlaceInMap
from locations.forms import SelectCityPlaceForm


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
            'place': PlaceInMap,
            'studio': DanceStudio,
            'shop': DanceShop,
            'hall_for_rent': DanceHall
        }.get(location, '')

        select_city_form = {
            'place': SelectCityPlaceForm,
            # 'studio': SelectCityStudioForm,
            # 'shop': SelectCityShopForm,
            # 'hall_for_rent': SelectCityHallForm
        }.get(location, '')

        if entity and select_city_form:
            select_city_form = select_city_form(request.POST or None)
            try:
                instances = entity.objects.filter(locations__city=int(request.POST['city'][0]))
            except:
                print(select_city_form.initial['city'])
                if select_city_form.initial['city']:
                    instances = entity.objects.filter(locations__city=select_city_form.initial['city'])
                else:
                    instances = None
        else:
            is_wrong_location = True
            context = {
                'title': title,
                'is_wrong_location': is_wrong_location,
            }
            return render(request, 'locations/locations.html', context)

    context = {
        'title': title,
        'is_wrong_location': is_wrong_location,
        'instances': instances,
        'location_title': location_title,
        'select_city_form': select_city_form
    }
    return render(request, 'locations/locations.html', context)


def place_show(request, place_id):
    place = get_object_or_404(PlaceInMap, pk=place_id)
    title = '%s' % (place.title,)

    # form = EventsFilterForm(request.POST or None)

    context = {
        'title': title,
        'place': place,
        # 'form': form
    }
    return render(request, 'locations/place-single.html', context)
