from django import forms

from entities.models import City, PlaceInMap


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
