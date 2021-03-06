# coding: utf-8
from django import forms
from .models import Event, Location, EventType, DanceType, Link


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ["title", 'description', "note", "status", 'start_date', 'end_date', "event_types", "dance_types",
                  "locations", 'links', "author"]

    def clean(self):
        cleaned_data = super(EventForm, self).clean()
        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")

        if start_date and end_date:
            if end_date < start_date:
                raise forms.ValidationError("End date cannot be earlier than start date!")
        return cleaned_data


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
