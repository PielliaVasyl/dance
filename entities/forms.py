# coding: utf-8
from django import forms
from .models import Event, Location, EventType, DanceType, Link, Instructor, DanceStudio, DanceClass, WeekDay, Article, \
    VisitorMessage, DanceHallPhoto, DanceHall, DanceShopPhoto, DanceShop, Contacts, Socials, SocialLinkFB, SocialLinkVK, \
    SocialLinkInstagram, SocialLinkTwitter


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ["title", 'description', "note", "status", 'start_date', 'end_date', "event_types", "dance_types",
                  "locations", 'links', "author"]

    def clean(self):
        cleaned_data = super(EventForm, self).clean()
        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")

        if start_date and end_date:
            if end_date < start_date:
                raise forms.ValidationError("End date cannot be earlier than start date!")
        return cleaned_data


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ["title", 'description', 'show_in_map_section', "address", "city", "dance_types", "author"]


class EventTypeForm(forms.ModelForm):
    class Meta:
        model = EventType
        fields = ["title", 'description', "author"]


class DanceTypeForm(forms.ModelForm):
    class Meta:
        model = DanceType
        fields = ["title", 'description', 'image', "author"]


class SocialLinkFBForm(forms.ModelForm):
    class Meta:
        model = SocialLinkFB
        fields = ['link', "author"]


class SocialLinkVKForm(forms.ModelForm):
    class Meta:
        model = SocialLinkVK
        fields = ['link', "author"]


class SocialLinkInstagramForm(forms.ModelForm):
    class Meta:
        model = SocialLinkInstagram
        fields = ['link', "author"]


class SocialLinkTwitterForm(forms.ModelForm):
    class Meta:
        model = SocialLinkTwitter
        fields = ['link', "author"]


class SocialsForm(forms.ModelForm):
    class Meta:
        model = Socials
        fields = ['title', 'fb', 'vk', 'instagram', 'twitter', "author"]


class ContactsForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = ['title', 'phone_number', 'socials', "author"]


class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ["link", "author"]


class InstructorForm(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = ["name", 'description', 'dance_types', 'links', 'events', "author"]


class DanceStudioForm(forms.ModelForm):
    class Meta:
        model = DanceStudio
        fields = ["title", 'description', 'logo', 'locations', 'links', 'instructors', 'dance_types', "author"]


class WeekDayForm(forms.ModelForm):
    class Meta:
        model = WeekDay
        fields = ["day"]


class DanceClassForm(forms.ModelForm):
    class Meta:
        model = DanceClass
        fields = ["title", 'description', 'is_opened_lesson', 'is_probably_free', 'first_lesson_free',
                  'free_lesson_date', 'every_first_lesson_free', 'start_date', 'end_date', 'schedule_week_days',
                  'dance_studio', 'dance_types', 'instructors', 'links', "author"]


class DanceHallPhotoForm(forms.ModelForm):
    class Meta:
        model = DanceHallPhoto
        fields = ["title", 'description', 'photo', "author"]


class DanceHallForm(forms.ModelForm):
    class Meta:
        model = DanceHall
        fields = ["title", 'description', 'photos', 'locations', 'links', "author"]


class DanceShopPhotoForm(forms.ModelForm):
    class Meta:
        model = DanceShopPhoto
        fields = ["title", 'description', 'photo', "author"]


class DanceShopForm(forms.ModelForm):
    class Meta:
        model = DanceShop
        fields = ["title", 'description', 'photos', 'locations', 'links', "author"]


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'description', 'image', 'is_linked_article', 'article_link', "author"]


class VisitorMessageForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(VisitorMessageForm, self).__init__(*args, **kwargs)

        self.fields['visitor_name'].label = "Как к Вам обращаться?"
        self.fields['visitor_email'].label = "Ваш email"
        self.fields['visitor_phone_number'].label = "Ваш номер телефона"
        self.fields['message_subject'].label = "Тема Вашего письма"
        self.fields['message_text'].label = "Текст письма"

    class Meta:
        model = VisitorMessage
        fields = ['visitor_name', 'visitor_email', 'visitor_phone_number', 'message_subject', 'message_text']
