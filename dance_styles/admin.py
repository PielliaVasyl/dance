from django.contrib import admin

from dance_styles.forms import CountTypeForm, BetweenPartnersDistanceForm, AveragePriceForm
from dance_styles.models import CountType, BetweenPartnersDistance, AveragePrice


class CountTypeAdmin(admin.ModelAdmin):
    list_display = ["count_type"]
    form = CountTypeForm

admin.site.register(CountType, CountTypeAdmin)


class BetweenPartnersDistanceAdmin(admin.ModelAdmin):
    list_display = ["distance"]
    form = BetweenPartnersDistanceForm

admin.site.register(BetweenPartnersDistance, BetweenPartnersDistanceAdmin)


class AveragePriceAdmin(admin.ModelAdmin):
    list_display = ["price"]
    form = AveragePriceForm

admin.site.register(AveragePrice, AveragePriceAdmin)
