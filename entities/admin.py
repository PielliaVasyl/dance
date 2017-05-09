from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import UserProfile, Event, EventType, DanceType, Link, Instructor, DanceStudio, DanceClass, \
    WeekDay, Article, VisitorMessage, DanceHallPhoto, DanceHall, DanceShopPhoto, DanceShop, Contacts, Socials, \
    SocialLinkVK, SocialLinkFB, SocialLinkInstagram, SocialLinkTwitter, PlaceInMap, PlaceInMapLocation, \
    PlaceInMapMapCoordinates, DanceStudioMapCoordinates, DanceHallMapCoordinates, DanceShopMapCoordinates, \
    EventLocation, DanceStudioLocation, DanceHallLocation, DanceShopLocation, PhoneNumber
from .forms import EventForm, EventTypeForm, DanceTypeForm, LinkForm, InstructorForm, DanceStudioForm, \
    DanceClassForm, WeekDayForm, ArticleForm, VisitorMessageForm, DanceHallPhotoForm, DanceHallForm, \
    DanceShopPhotoForm, DanceShopForm, ContactsForm, SocialsForm, SocialLinkVKForm, SocialLinkFBForm, \
    SocialLinkInstagramForm, SocialLinkTwitterForm, PlaceInMapForm, PlaceInMapLocationForm, \
    PlaceInMapMapCoordinatesForm, DanceStudioMapCoordinatesForm, DanceHallMapCoordinatesForm, \
    DanceShopMapCoordinatesForm, EventLocationForm, DanceStudioLocationForm, DanceHallLocationForm, \
    DanceShopLocationForm, PhoneNumberForm


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


class SocialLinkVKAdmin(admin.ModelAdmin):
    list_display = ['link', "author", 'created', 'updated']
    form = SocialLinkVKForm

admin.site.register(SocialLinkVK, SocialLinkVKAdmin)


class SocialLinkFBAdmin(admin.ModelAdmin):
    list_display = ['link', "author", 'created', 'updated']
    form = SocialLinkFBForm

admin.site.register(SocialLinkFB, SocialLinkFBAdmin)


class SocialLinkInstagramAdmin(admin.ModelAdmin):
    list_display = ['link', "author", 'created', 'updated']
    form = SocialLinkInstagramForm

admin.site.register(SocialLinkInstagram, SocialLinkInstagramAdmin)


class SocialLinkTwitterAdmin(admin.ModelAdmin):
    list_display = ['link', "author", 'created', 'updated']
    form = SocialLinkTwitterForm

admin.site.register(SocialLinkTwitter, SocialLinkTwitterAdmin)


class SocialsAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_fbs', 'get_vks', 'get_instagrams', 'get_twitters', "author", 'created', 'updated']
    form = SocialsForm

admin.site.register(Socials, SocialsAdmin)


class PhoneNumberAdmin(admin.ModelAdmin):
    list_display = ['phone_number', "author", 'created', 'updated']
    form = PhoneNumberForm

admin.site.register(PhoneNumber, PhoneNumberAdmin)


class ContactsAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_phone_numbers', 'socials', "author", 'created', 'updated']
    form = ContactsForm

admin.site.register(Contacts, ContactsAdmin)


class LinkAdmin(admin.ModelAdmin):
    list_display = ["link", "author", 'created', 'updated']
    form = LinkForm

admin.site.register(Link, LinkAdmin)


class DanceTypeAdmin(admin.ModelAdmin):
    list_display = ["title", 'short_description', 'image', "author", 'created', 'updated']
    form = DanceTypeForm

admin.site.register(DanceType, DanceTypeAdmin)


class EventTypeAdmin(admin.ModelAdmin):
    list_display = ["title", 'short_description', "author", 'created', 'updated']
    form = EventTypeForm

admin.site.register(EventType, EventTypeAdmin)


class PlaceInMapMapCoordinatesAdmin(admin.ModelAdmin):
    list_display = ["lat", 'lng', "author", 'created', 'updated']
    form = PlaceInMapMapCoordinatesForm

admin.site.register(PlaceInMapMapCoordinates, PlaceInMapMapCoordinatesAdmin)


class DanceStudioMapCoordinatesAdmin(admin.ModelAdmin):
    list_display = ["lat", 'lng', "author", 'created', 'updated']
    form = DanceStudioMapCoordinatesForm

admin.site.register(DanceStudioMapCoordinates, DanceStudioMapCoordinatesAdmin)


class DanceHallMapCoordinatesAdmin(admin.ModelAdmin):
    list_display = ["lat", 'lng', "author", 'created', 'updated']
    form = DanceHallMapCoordinatesForm

admin.site.register(DanceHallMapCoordinates, DanceHallMapCoordinatesAdmin)


class DanceShopMapCoordinatesAdmin(admin.ModelAdmin):
    list_display = ["lat", 'lng', "author", 'created', 'updated']
    form = DanceShopMapCoordinatesForm

admin.site.register(DanceShopMapCoordinates, DanceShopMapCoordinatesAdmin)


class PlaceInMapLocationAdmin(admin.ModelAdmin):
    list_display = ["address", "city", 'coordinates', "author", 'created', 'updated']
    form = PlaceInMapLocationForm

admin.site.register(PlaceInMapLocation, PlaceInMapLocationAdmin)


class EventLocationAdmin(admin.ModelAdmin):
    list_display = ["address", "city", "author", 'created', 'updated']
    form = EventLocationForm

admin.site.register(EventLocation, EventLocationAdmin)


class DanceStudioLocationAdmin(admin.ModelAdmin):
    list_display = ["address", "city", 'coordinates', "author", 'created', 'updated']
    form = DanceStudioLocationForm

admin.site.register(DanceStudioLocation, DanceStudioLocationAdmin)


class DanceHallLocationAdmin(admin.ModelAdmin):
    list_display = ["address", "city", 'coordinates', "author", 'created', 'updated']
    form = DanceHallLocationForm

admin.site.register(DanceHallLocation, DanceHallLocationAdmin)


class DanceShopLocationAdmin(admin.ModelAdmin):
    list_display = ["address", "city", 'coordinates', "author", 'created', 'updated']
    form = DanceShopLocationForm

admin.site.register(DanceShopLocation, DanceShopLocationAdmin)


class PlaceInMapAdmin(admin.ModelAdmin):
    list_display = ["title", 'short_description', 'image', 'get_locations', "get_dance_types", "author", 'created',
                    'updated']
    form = PlaceInMapForm

admin.site.register(PlaceInMap, PlaceInMapAdmin)


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


class InstructorAdmin(admin.ModelAdmin):
    list_display = ["name", 'short_description', 'get_dance_types', 'get_events', 'get_links', 'contacts', "author",
                    'created', 'updated']
    form = InstructorForm

admin.site.register(Instructor, InstructorAdmin)


class DanceStudioAdmin(admin.ModelAdmin):
    list_display = ["title", 'short_description', 'get_dance_types', 'get_links', 'get_instructors', 'get_locations',
                    'contacts', "author", 'created', 'updated']
    form = DanceStudioForm

admin.site.register(DanceStudio, DanceStudioAdmin)


class WeekDayAdmin(admin.ModelAdmin):
    list_display = ["day"]
    form = WeekDayForm

admin.site.register(WeekDay, WeekDayAdmin)


class DanceClassAdmin(admin.ModelAdmin):
    list_display = ["title", 'short_description', 'is_opened_lesson', 'is_probably_free', 'first_lesson_free',
                    'free_lesson_date', 'every_first_lesson_free', 'experience_level', 'start_date', 'end_date',
                    'get_schedule_week_days', 'dance_studio', 'get_dance_types', 'get_instructors', 'get_links',
                    "author", 'created', 'updated']
    form = DanceClassForm

admin.site.register(DanceClass, DanceClassAdmin)


class DanceHallPhotoAdmin(admin.ModelAdmin):
    list_display = ["title", 'description', 'photo', "author", 'created', 'updated']
    form = DanceHallPhotoForm

admin.site.register(DanceHallPhoto, DanceHallPhotoAdmin)


class DanceHallAdmin(admin.ModelAdmin):
    list_display = ["title", 'short_description', 'count_photos', 'get_locations', 'get_links', 'contacts', "author",
                    'created', 'updated']
    form = DanceHallForm

admin.site.register(DanceHall, DanceHallAdmin)


class DanceShopPhotoAdmin(admin.ModelAdmin):
    list_display = ["title", 'description', 'photo', "author", 'created', 'updated']
    form = DanceShopPhotoForm

admin.site.register(DanceShopPhoto, DanceShopPhotoAdmin)


class DanceShopAdmin(admin.ModelAdmin):
    list_display = ["title", 'short_description', 'count_photos', 'get_locations', 'get_links', 'contacts', "author",
                    'created', 'updated']
    form = DanceShopForm

admin.site.register(DanceShop, DanceShopAdmin)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'short_description', 'image', 'is_linked_article', 'article_link', "author", 'created',
                    'updated']
    form = ArticleForm

admin.site.register(Article, ArticleAdmin)


class VisitorMessageAdmin(admin.ModelAdmin):
    list_display = ['visitor_name', 'visitor_email', 'visitor_phone_number', 'message_subject', 'message_text',
                    'created', 'updated']
    form = VisitorMessageForm

admin.site.register(VisitorMessage, VisitorMessageAdmin)
