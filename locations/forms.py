from django import forms

from entities.models import City


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ["city"]
