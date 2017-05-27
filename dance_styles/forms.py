from django import forms

from dance_styles.models import DanceStyleInSectionCountType, DanceStyleInSectionBetweenPartnersDistance, \
    DanceStyleInSectionAveragePrice, DanceStyleInSectionAttendeeAge
from entities.models import DanceStyleInSection, DanceStyleDirection


class DanceStyleInSectionCountTypeForm(forms.ModelForm):
    class Meta:
        model = DanceStyleInSectionCountType
        fields = ["count_type"]


class DanceStyleInSectionBetweenPartnersDistanceForm(forms.ModelForm):
    class Meta:
        model = DanceStyleInSectionBetweenPartnersDistance
        fields = ["distance"]


class DanceStyleInSectionAveragePriceForm(forms.ModelForm):
    class Meta:
        model = DanceStyleInSectionAveragePrice
        fields = ["price"]


class DanceStyleInSectionAttendeeAgeForm(forms.ModelForm):
    class Meta:
        model = DanceStyleInSectionAttendeeAge
        fields = ["attendee_age"]


# ===========================================================================

def _get_titles_choices(dance_style_in_section_list):
    titles_choices = [(dance_style_in_section.pk, dance_style_in_section.title)
                      for dance_style_in_section in dance_style_in_section_list]

    return titles_choices


def _get_directions_choices(dance_style_in_section_list):
    direction_show = DanceStyleDirection.DIRECTION_SHOW
    directions_choices = [(dance_style_in_section.dance_style.direction.pk,
                           direction_show.get(dance_style_in_section.dance_style.direction.title,
                                              dance_style_in_section.dance_style.direction.title))
                          for dance_style_in_section in dance_style_in_section_list]
    if directions_choices:
        directions_choices = tuple(set(directions_choices))

    return directions_choices


def _get_count_types_choices(dance_style_in_section_list):
    count_type_dict = DanceStyleInSectionCountType.COUNT_TYPE_SHOW

    count_types_per_dance_style_in_section_list = [[(count_type.pk,
                                                     count_type_dict.get(count_type.count_type, count_type.count_type))
                                                    for count_type in dance_style_in_section.count_types.all()]
                                                   for dance_style_in_section in dance_style_in_section_list]

    count_types_choices = []
    for count_types_per_dance_style_in_section in count_types_per_dance_style_in_section_list:
        count_types_choices.extend(count_types_per_dance_style_in_section)
    count_types_choices = tuple(set(count_types_choices))

    return count_types_choices


def _get_distances_choices(dance_style_in_section_list):
    distance_dict = DanceStyleInSectionBetweenPartnersDistance.DISTANCE_SHOW

    distances_per_dance_style_in_section_list = \
        [[(distance.pk, distance_dict.get(distance.distance, distance.distance))
          for distance in dance_style_in_section.between_partners_distances.all()]
         for dance_style_in_section in dance_style_in_section_list]

    distances_choices = []
    for distances_per_dance_style_in_section in distances_per_dance_style_in_section_list:
        distances_choices.extend(distances_per_dance_style_in_section)
    distances_choices = tuple(set(distances_choices))

    return distances_choices


def _get_prices_choices(dance_style_in_section_list):
    price_dict = DanceStyleInSectionAveragePrice.PRICE_SHOW

    prices_per_dance_style_in_section_list = \
        [[(price.pk, price_dict.get(price.price, price.price))
          for price in dance_style_in_section.average_prices.all()]
         for dance_style_in_section in dance_style_in_section_list]

    prices_choices = []
    for prices_per_dance_style_in_section in prices_per_dance_style_in_section_list:
        prices_choices.extend(prices_per_dance_style_in_section)
    prices_choices = tuple(set(prices_choices))

    return prices_choices


class DanceStyleFilterForm(forms.Form):
    dance_style_in_section_list = DanceStyleInSection.objects.all()

    titles = forms.MultipleChoiceField(
        widget=forms.SelectMultiple(attrs={'class': 'chosen-select', 'style': 'min-width: 172px; width: 100%',
                                           'tabindex': '0',
                                           'data-placeholder': "Выберите по названию..."}),
        choices=_get_titles_choices(dance_style_in_section_list)
    )

    directions = forms.MultipleChoiceField(
        widget=forms.SelectMultiple(attrs={'class': 'chosen-select', 'style': 'min-width: 172px; width: 100%',
                                           'tabindex': '0',
                                           'data-placeholder': "Выберите направления..."}),
        choices=_get_directions_choices(dance_style_in_section_list)
    )

    count_types = forms.MultipleChoiceField(
        widget=forms.SelectMultiple(attrs={'class': 'chosen-select', 'style': 'min-width: 172px; width: 100%',
                                           'tabindex': '0',
                                           'data-placeholder': "Выберите количество..."}),
        choices=_get_count_types_choices(dance_style_in_section_list)
    )

    between_partners_distances = forms.MultipleChoiceField(
        widget=forms.SelectMultiple(attrs={'class': 'chosen-select', 'style': 'min-width: 172px; width: 100%',
                                           'tabindex': '0',
                                           'data-placeholder': "Выберите дистанции..."}),
        choices=_get_distances_choices(dance_style_in_section_list)
    )

    average_prices = forms.MultipleChoiceField(
        widget=forms.SelectMultiple(attrs={'class': 'chosen-select', 'style': 'min-width: 172px; width: 100%',
                                           'tabindex': '0',
                                           'data-placeholder': "Выберите цены..."}),
        choices=_get_prices_choices(dance_style_in_section_list)
    )

    # cities = forms.MultipleChoiceField(
    #     widget=forms.SelectMultiple(attrs={'class': 'chosen-select', 'style': 'min-width: 172px; width: 100%',
    #                                        'tabindex': '0',
    #                                        'data-placeholder': "Выберите города..."}),
    #     # choices=_get_cities_choices(events)
    # )

    def __init__(self, *args, **kwargs):
        dance_style_in_section_list = DanceStyleInSection.objects.all()

        # first call parent's constructor
        super(DanceStyleFilterForm, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['titles'].required = False
        self.fields['titles'].label = 'Название стиля'
        self.fields['titles'].choices = _get_titles_choices(dance_style_in_section_list)
        self.fields['directions'].required = False
        self.fields['directions'].label = 'Направление стиля'
        self.fields['directions'].choices = _get_directions_choices(dance_style_in_section_list)
        self.fields['count_types'].required = False
        self.fields['count_types'].label = 'Количество людей'
        self.fields['count_types'].choices = _get_count_types_choices(dance_style_in_section_list)
        self.fields['between_partners_distances'].required = False
        self.fields['between_partners_distances'].label = 'Расстояние между партнерами'
        self.fields['between_partners_distances'].choices = _get_distances_choices(dance_style_in_section_list)
        self.fields['average_prices'].required = False
        self.fields['average_prices'].label = 'Уровень цен'
        self.fields['average_prices'].choices = _get_prices_choices(dance_style_in_section_list)
