from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import UserProfile, Event, Location, EventType, DanceType, Link, Instructor, DanceStudio, DanceClass, \
    WeekDay
from .forms import EventForm, LocationForm, EventTypeForm, DanceTypeForm, LinkForm, InstructorForm, DanceStudioForm, \
    DanceClassForm, WeekDayForm


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

    @staticmethod
    def duration(instance):
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


class InstructorAdmin(admin.ModelAdmin):
    list_display = ["name", 'description', 'get_dance_types', 'get_events', 'get_links', "author", 'created', 'updated']
    form = InstructorForm

admin.site.register(Instructor, InstructorAdmin)


class DanceStudioAdmin(admin.ModelAdmin):
    list_display = ["title", 'description', 'get_dance_types', 'get_links', 'get_instructors', 'get_locations',
                    "author", 'created', 'updated']
    form = DanceStudioForm

admin.site.register(DanceStudio, DanceStudioAdmin)


class WeekDayAdmin(admin.ModelAdmin):
    list_display = ["day"]
    form = WeekDayForm

admin.site.register(WeekDay, WeekDayAdmin)


class DanceClassAdmin(admin.ModelAdmin):
    list_display = ["title", 'description', 'first_lesson_free', 'free_lesson_date', 'every_first_lesson_free',
                    'start_date', 'end_date', 'get_schedule_week_days', 'dance_studio', 'get_dance_types',
                    'get_instructors', 'get_links', "author", 'created', 'updated']
    form = DanceClassForm

admin.site.register(DanceClass, DanceClassAdmin)
