# coding: utf-8
from django import forms
from .models import Event, Location, EventType, DanceType, Link


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ["title", 'description', "note", "status", "event_types", "dance_types", "locations", 'links',
                  "author"]


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ["title", 'description', "address", "city", "dance_types", "author"]


class EventTypeForm(forms.ModelForm):
    class Meta:
        model = EventType
        fields = ["title", 'description', "author"]


class DanceTypeForm(forms.ModelForm):
    class Meta:
        model = DanceType
        fields = ["title", 'description', 'image', "author"]


class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ["link", "author"]
