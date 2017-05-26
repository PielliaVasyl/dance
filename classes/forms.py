from django import forms

from classes.models import WeekDay
from entities.models import DanceClassType, DanceClass, DanceStyle, DanceClassPriceType, DanceClassExperienceLevel, \
    DanceStyleDirection


class WeekDayForm(forms.ModelForm):
    class Meta:
        model = WeekDay
        fields = ["day"]


def _get_dance_class_types_choices(dance_classes):
    dance_class_type_dict = DanceClassType.DANCE_CLASS_TYPE_DICT
    dance_class_types_per_dance_classes = [[(dance_class_type.pk,
                                             dance_class_type_dict.get(dance_class_type.title, dance_class_type.title))
                                            for dance_class_type in dance_class.dance_class_types.all()]
                                           for dance_class in dance_classes]

    dance_class_types_choices = []
    for dance_class_types_per_dance_class in dance_class_types_per_dance_classes:
        dance_class_types_choices.extend(dance_class_types_per_dance_class)
    dance_class_types_choices = tuple(set(dance_class_types_choices))

    return dance_class_types_choices


def _get_dance_styles_choices(dance_styles, dance_classes):
    direction_dict = DanceStyleDirection.DIRECTION_SHOW
    all_directions = set([dance_style.direction for dance_style in dance_styles])

    styles_per_dance_classes = [[(dance_style.direction, dance_style.pk, dance_style.title)
                                 for dance_style in dance_class.dance_styles.all()]
                                for dance_class in dance_classes]

    all_dance_styles = []
    for styles_per_dance_class in styles_per_dance_classes:
        all_dance_styles.extend(styles_per_dance_class)

    all_dance_styles = tuple(set(all_dance_styles))

    dance_styles_choices = ([(direction_dict.get(dance_direction, dance_direction),
                              tuple([(i[1], i[2]) for i in [dance_style for dance_style in all_dance_styles]
                                     if i[0] == dance_direction])) for dance_direction in all_directions][0],)
    return dance_styles_choices


def _get_price_types_choices(dance_classes):
    dance_class_price_type_dict = DanceClassPriceType.DANCE_CLASS_PRICE_TYPE_DICT
    price_types_per_dance_classes = [[(price_type.pk,
                                       dance_class_price_type_dict.get(price_type.title, price_type.title))
                                      for price_type in dance_class.price_types.all()]
                                     for dance_class in dance_classes]

    price_types_choices = []
    for price_types_per_dance_class in price_types_per_dance_classes:
        price_types_choices.extend(price_types_per_dance_class)
    price_types_choices = tuple(set(price_types_choices))

    return price_types_choices


def _get_dance_studios_choices(dance_classes):
    dance_studios_per_dance_classes = [(dance_class.dance_studio.pk, dance_class.dance_studio.title)
                                       for dance_class in dance_classes if dance_class.dance_studio]
    return dance_studios_per_dance_classes


def _get_experience_levels_choices(dance_classes):
    experience_levels_dict = DanceClassExperienceLevel.EXPERIENCE_LEVEL_DICT
    experience_levels_per_dance_classes = [[(experience_level.pk,
                                             experience_levels_dict.get(experience_level.title, experience_level.title))
                                            for experience_level in dance_class.experience_levels.all()]
                                           for dance_class in dance_classes]

    experience_levels_choices = []
    for experience_levels_per_dance_class in experience_levels_per_dance_classes:
        experience_levels_choices.extend(experience_levels_per_dance_class)
    experience_levels_choices = tuple(set(experience_levels_choices))

    return experience_levels_choices


class DanceClassFilterForm(forms.Form):
    # dance_classes = DanceClass.objects.all()
    # dance_styles = DanceStyle.objects.all()
    #
    # DANCE_CLASS_TYPES_CHOICES = _get_dance_class_types_choices(dance_classes)
    dance_class_types = forms.MultipleChoiceField(
        widget=forms.SelectMultiple(attrs={'class': 'chosen-select', 'style': 'min-width: 172px; width: 100%',
                                           'tabindex': '0',
                                           'data-placeholder': "Выберите типы..."}),
        # choices=DANCE_CLASS_TYPES_CHOICES
    )

    # DANCE_STYLES_CHOICES = _get_dance_styles_choices(dance_styles, dance_classes)
    dance_styles = forms.MultipleChoiceField(
        widget=forms.SelectMultiple(attrs={'class': 'chosen-select', 'style': 'min-width: 172px; width: 100%',
                                           'tabindex': '0',
                                           'data-placeholder': "Выберите танцевальные стили..."}),
        # choices=DANCE_STYLES_CHOICES
    )

    # PRICE_TYPES_CHOICES = _get_price_types_choices(dance_classes)
    price_types = forms.MultipleChoiceField(
        widget=forms.SelectMultiple(attrs={'class': 'chosen-select', 'style': 'min-width: 172px; width: 100%',
                                           'tabindex': '0',
                                           'data-placeholder': "Выберите типы стоимости..."}),
        # choices=PRICE_TYPES_CHOICES
    )

    # DANCE_STUDIOS_CHOICES = _get_dance_studios_choices(dance_classes)
    dance_studios = forms.MultipleChoiceField(
        widget=forms.SelectMultiple(attrs={'class': 'chosen-select', 'style': 'min-width: 172px; width: 100%',
                                           'tabindex': '0',
                                           'data-placeholder': "Выберите школы..."}),
        # choices=DANCE_STUDIOS_CHOICES
    )

    # EXPERIENCE_LEVELS_CHOICES = _get_experience_levels_choices(dance_classes)
    experience_levels = forms.MultipleChoiceField(
        widget=forms.SelectMultiple(attrs={'class': 'chosen-select', 'style': 'min-width: 172px; width: 100%',
                                           'tabindex': '0',
                                           'data-placeholder': "Выберите уровень опыта..."}),
        # choices=EXPERIENCE_LEVELS_CHOICES
    )

    def __init__(self, *args, **kwargs):
        dance_classes = DanceClass.objects.all()
        dance_styles = DanceStyle.objects.all()

        # first call parent's constructor
        super(DanceClassFilterForm, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['dance_class_types'].required = False
        self.fields['dance_class_types'].choices = _get_dance_class_types_choices(dance_classes)
        self.fields['dance_styles'].required = False
        self.fields['dance_styles'].choices = _get_dance_styles_choices(dance_styles, dance_classes)
        self.fields['price_types'].required = False
        self.fields['price_types'].choices = _get_price_types_choices(dance_classes)
        self.fields['dance_studios'].required = False
        self.fields['dance_studios'].choices = _get_dance_studios_choices(dance_classes)
        self.fields['experience_levels'].required = False
        self.fields['experience_levels'].choices = _get_experience_levels_choices(dance_classes)
