from django import forms

from classes.models import WeekDay


class WeekDayForm(forms.ModelForm):
    class Meta:
        model = WeekDay
        fields = ["day"]
