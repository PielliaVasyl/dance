from django.contrib import admin

from dance_styles.forms import DanceStyleInSectionCountTypeForm, DanceStyleInSectionBetweenPartnersDistanceForm, \
    DanceStyleInSectionAveragePriceForm, DanceStyleInSectionAttendeeAgeForm
from dance_styles.models import DanceStyleInSectionCountType, DanceStyleInSectionBetweenPartnersDistance, \
    DanceStyleInSectionAveragePrice, DanceStyleInSectionAttendeeAge


class DanceStyleInSectionCountTypeAdmin(admin.ModelAdmin):
    list_display = ["count_type"]
    form = DanceStyleInSectionCountTypeForm

admin.site.register(DanceStyleInSectionCountType, DanceStyleInSectionCountTypeAdmin)


class DanceStyleInSectionBetweenPartnersDistanceAdmin(admin.ModelAdmin):
    list_display = ["distance"]
    form = DanceStyleInSectionBetweenPartnersDistanceForm

admin.site.register(DanceStyleInSectionBetweenPartnersDistance, DanceStyleInSectionBetweenPartnersDistanceAdmin)


class DanceStyleInSectionAveragePriceAdmin(admin.ModelAdmin):
    list_display = ["price"]
    form = DanceStyleInSectionAveragePriceForm

admin.site.register(DanceStyleInSectionAveragePrice, DanceStyleInSectionAveragePriceAdmin)


class DanceStyleInSectionAttendeeAgeAdmin(admin.ModelAdmin):
    list_display = ["attendee_age"]
    form = DanceStyleInSectionAttendeeAgeForm

admin.site.register(DanceStyleInSectionAttendeeAge, DanceStyleInSectionAttendeeAgeAdmin)
