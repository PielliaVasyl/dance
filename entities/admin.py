from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import UserProfile, Event, Location, EventType, DanceType, Link
from .forms import EventForm, LocationForm, EventTypeForm, DanceTypeForm, LinkForm


class UserProfileInline(admin.StackedInline):
    model = UserProfile


class UserProfileAdmin(UserAdmin):
    list_display = ('username', "first_name", "last_name", "email", 'get_role', "is_staff")
    inlines = (UserProfileInline, )

    def get_role(self, instance):
        return instance.userprofile.role
    get_role.short_description = 'Role'

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(UserProfileAdmin, self).get_inline_instances(request, obj)

admin.site.unregister(User)
admin.site.register(User, UserProfileAdmin)


class EventAdmin(admin.ModelAdmin):
    list_display = ["title", "note", "status", 'start_date', 'end_date', 'duration', "get_event_types",
                    "get_dance_types", "get_locations", 'get_links', "author", 'created', 'updated']
    form = EventForm

    def duration(self, instance):
        if instance.start_date and instance.end_date:
            return '%s day(s)' % str(int((instance.end_date - instance.start_date).days) + 1)
        return '0 days'

admin.site.register(Event, EventAdmin)


class LocationAdmin(admin.ModelAdmin):
    list_display = ["title", 'description', "address", "city", "get_dance_types", "author", 'created', 'updated']
    form = LocationForm

admin.site.register(Location, LocationAdmin)


class EventTypeAdmin(admin.ModelAdmin):
    list_display = ["title", 'description', "author", 'created', 'updated']
    form = EventTypeForm

admin.site.register(EventType, EventTypeAdmin)


class DanceTypeAdmin(admin.ModelAdmin):
    list_display = ["title", 'description', 'image', "author", 'created', 'updated']
    form = DanceTypeForm

admin.site.register(DanceType, DanceTypeAdmin)


class LinkAdmin(admin.ModelAdmin):
    list_display = ["link", "author", 'created', 'updated']
    form = LinkForm

admin.site.register(Link, LinkAdmin)
