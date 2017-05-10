from django import forms

from dance_styles.models import CountType, BetweenPartnersDistance, AveragePrice


class CountTypeForm(forms.ModelForm):
    class Meta:
        model = CountType
        fields = ["count_type"]


class BetweenPartnersDistanceForm(forms.ModelForm):
    class Meta:
        model = BetweenPartnersDistance
        fields = ["distance"]


class AveragePriceForm(forms.ModelForm):
    class Meta:
        model = AveragePrice
        fields = ["price"]
