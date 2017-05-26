from django import forms

from dance_styles.models import DanceStyleInSectionCountType, DanceStyleInSectionBetweenPartnersDistance, \
    DanceStyleInSectionAveragePrice, \
    DanceStyleInSectionAttendeeAge


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
