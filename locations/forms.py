from django import forms

from entities.models import City, PlaceInMap, DanceStyle, PlaceType


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ["city"]


def _get_cities_choices(places):
    cities_per_places = [[(loc.city.pk, loc.city.city) for loc in place.locations.all() if loc.city]
                         for place in places]
    all_cities = []
    for cities_per_place in cities_per_places:
        all_cities.extend(cities_per_place)
    all_cities = tuple(set(all_cities))
    return all_cities


def _get_default_kyiv_or_another_city(places):
    choices = _get_cities_choices(places)
    try:
        kyiv = City.objects.get(city='Киев')
        if (kyiv.pk, kyiv.city) in choices:
            return kyiv.pk
    except:
        pass
    try:
        return choices[0][0]
    except:
        pass
    return ''


class SelectCityPlaceForm(forms.Form):
    places = PlaceInMap.objects.all()

    CITIES_CHOICES = _get_cities_choices(places)
    city = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'chosen-select', 'style': 'min-width: 172px; width: 200px',
                                           'tabindex': '0',
                                           'data-placeholder': "Выберите город...",
                                   'onchange': 'this.form.submit();'}),
        choices=CITIES_CHOICES
    )

    def __init__(self, *args, **kwargs):
        places = PlaceInMap.objects.all()

        # first call parent's constructor
        super(SelectCityPlaceForm, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['city'].required = False
        self.fields['city'].choices = _get_cities_choices(places)
        self.initial['city'] = _get_default_kyiv_or_another_city(places)


def _get_place_types_choices(places):
    place_type_dict = PlaceType.PLACE_TYPE_DICT

    place_types_per_events = [[(place_type.pk, place_type_dict.get(place_type.title, place_type.title))
                               for place_type in place.place_types.all()]
                              for place in places]

    place_types_choices = []
    for place_types_per_event in place_types_per_events:
        place_types_choices.extend(place_types_per_event)
    place_types_choices = tuple(set(place_types_choices))

    return place_types_choices


def _get_dance_styles_choices(dance_styles, places):
    direction_dict = DanceStyle.DIRECTION_SHOW
    all_directions = set([dance_style.direction for dance_style in dance_styles])

    styles_per_place = [[(dance_style.direction, dance_style.pk, dance_style.title)
                         for dance_style in place.dance_styles.all()]
                        for place in places]
    all_dance_styles = []
    for j in styles_per_place:
        all_dance_styles.extend(j)
    all_dance_styles = tuple(set(all_dance_styles))

    dance_styles_choices = ([(direction_dict.get(dance_direction, dance_direction),
                              tuple([(i[1], i[2]) for i in [dance_style for dance_style in all_dance_styles]
                                     if i[0] == dance_direction])) for dance_direction in all_directions][0],)
    return dance_styles_choices


class PlacesFilterForm(forms.Form):
    places = PlaceInMap.objects.all()
    dance_styles = DanceStyle.objects.all()

    place_types = forms.MultipleChoiceField(
        widget=forms.SelectMultiple(attrs={'class': 'chosen-select', 'style': 'min-width: 172px; width: 100%',
                                           'tabindex': '0',
                                           'data-placeholder': "Выберите типы..."}),
        choices=_get_place_types_choices(places)
    )

    dance_styles = forms.MultipleChoiceField(
        widget=forms.SelectMultiple(attrs={'class': 'chosen-select', 'style': 'min-width: 172px; width: 100%',
                                           'tabindex': '0',
                                           'data-placeholder': "Выберите танцевальные стили..."}),
        choices=_get_dance_styles_choices(dance_styles, places)
    )

    city = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'chosen-select', 'style': 'min-width: 172px; width: 100%',
                                   'tabindex': '0',
                                   'data-placeholder': "Выберите города..."}),
        choices=_get_cities_choices(places)
    )

    def __init__(self, *args, **kwargs):
        places = PlaceInMap.objects.all()
        dance_styles = DanceStyle.objects.all()

        # first call parent's constructor
        super(PlacesFilterForm, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['place_types'].required = False
        self.fields['place_types'].label = 'Типы мест'
        self.fields['place_types'].choices = _get_place_types_choices(places)
        self.fields['dance_styles'].required = False
        self.fields['dance_styles'].label = 'Танцевальные стили'
        self.fields['dance_styles'].choices = _get_dance_styles_choices(dance_styles, places)
        self.fields['city'].label = 'Город'
        self.fields['city'].choices = _get_cities_choices(places)
