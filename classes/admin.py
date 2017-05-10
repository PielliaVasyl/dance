from django.contrib import admin

from classes.models import WeekDay
from classes.forms import WeekDayForm


class WeekDayAdmin(admin.ModelAdmin):
    list_display = ["day"]
    form = WeekDayForm

admin.site.register(WeekDay, WeekDayAdmin)
