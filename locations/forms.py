from django import forms

from entities.models import City, PlaceInMap, DanceStyle, PlaceType, DanceStudio, DanceShop, ShopType, DanceHall, \
    Instructor


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ["city"]


def _get_cities_choices(instances, instances_2=None):
    cities_per_instances = [[(loc.city.pk, loc.city.city) for loc in instance.locations.all() if loc.city]
                            for instance in instances]
    cities_per_instances_2 = []
    if instances_2:
        cities_per_instances_2 = [[(loc.city.pk, loc.city.city) for loc in instance.locations.all() if loc.city]
                                  for instance in instances_2]

    all_cities = []
    for cities_per_instance in cities_per_instances:
        all_cities.extend(cities_per_instance)
    if instances_2:
        for cities_per_instance in cities_per_instances_2:
            all_cities.extend(cities_per_instance)
    all_cities = tuple(set(all_cities))
    return all_cities


def _get_default_kyiv_or_another_city(instances, instances_2=None):
    choices = _get_cities_choices(instances, instances_2)
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


class SelectCityStudioForm(forms.Form):
    studios = DanceStudio.objects.all()
    instructors = Instructor.objects.all()

    city = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'chosen-select', 'style': 'min-width: 172px; width: 200px',
                                   'tabindex': '0',
                                   'data-placeholder': "Выберите город...",
                                   'onchange': 'this.form.submit();'}),
        choices=_get_cities_choices(studios, instructors)
    )

    def __init__(self, *args, **kwargs):
        studios = DanceStudio.objects.all()
        instructors = Instructor.objects.all()

        # first call parent's constructor
        super(SelectCityStudioForm, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['city'].required = False
        self.fields['city'].choices = _get_cities_choices(studios, instructors)
        self.initial['city'] = _get_default_kyiv_or_another_city(studios, instructors)


class SelectCityShopForm(forms.Form):
    shops = DanceShop.objects.all()

    city = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'chosen-select', 'style': 'min-width: 172px; width: 200px',
                                   'tabindex': '0',
                                   'data-placeholder': "Выберите город...",
                                   'onchange': 'this.form.submit();'}),
        choices=_get_cities_choices(shops)
    )

    def __init__(self, *args, **kwargs):
        shops = DanceShop.objects.all()
        # first call parent's constructor
        super(SelectCityShopForm, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['city'].required = False
        self.fields['city'].choices = _get_cities_choices(shops)
        self.initial['city'] = _get_default_kyiv_or_another_city(shops)


class SelectCityHallForm(forms.Form):
    halls = DanceHall.objects.all()

    city = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'chosen-select', 'style': 'min-width: 172px; width: 200px',
                                   'tabindex': '0',
                                   'data-placeholder': "Выберите город...",
                                   'onchange': 'this.form.submit();'}),
        choices=_get_cities_choices(halls)
    )

    def __init__(self, *args, **kwargs):
        halls = DanceHall.objects.all()
        # first call parent's constructor
        super(SelectCityHallForm, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['city'].required = False
        self.fields['city'].choices = _get_cities_choices(halls)
        self.initial['city'] = _get_default_kyiv_or_another_city(halls)


def _get_place_types_choices(places):
    place_type_dict = PlaceType.PLACE_TYPE_DICT

    place_types_per_places = [[(place_type.pk, place_type_dict.get(place_type.title, place_type.title))
                               for place_type in place.place_types.all()]
                              for place in places]

    place_types_choices = []
    for place_types_per_place in place_types_per_places:
        place_types_choices.extend(place_types_per_place)
    place_types_choices = tuple(set(place_types_choices))

    return place_types_choices


def _get_shop_types_choices(shops):
    shop_type_dict = ShopType.SHOP_TYPE_DICT

    shop_types_per_shops = [[(shop_type.pk, shop_type_dict.get(shop_type.title, shop_type.title))
                              for shop_type in shop.shop_types.all()]
                             for shop in shops]
    shop_types_choices = []
    for shop_types_per_shop in shop_types_per_shops:
        shop_types_choices.extend(shop_types_per_shop)
    shop_types_choices = tuple(set(shop_types_choices))

    return shop_types_choices


def _get_dance_styles_choices(dance_styles, instances, instances_2=None):
    direction_dict = DanceStyle.DIRECTION_SHOW
    all_directions = set([dance_style.direction for dance_style in dance_styles])

    styles_per_instance = [[(dance_style.direction, dance_style.pk, dance_style.title)
                            for dance_style in instance.dance_styles.all()]
                           for instance in instances]
    styles_per_instance_2 = []
    if instances_2:
        styles_per_instance_2 = [[(dance_style.direction, dance_style.pk, dance_style.title)
                                for dance_style in instance.dance_styles.all()]
                               for instance in instances_2]
    all_dance_styles = []
    for j in styles_per_instance:
        all_dance_styles.extend(j)
    if instances_2:
        for j in styles_per_instance_2:
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
                                   'data-placeholder': "Выберите город..."}),
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


class StudiosFilterForm(forms.Form):
    studios = DanceStudio.objects.all()
    instructors = Instructor.objects.all()
    dance_styles = DanceStyle.objects.all()

    dance_styles = forms.MultipleChoiceField(
        widget=forms.SelectMultiple(attrs={'class': 'chosen-select', 'style': 'min-width: 172px; width: 100%',
                                           'tabindex': '0',
                                           'data-placeholder': "Выберите танцевальные стили..."}),
        choices=_get_dance_styles_choices(dance_styles, studios, instructors)
    )

    city = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'chosen-select', 'style': 'min-width: 172px; width: 100%',
                                   'tabindex': '0',
                                   'data-placeholder': "Выберите город..."}),
        choices=_get_cities_choices(studios, instructors)
    )

    def __init__(self, *args, **kwargs):
        studios = DanceStudio.objects.all()
        instructors = Instructor.objects.all()
        dance_styles = DanceStyle.objects.all()

        # first call parent's constructor
        super(StudiosFilterForm, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['dance_styles'].required = False
        self.fields['dance_styles'].label = 'Танцевальные стили'
        self.fields['dance_styles'].choices = _get_dance_styles_choices(dance_styles, studios, instructors)
        self.fields['city'].label = 'Город'
        self.fields['city'].choices = _get_cities_choices(studios, instructors)


class ShopsFilterForm(forms.Form):
    shops = DanceShop.objects.all()

    shop_types = forms.MultipleChoiceField(
        widget=forms.SelectMultiple(attrs={'class': 'chosen-select', 'style': 'min-width: 172px; width: 100%',
                                           'tabindex': '0',
                                           'data-placeholder': "Выберите типы..."}),
        choices=_get_shop_types_choices(shops)
    )

    city = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'chosen-select', 'style': 'min-width: 172px; width: 100%',
                                   'tabindex': '0',
                                   'data-placeholder': "Выберите город..."}),
        choices=_get_cities_choices(shops)
    )

    def __init__(self, *args, **kwargs):
        shops = DanceShop.objects.all()
        # first call parent's constructor
        super(ShopsFilterForm, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['shop_types'].required = False
        self.fields['shop_types'].label = 'Типы магазинов'
        self.fields['shop_types'].choices = _get_shop_types_choices(shops)
        self.fields['city'].label = 'Город'
        self.fields['city'].choices = _get_cities_choices(shops)


class HallsFilterForm(forms.Form):
    halls = DanceHall.objects.all()

    # shop_types = forms.MultipleChoiceField(
    #     widget=forms.SelectMultiple(attrs={'class': 'chosen-select', 'style': 'min-width: 172px; width: 100%',
    #                                        'tabindex': '0',
    #                                        'data-placeholder': "Выберите типы..."}),
    #     choices=_get_hall_types_choices(halls)
    # )

    city = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'chosen-select', 'style': 'min-width: 172px; width: 100%',
                                   'tabindex': '0',
                                   'data-placeholder': "Выберите город..."}),
        choices=_get_cities_choices(halls)
    )

    def __init__(self, *args, **kwargs):
        halls = DanceHall.objects.all()
        # first call parent's constructor
        super(HallsFilterForm, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        # self.fields['shop_types'].required = False
        # self.fields['shop_types'].label = 'Типы магазинов'
        # self.fields['shop_types'].choices = _get_shop_types_choices(shops)
        self.fields['city'].label = 'Город'
        self.fields['city'].choices = _get_cities_choices(halls)
