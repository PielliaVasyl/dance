from django.contrib import admin

from entities.models import City
from locations.forms import CityForm


class CityAdmin(admin.ModelAdmin):
    list_display = ["city", 'created', 'updated']
    form = CityForm

admin.site.register(City, CityAdmin)
