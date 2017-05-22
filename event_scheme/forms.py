from django import forms
from entities.models import EventType, Event, DanceStyle


def _get_event_types_choices(events):
    event_type_dict = EventType.EVENT_TYPE_DICT

    event_types_per_events = [[(event_type.pk, event_type_dict.get(event_type.title, event_type.title))
                               for event_type in event.event_types.all()]
                              for event in events]

    event_types_choices = []
    for event_types_per_event in event_types_per_events:
        event_types_choices.extend(event_types_per_event)
    event_types_choices = tuple(set(event_types_choices))

    return event_types_choices


def _get_dance_styles_choices(dance_styles, events):
    direction_dict = DanceStyle.DIRECTION_SHOW
    all_directions = set([dance_style.direction for dance_style in dance_styles])

    styles_per_event = [[(dance_style.direction, dance_style.pk, dance_style.title)
                         for dance_style in event.dance_styles.all()]
                        for event in events]
    all_dance_styles = []
    for j in styles_per_event:
        all_dance_styles.extend(j)
    all_dance_styles = tuple(set(all_dance_styles))

    dance_styles_choices = ([(direction_dict.get(dance_direction, dance_direction),
                              tuple([(i[1], i[2]) for i in [dance_style for dance_style in all_dance_styles]
                                     if i[0] == dance_direction])) for dance_direction in all_directions][0],)
    return dance_styles_choices


def _get_cities_choices(events):
    cities_per_events = [[(loc.city.pk, loc.city.city) for loc in event.locations.all() if loc.city]
                         for event in events]
    all_cities = []
    for cities_per_event in cities_per_events:
        all_cities.extend(cities_per_event)
    all_cities = tuple(set(all_cities))
    return all_cities


class EventsFilterForm(forms.Form):
    events = Event.objects.all()
    dance_styles = DanceStyle.objects.all()

    EVENT_TYPES_CHOICES = _get_event_types_choices(events)
    event_types = forms.MultipleChoiceField(
        widget=forms.SelectMultiple(attrs={'class': 'chosen-select', 'style': 'min-width: 210px; width: 100%',
                                           'tabindex': '0',
                                           'data-placeholder': "Выберите типы..."}),
        choices=EVENT_TYPES_CHOICES
    )

    DANCE_STYLES_CHOICES = _get_dance_styles_choices(dance_styles, events)
    dance_styles = forms.MultipleChoiceField(
        widget=forms.SelectMultiple(attrs={'class': 'chosen-select', 'style': 'min-width: 210px; width: 100%',
                                           'tabindex': '0',
                                           'data-placeholder': "Выберите танцевальные стили..."}),
        choices=DANCE_STYLES_CHOICES
    )

    CITIES_CHOICES = _get_cities_choices(events)
    cities = forms.MultipleChoiceField(
        widget=forms.SelectMultiple(attrs={'class': 'chosen-select', 'style': 'min-width: 210px; width: 100%',
                                           'tabindex': '0',
                                           'data-placeholder': "Выберите города..."}),
        choices=CITIES_CHOICES
    )

    def __init__(self, *args, **kwargs):
        events = Event.objects.all()
        dance_styles = DanceStyle.objects.all()

        # first call parent's constructor
        super(EventsFilterForm, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['event_types'].required = False
        self.fields['event_types'].choices = _get_event_types_choices(events)
        self.fields['dance_styles'].required = False
        self.fields['dance_styles'].choices = _get_dance_styles_choices(dance_styles, events)
        self.fields['cities'].required = False
        self.fields['cities'].choices = _get_cities_choices(events)
