from django.shortcuts import render, get_object_or_404

from algoritms.entity_schedule import _get_filtered_instances
from entities.models import DanceHall, DanceStudio, DanceShop, PlaceInMap
from locations.forms import SelectCityPlaceForm, PlacesFilterForm, SelectCityStudioForm, StudiosFilterForm, \
    SelectCityShopForm, ShopsFilterForm, HallsFilterForm, SelectCityHallForm


def locations_show(request):
    location = request.GET.get('location', '')

    instances = ''
    location_set = {'place', 'studio', 'shop', 'hall'}

    is_wrong_location = location not in location_set
    select_city_form = SelectCityPlaceForm(None)
    form = PlacesFilterForm(None)

    title = {
        'place': 'Танцевальные места на карте',
        'studio': 'Танцевальные школы на карте',
        'shop': 'Магазины танцевальной одежды на карте',
        'hall': 'Танцевальные залы для аренды'
    }.get(location, 'Неверно указан тип локаций')

    location_title = {
        'place': 'Танцевальные места',
        'studio': 'Танцевальные школы',
        'shop': 'Магазины танцевальной одежды',
        'hall': 'Танцевальные залы для аренды'
    }.get(location, 'Неверно указан тип локаций')

    find_location_title = {
        'place': 'места',
        'studio': 'школы',
        'shop': 'магазины',
        'hall': 'залы'
    }.get(location, 'Неверно указан тип локаций')

    if not is_wrong_location:
        entity = {
            'place': PlaceInMap,
            'studio': DanceStudio,
            'shop': DanceShop,
            'hall': DanceHall
        }.get(location, '')

        select_city_form = {
            'place': SelectCityPlaceForm,
            'studio': SelectCityStudioForm,
            'shop': SelectCityShopForm,
            'hall': SelectCityHallForm
        }.get(location, '')

        form = {
            'place': PlacesFilterForm,
            'studio': StudiosFilterForm,
            'shop': ShopsFilterForm,
            'hall': HallsFilterForm
        }.get(location, '')

        if entity and select_city_form and form:
            select_city_form = select_city_form(request.POST or None)
            form = form(request.POST or None)
            try:
                instances = entity.objects.filter(locations__city=int(request.POST['city'][0]))
            except:
                if select_city_form.initial['city']:
                    instances = entity.objects.filter(locations__city=select_city_form.initial['city']).distinct()
                else:
                    instances = None
            filters = None
            if form.is_valid():
                if location == 'place':
                    place_types = form.cleaned_data.get('place_types')
                    dance_styles = form.cleaned_data.get('dance_styles')
                    if place_types or dance_styles:
                        filters = {}
                        if place_types:
                            filters['place_types'] = place_types
                        if dance_styles:
                            filters['dance_styles'] = dance_styles

                if location == 'studio':
                    dance_styles = form.cleaned_data.get('dance_styles')
                    if dance_styles:
                        filters = {}
                        if dance_styles:
                            filters['dance_styles'] = dance_styles

                if location == 'shop':
                    shop_types = form.cleaned_data.get('shop_types')
                    dance_styles = form.cleaned_data.get('dance_styles')
                    if shop_types or dance_styles:
                        filters = {}
                        if shop_types:
                            filters['shop_types'] = shop_types
                        if dance_styles:
                            filters['dance_styles'] = dance_styles

                if location == 'hall':
                    pass

            instances = _get_filtered_instances(instances, filters)
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
        'find_location_title': find_location_title,
        'select_city_form': select_city_form,
        'form': form
    }
    return render(request, 'locations/locations.html', context)


def place_show(request, place_id):
    place = get_object_or_404(PlaceInMap, pk=place_id)
    title = '%s' % (place.title,)

    form = PlacesFilterForm(request.POST or None)
    city_num = 1
    try:
        city_num = place.locations.all()[0].city.pk
    except:
        pass

    context = {
        'title': title,
        'place': place,
        'form': form,
        'city_num': city_num
    }
    return render(request, 'locations/place-single.html', context)


def studio_show(request, studio_id):
    studio = get_object_or_404(DanceStudio, pk=studio_id)
    title = '%s' % (studio.title,)

    form = StudiosFilterForm(request.POST or None)
    city_num = 1
    try:
        city_num = studio.locations.all()[0].city.pk
    except:
        pass

    context = {
        'title': title,
        'studio': studio,
        'form': form,
        'city_num': city_num
    }
    return render(request, 'locations/studio-single.html', context)


def shop_show(request, shop_id):
    shop = get_object_or_404(DanceShop, pk=shop_id)
    title = '%s' % (shop.title,)

    form = ShopsFilterForm(request.POST or None)
    city_num = 1
    try:
        city_num = shop.locations.all()[0].city.pk
    except:
        pass

    context = {
        'title': title,
        'shop': shop,
        'form': form,
        'city_num': city_num
    }
    return render(request, 'locations/shop-single.html', context)


def hall_show(request, hall_id):
    hall = get_object_or_404(DanceHall, pk=hall_id)
    title = '%s' % (hall.title,)

    form = HallsFilterForm(request.POST or None)
    city_num = 1
    try:
        city_num = hall.locations.all()[0].city.pk
    except:
        pass

    context = {
        'title': title,
        'hall': hall,
        'form': form,
        'city_num': city_num
    }
    return render(request, 'locations/hall-single.html', context)
