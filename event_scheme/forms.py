from django import forms
from entities.models import EventType, Event, DanceStyle


def get_dance_styles_choices(all_dance_styles, all_directions):
    return ([(dance_direction, tuple([(i[1], i[2]) for i in [dance_style for dance_style in all_dance_styles]
                                      if i[0] == dance_direction])) for dance_direction in all_directions][0],)


class EventsFilterForm(forms.Form):
    events = Event.objects.all()
    EVENT_TYPES_CHOICES = [(i.pk, EventType.EVENT_TYPE_DICT.get(i.title, i.title)) for i in EventType.objects.all()]
    event_types = forms.MultipleChoiceField(
        widget=forms.SelectMultiple(attrs={'class': 'chosen-select', 'style': 'min-width: 265px',
                                           'tabindex': '0',
                                           'data-placeholder': "Выберите типы..."}),
        choices=EVENT_TYPES_CHOICES
    )
    dance_styles = DanceStyle.objects.all()
    all_directions = set([dance_style.direction for dance_style in dance_styles])
    all_dance_styles = tuple(set([i[0] for i in [[(dance_style.direction, dance_style.pk, dance_style.title)
                                                  for dance_style in event.dance_styles.all()] for event in events]
                                  if i != []]))
    DANCE_STYLES_CHOICES = get_dance_styles_choices(all_dance_styles, all_directions)

    dance_styles = forms.MultipleChoiceField(
        widget=forms.SelectMultiple(attrs={'class': 'chosen-select', 'style': 'min-width: 265px',
                                           'tabindex': '0',
                                           'data-placeholder': "Выберите танцевальные стили..."}),
        choices=DANCE_STYLES_CHOICES
    )
    # get a tuple of all cities in events
    CITIES_CHOICES = tuple(set(
        [i[0] for i in [[(loc.city.pk, loc.city.city) for loc in event.locations.all() if loc.city] for event in events]
         if i != []]
    ))

    cities = forms.MultipleChoiceField(
        widget=forms.SelectMultiple(attrs={'class': 'chosen-select', 'style': 'min-width: 265px; width: 100%',
                                           'tabindex': '0',
                                           'data-placeholder': "Выберите города..."}),
        choices=CITIES_CHOICES
    )

    def __init__(self, *args, **kwargs):
        # first call parent's constructor
        super(EventsFilterForm, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['event_types'].required = False
        self.fields['dance_styles'].required = False
        self.fields['cities'].required = False
