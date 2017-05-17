# coding: utf-8
import datetime
from django import forms
from .models import Event, EventType, DanceStyle, Instructor, DanceStudio, DanceClass, Article, \
    VisitorMessage, DanceHallPhoto, DanceHall, DanceShopPhoto, DanceShop, Contacts, Socials, SocialLinkFB, \
    SocialLinkVK, SocialLinkInstagram, SocialLinkTwitter, PlaceInMap, PlaceInMapLocation, PlaceInMapMapCoordinates, \
    DanceStudioMapCoordinates, DanceHallMapCoordinates, DanceShopMapCoordinates, EventLocation, DanceStudioLocation, \
    DanceHallLocation, DanceShopLocation, PhoneNumber, EventLink, InstructorLink, DanceStudioLink, DanceClassLink, \
    DanceHallLink, DanceShopLink, LinkShouldKnowLink, PersonShouldKnowLink, OrganizationShouldKnowLink, LinkShouldKnow, \
    PersonShouldKnow, OrganizationShouldKnow, VideoWikiLink, AudioWikiLink, VideoWikiTag, AudioWikiTag, VideoWiki, \
    AudioWiki, AudioWikiPlaylistLink, VideoWikiPlaylistLink, PhotoWikiTag, PhotoWiki, VideoWikiPlaylist, \
    AudioWikiPlaylist, PhotoWikiAlbum


class SocialLinkVKForm(forms.ModelForm):
    class Meta:
        model = SocialLinkVK
        fields = ['link', "author"]


class SocialLinkFBForm(forms.ModelForm):
    class Meta:
        model = SocialLinkFB
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


class PhoneNumberForm(forms.ModelForm):
    class Meta:
        model = PhoneNumber
        fields = ['phone_number', "author"]


class ContactsForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = ['title', 'phone_numbers', 'socials', "author"]


class LinkShouldKnowLinkForm(forms.ModelForm):
    class Meta:
        model = LinkShouldKnowLink
        fields = ["link", "author"]


class PersonShouldKnowLinkForm(forms.ModelForm):
    class Meta:
        model = PersonShouldKnowLink
        fields = ["link", "author"]


class OrganizationShouldKnowLinkForm(forms.ModelForm):
    class Meta:
        model = OrganizationShouldKnowLink
        fields = ["link", "author"]


class EventLinkForm(forms.ModelForm):
    class Meta:
        model = EventLink
        fields = ["link", "author"]


class InstructorLinkForm(forms.ModelForm):
    class Meta:
        model = InstructorLink
        fields = ["link", "author"]


class DanceStudioLinkForm(forms.ModelForm):
    class Meta:
        model = DanceStudioLink
        fields = ["link", "author"]


class DanceClassLinkForm(forms.ModelForm):
    class Meta:
        model = DanceClassLink
        fields = ["link", "author"]


class DanceHallLinkForm(forms.ModelForm):
    class Meta:
        model = DanceHallLink
        fields = ["link", "author"]


class DanceShopLinkForm(forms.ModelForm):
    class Meta:
        model = DanceShopLink
        fields = ["link", "author"]


class VideoWikiLinkForm(forms.ModelForm):
    class Meta:
        model = VideoWikiLink
        fields = ["link", "author"]


class AudioWikiLinkForm(forms.ModelForm):
    class Meta:
        model = AudioWikiLink
        fields = ["link", "author"]


class AudioWikiPlaylistLinkForm(forms.ModelForm):
    class Meta:
        model = AudioWikiPlaylistLink
        fields = ["link", "author"]


class VideoWikiPlaylistLinkForm(forms.ModelForm):
    class Meta:
        model = VideoWikiPlaylistLink
        fields = ["link", "author"]


class LinkShouldKnowForm(forms.ModelForm):
    class Meta:
        model = LinkShouldKnow
        fields = ['title', 'description', 'image', 'direction', 'links', 'author']


class PersonShouldKnowForm(forms.ModelForm):
    class Meta:
        model = PersonShouldKnow
        fields = ['title', 'description', 'image', 'direction', 'links', 'author']


class OrganizationShouldKnowForm(forms.ModelForm):
    class Meta:
        model = OrganizationShouldKnow
        fields = ['title', 'description', 'image', 'direction', 'links', 'author']


class DanceStyleForm(forms.ModelForm):
    class Meta:
        model = DanceStyle
        fields = ["title", 'description', 'image', 'direction', 'count_types', 'between_partners_distances',
                  'average_prices', 'for_children', "author"]


class EventTypeForm(forms.ModelForm):
    class Meta:
        model = EventType
        fields = ["title", 'description', "author"]


class PlaceInMapMapCoordinatesForm(forms.ModelForm):
    class Meta:
        model = PlaceInMapMapCoordinates
        fields = ["lat", 'lng', "author"]


class DanceStudioMapCoordinatesForm(forms.ModelForm):
    class Meta:
        model = DanceStudioMapCoordinates
        fields = ["lat", 'lng', "author"]


class DanceHallMapCoordinatesForm(forms.ModelForm):
    class Meta:
        model = DanceHallMapCoordinates
        fields = ["lat", 'lng', "author"]


class DanceShopMapCoordinatesForm(forms.ModelForm):
    class Meta:
        model = DanceShopMapCoordinates
        fields = ["lat", 'lng', "author"]


class PlaceInMapLocationForm(forms.ModelForm):
    class Meta:
        model = PlaceInMapLocation
        fields = ["address", "city", "note", 'coordinates', "author"]


class EventLocationForm(forms.ModelForm):
    class Meta:
        model = EventLocation
        fields = ["address", "city", "note", "author"]


class DanceStudioLocationForm(forms.ModelForm):
    class Meta:
        model = DanceStudioLocation
        fields = ["address", "city", "note", 'coordinates', "author"]


class DanceHallLocationForm(forms.ModelForm):
    class Meta:
        model = DanceHallLocation
        fields = ["address", "city", "note", 'coordinates', "author"]


class DanceShopLocationForm(forms.ModelForm):
    class Meta:
        model = DanceShopLocation
        fields = ["address", "city", "note", 'coordinates', "author"]


class PlaceInMapForm(forms.ModelForm):
    class Meta:
        model = PlaceInMap
        fields = ["title", 'description', 'image', 'locations', "dance_styles", "author"]


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ["title", 'description', "note", "status", 'start_date', 'end_date', "event_types", "dance_styles",
                  "locations", 'links', "author"]

    class Media:
        js = ('//code.jquery.com/jquery-1.11.0.min.js', 'js/end_date_onchange.js')

    def clean(self):
        cleaned_data = super(EventForm, self).clean()
        status = cleaned_data.get("status")
        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")

        if start_date and end_date:
            if end_date < start_date:
                raise forms.ValidationError("End date cannot be earlier than start date!")

        if status == 'PL' and end_date and end_date <= datetime.date.today():
            raise forms.ValidationError("Status cannot be Planned!")
        if status == 'PL' and start_date and end_date and start_date <= datetime.date.today() <= end_date:
            raise forms.ValidationError("Status cannot be Planned!")
        if status == 'HD' and end_date and end_date < datetime.date.today():
            raise forms.ValidationError("Status cannot be Holding!")
        if status == 'HD' and start_date and start_date > datetime.date.today():
            raise forms.ValidationError("Status cannot be Holding!")
        if status == 'CL' and start_date and start_date > datetime.date.today():
            raise forms.ValidationError("Status cannot be Completed!")
        if status == 'CL' and start_date and end_date and start_date <= datetime.date.today() <= end_date:
            raise forms.ValidationError("Status cannot be Completed!")

        return cleaned_data


class InstructorForm(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = ["name", 'description', 'dance_styles', 'links', 'contacts', 'events', "author"]


class DanceStudioForm(forms.ModelForm):
    class Meta:
        model = DanceStudio
        fields = ["title", 'description', 'logo', 'locations', 'links', 'contacts', 'instructors', 'dance_styles',
                  "author"]


class DanceClassForm(forms.ModelForm):
    class Meta:
        model = DanceClass
        fields = ["title", 'description', 'is_opened_lesson', 'is_probably_free', 'first_lesson_free',
                  'free_lesson_date', 'every_first_lesson_free', 'experience_level', 'start_date', 'end_date',
                  'schedule_week_days', 'dance_studio', 'dance_styles', 'instructors', 'links', "author"]

    class Media:
        js = ('//code.jquery.com/jquery-1.11.0.min.js', 'js/end_date_onchange.js')


class DanceHallPhotoForm(forms.ModelForm):
    class Meta:
        model = DanceHallPhoto
        fields = ["title", 'description', 'photo', "author"]


class DanceHallForm(forms.ModelForm):
    class Meta:
        model = DanceHall
        fields = ["title", 'description', 'photos', 'locations', 'links', 'contacts', "author"]


class DanceShopPhotoForm(forms.ModelForm):
    class Meta:
        model = DanceShopPhoto
        fields = ["title", 'description', 'photo', "author"]


class DanceShopForm(forms.ModelForm):
    class Meta:
        model = DanceShop
        fields = ["title", 'description', 'photos', 'locations', 'links', 'contacts', "author"]


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'description', 'image', 'is_linked_article', 'article_link', "author"]


class VideoWikiTagForm(forms.ModelForm):
    class Meta:
        model = VideoWikiTag
        fields = ['title', 'start_time', 'end_time']


class AudioWikiTagForm(forms.ModelForm):
    class Meta:
        model = AudioWikiTag
        fields = ['title']


class PhotoWikiTagForm(forms.ModelForm):
    class Meta:
        model = PhotoWikiTag
        fields = ['title']


class VideoWikiForm(forms.ModelForm):
    class Meta:
        model = VideoWiki
        fields = ['title', 'dance_styles', 'link', 'tags', 'author']


class AudioWikiForm(forms.ModelForm):
    class Meta:
        model = AudioWiki
        fields = ['title', 'singer', 'dance_styles', 'link', 'tags', 'author']


class PhotoWikiForm(forms.ModelForm):
    class Meta:
        model = PhotoWiki
        fields = ['title', 'photographer', 'dance_styles', 'image', 'tags', 'author']


class VideoWikiPlaylistForm(forms.ModelForm):
    class Meta:
        model = VideoWikiPlaylist
        fields = ['title', 'link', 'dance_style', 'author']


class AudioWikiPlaylistForm(forms.ModelForm):
    class Meta:
        model = AudioWikiPlaylist
        fields = ['title', 'link', 'dance_style', 'author']


class PhotoWikiAlbumForm(forms.ModelForm):
    class Meta:
        model = PhotoWikiAlbum
        fields = ['title', 'photos', 'author']


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
