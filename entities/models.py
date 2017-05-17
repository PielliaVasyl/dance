from datetime import date

from django.utils.translation import activate

from algoritms.change_status_value import change_status_value_in_values, get_current_status

from django.template.defaultfilters import date as date_filter
from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.defaultfilters import truncatechars

from classes.models import WeekDay
from dance_styles.models import CountType, BetweenPartnersDistance, AveragePrice


class UserProfile(models.Model):
    user = models.OneToOneField(User)

    role = models.CharField(max_length=50, blank=True, default=None, null=True)

    def name(self):
        return self.user.name

    def __str__(self):
        return "%s's profile" % self.user


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()


class AbstractSocialLink(models.Model):
    link = models.URLField()

    author = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return '%s' % self.link

    class Meta:
        ordering = ('created',)


class SocialLinkFB(AbstractSocialLink):
    pass


class SocialLinkVK(AbstractSocialLink):
    pass


class SocialLinkInstagram(AbstractSocialLink):
    pass


class SocialLinkTwitter(AbstractSocialLink):
    pass


class Socials(models.Model):
    title = models.CharField(max_length=50)
    fb = models.ManyToManyField(SocialLinkFB, blank=True)
    vk = models.ManyToManyField(SocialLinkVK, blank=True)
    instagram = models.ManyToManyField(SocialLinkInstagram, blank=True)
    twitter = models.ManyToManyField(SocialLinkTwitter, blank=True)

    def get_fbs(self):
        if self.fb.all():
            return "\n".join([p.link for p in self.fb.all()])
        return ''

    def get_vks(self):
        if self.fb.all():
            return "\n".join([p.link for p in self.vk.all()])
        return ''

    def get_instagrams(self):
        if self.fb.all():
            return "\n".join([p.link for p in self.instagram.all()])
        return ''

    def get_twitters(self):
        if self.fb.all():
            return "\n".join([p.link for p in self.twitter.all()])
        return ''

    author = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return '%s' % self.title

    class Meta:
        ordering = ('title',)


class PhoneNumber(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Введите номер телефона в формате: '+380XXXXXXX'. Разрешено до 15 цифр.")
    phone_number = models.CharField(max_length=16, validators=[phone_regex], blank=True)  # validators should be a list

    author = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return '%s' % self.phone_number

    class Meta:
        ordering = ('created',)


class Contacts(models.Model):
    title = models.CharField(max_length=50)

    phone_numbers = models.ManyToManyField(PhoneNumber, blank=True)

    def get_phone_numbers(self):
        if self.phone_numbers.all():
            return "\n".join([p.phone_number for p in self.phone_numbers.all()])
        return ''

    socials = models.ForeignKey('Socials', on_delete=models.CASCADE, blank=True, null=True)

    author = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return '%s' % self.title

    class Meta:
        ordering = ('title',)


class AbstractLink(models.Model):
    link = models.URLField()

    author = models.ForeignKey('UserProfile', on_delete=models.CASCADE, )
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return '%s' % self.link

    class Meta:
        ordering = ('link',)


class LinkShouldKnowLink(AbstractLink):
    pass


class PersonShouldKnowLink(AbstractLink):
    pass


class OrganizationShouldKnowLink(AbstractLink):
    pass


class EventLink(AbstractLink):
    pass


class InstructorLink(AbstractLink):
    pass


class DanceStudioLink(AbstractLink):
    pass


class DanceClassLink(AbstractLink):
    pass


class DanceHallLink(AbstractLink):
    pass


class DanceShopLink(AbstractLink):
    pass


class VideoWikiLink(AbstractLink):
    pass


class AudioWikiLink(AbstractLink):
    pass


class AudioWikiPlaylistLink(AbstractLink):
    pass


class VideoWikiPlaylistLink(AbstractLink):
    pass


class AbstractShouldKnow(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(blank=True)

    @property
    def short_description(self):
        return truncatechars(self.description, 100)

    author = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return '%s' % self.title

    class Meta:
        ordering = ('updated',)


class LinkShouldKnow(AbstractShouldKnow):
    OTHER = 'OTH'

    DIRECTIONS = {OTHER}
    DIRECTION_SHOW = {
        OTHER: 'Другое'
    }
    DIRECTION_CHOICES = (
        (OTHER, 'Другое'),
    )
    direction = models.CharField(max_length=3, choices=DIRECTION_CHOICES, default=OTHER)

    links = models.ManyToManyField(LinkShouldKnowLink, blank=True)

    def get_links(self):
        if self.links.all():
            return "\n".join([p.link for p in self.links.all()])
        return ''


class PersonShouldKnow(AbstractShouldKnow):
    OTHER = 'OTH'

    DIRECTIONS = {OTHER}
    DIRECTION_SHOW = {
        OTHER: 'Другое'
    }
    DIRECTION_CHOICES = (
        (OTHER, 'Другое'),
    )
    direction = models.CharField(max_length=3, choices=DIRECTION_CHOICES, default=OTHER)

    links = models.ManyToManyField(PersonShouldKnowLink, blank=True)

    def get_links(self):
        if self.links.all():
            return "\n".join([p.link for p in self.links.all()])
        return ''


class OrganizationShouldKnow(AbstractShouldKnow):
    OTHER = 'OTH'

    DIRECTIONS = {OTHER}
    DIRECTION_SHOW = {
        OTHER: 'Другое'
    }
    DIRECTION_CHOICES = (
        (OTHER, 'Другое'),
    )
    direction = models.CharField(max_length=3, choices=DIRECTION_CHOICES, default=OTHER)

    links = models.ManyToManyField(OrganizationShouldKnowLink, blank=True)

    def get_links(self):
        if self.links.all():
            return "\n".join([p.link for p in self.links.all()])
        return ''


class DanceStyle(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    image = models.ImageField(blank=True)

    @property
    def short_description(self):
        return truncatechars(self.description, 100)

    BALLET = 'BAL'
    LATINA = 'LAT'

    DIRECTIONS = {BALLET, LATINA}
    DIRECTION_SHOW = {
        BALLET: 'Балет',
        LATINA: 'Латина'
    }
    DIRECTION_CHOICES = (
        (BALLET, 'Балет'),
        (LATINA, 'Латина'),
    )
    direction = models.CharField(max_length=3, choices=DIRECTION_CHOICES, default=LATINA)

    def direction_show(self):
        direction_choices_dict = {k: v for k, v in self.DIRECTION_CHOICES}
        return "%s" % direction_choices_dict.get(self.direction, self.direction)

    count_types = models.ManyToManyField(CountType, blank=True)
    between_partners_distances = models.ManyToManyField(BetweenPartnersDistance, blank=True)
    average_prices = models.ManyToManyField(AveragePrice, blank=True)

    def get_count_types(self):
        if self.count_types.all():
            return "\n".join([p.count_type for p in self.count_types.all()])
        return ''

    COUNT_TYPE_CHOICES = CountType.COUNT_TYPE_CHOICES

    def get_count_types_list(self):
        if self.count_types.all():
            return [{k: v for k, v in self.COUNT_TYPE_CHOICES}.get(p.count_type, p.count_type)
                    for p in self.count_types.all()]
        return []

    def get_between_partners_distances(self):
        if self.between_partners_distances.all():
            return "\n".join([p.distance for p in self.between_partners_distances.all()])
        return ''

    DISTANCE_CHOICES = BetweenPartnersDistance.DISTANCE_CHOICES

    def get_between_partners_distances_list(self):
        if self.between_partners_distances.all():
            return [{k: v for k, v in self.DISTANCE_CHOICES}.get(p.distance, p.distance) for p in
                    self.between_partners_distances.all()]
        return []

    def get_average_prices(self):
        if self.average_prices.all():
            return "\n".join([p.price for p in self.average_prices.all()])
        return ''

    PRICE_CHOICES = AveragePrice.PRICE_CHOICES

    def get_average_prices_list(self):
        if self.average_prices.all():
            return [{k: v for k, v in self.PRICE_CHOICES}.get(p.price, p.price) for p in self.average_prices.all()]
        return []

    for_children = models.BooleanField(blank=True, default=False)

    author = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return '%s - %s' % (self. direction, self.title)

    class Meta:
        ordering = ('title',)


class EventType(models.Model):
    description = models.TextField(blank=True)

    @property
    def short_description(self):
        return truncatechars(self.description, 100)

    FEST = 'FEST'
    COMPETITION = 'COMP'
    MASTERCLASS = 'MCLS'
    OPENAIR = 'OAIR'
    PARTY = 'PART'

    EVENT_TYPE_CHOICES = (
        (FEST, 'Фестивать'),
        (COMPETITION, 'Конкурс'),
        (MASTERCLASS, 'Мастер-класс'),
        (OPENAIR, 'Open air'),
        (PARTY, 'Вечеринка')
    )
    title = models.CharField(max_length=4, choices=EVENT_TYPE_CHOICES, default=MASTERCLASS)

    def title_show(self):
        title_show_dict = {
            self.FEST: 'Фестивать',
            self.COMPETITION: 'Конкурс',
            self.MASTERCLASS: 'Мастер-класс',
            self.OPENAIR: 'Open air',
            self.PARTY: 'Вечеринка'
        }
        return "%s" % title_show_dict.get(self.title, self.title)

    author = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return '%s' % self.title

    class Meta:
        ordering = ('created',)


class AbstractMapCoordinates(models.Model):
    lat = models.CharField(max_length=20)
    lng = models.CharField(max_length=20)

    author = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return 'Lat:%s, lng: %s' % (self.lat, self.lng)

    class Meta:
        ordering = ('created',)


class PlaceInMapMapCoordinates(AbstractMapCoordinates):
    pass


class DanceStudioMapCoordinates(AbstractMapCoordinates):
    pass


class DanceHallMapCoordinates(AbstractMapCoordinates):
    pass


class DanceShopMapCoordinates(AbstractMapCoordinates):
    pass


class City(models.Model):
    city = models.CharField(max_length=50, blank=True)

    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return '%s' % self.city

    class Meta:
        ordering = ('city',)


class AbstractLocation(models.Model):
    address = models.CharField(max_length=100, blank=True)
    city = models.ForeignKey('City', on_delete=models.CASCADE, blank=True, null=True)
    note = models.CharField(max_length=100, blank=True)

    author = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        if self.city:
            return '%s, %s' % (self.address, self.city.city)
        return '%s' % (self.address,)

    class Meta:
        ordering = ('created',)


class PlaceInMapLocation(AbstractLocation):
    coordinates = models.ForeignKey(PlaceInMapMapCoordinates, on_delete=models.CASCADE, blank=True, null=True)


class EventLocation(AbstractLocation):
    pass


class DanceStudioLocation(AbstractLocation):
    coordinates = models.ForeignKey(DanceStudioMapCoordinates, on_delete=models.CASCADE, blank=True, null=True)


class DanceHallLocation(AbstractLocation):
    coordinates = models.ForeignKey(DanceHallMapCoordinates, on_delete=models.CASCADE, blank=True, null=True)


class DanceShopLocation(AbstractLocation):
    coordinates = models.ForeignKey(DanceShopMapCoordinates, on_delete=models.CASCADE, blank=True, null=True)


class PlaceInMap(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    image = models.ImageField(blank=True)
    locations = models.ManyToManyField(PlaceInMapLocation, blank=True)

    def get_locations(self):
        if self.locations.all():
            return "\n".join([p.address for p in self.locations.all()])
        return ''

    def get_locations_address_list(self):
        if self.locations.all():
            return [p.address for p in self.locations.all()]
        return []

    @property
    def short_description(self):
        return truncatechars(self.description, 100)

    dance_styles = models.ManyToManyField(DanceStyle, blank=True)

    def get_dance_styles(self):
        if self.dance_styles.all():
            return "\n".join([p.title for p in self.dance_styles.all()])
        return ''

    def get_dance_styles_list(self):
        if self.dance_styles.all():
            return [p.title for p in self.dance_styles.all()]
        return []

    author = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return '%s' % (self.title,)

    class Meta:
        ordering = ('created',)


def _get_date_show(self):
    activate('ru')
    if self.start_date and self.end_date:
        if self.start_date == self.end_date:
            return '{0} {1}'.format(self.start_date.strftime('%d'), date_filter(self.start_date, 'F').lower()[:3])
        elif self.start_date.month == self.end_date.month:
            return '{0} - {1} {2}'.format(self.start_date.strftime('%d'), self.end_date.strftime('%d'),
                                          date_filter(self.start_date, 'F').lower()[:3])
        return '{0} {1} - {2} {3}'.format(self.start_date.strftime('%d'),
                                          date_filter(self.start_date, 'F').lower()[:3],
                                          self.end_date.strftime('%d'),
                                          date_filter(self.end_date, 'F').lower()[:3])
    if self.start_date:
        return 'c {0} {1}'.format(self.start_date.strftime('%d'),
                                  date_filter(self.start_date, 'F').lower()[:3])
    if self.end_date:
        return 'по {0} {1}'.format(self.end_date.strftime('%d'),
                                   date_filter(self.end_date, 'F').lower()[:3])


class Event(models.Model):
    # bad solution - check how status are signed
    @classmethod
    def from_db(cls, db, field_names, values):
        if len(values) != len(cls._meta.concrete_fields):
            values = list(values)
            values.reverse()
            from django.db.models.base import DEFERRED
            values = [values.pop() if f.attname in field_names else DEFERRED for f in cls._meta.concrete_fields]
        try:
            values = change_status_value_in_values(values, field_names)
        except:
            pass
        new = cls(*values)
        new._state.adding = False
        new._state.db = db
        return new

    def save(self, *args, **kwargs):
        self.status = get_current_status(self.status, self.start_date, self.end_date)
        super().save()

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    note = models.TextField(blank=True)

    @property
    def short_description(self):
        return truncatechars(self.description, 100)

    PLANNED = 'PL'
    DENIED = 'DN'
    POSTPONED = 'PP'
    HELD = 'HL'
    COMPLETED = 'CL'

    STATUS_CHOICES = (
        (PLANNED, 'Запланировано'),
        (DENIED, 'Отменено'),
        (POSTPONED, 'Перенесено'),
        (HELD, 'Проводится'),
        (COMPLETED, 'Завершено')
    )
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=PLANNED, blank=True)

    def status_show(self):
        status_choices_dict = {k: v for k, v in self.STATUS_CHOICES}
        return "%s" % status_choices_dict.get(self.status, 'Статус неизвестен')

    def status_icon(self, planned=PLANNED, denied=DENIED, postponed=POSTPONED, held=HELD, completed=COMPLETED):
        status_icon_dict = {
            planned: 'fa-calendar-check-o',
            denied: 'fa-times',
            postponed: 'fa-clock-o',
            held: 'fa-play',
            completed: 'fa-check'
        }
        return "%s" % status_icon_dict.get(self.status, 'fa-dot-circle-o')

    def status_label_color(self, planned=PLANNED, denied=DENIED, postponed=POSTPONED, held=HELD, completed=COMPLETED):
        status_label_color_dict = {
            planned: 'info',
            denied: 'danger',
            postponed: 'warning',
            held: 'success',
            completed: 'primary'
        }
        return "%s" % status_label_color_dict.get(self.status, 'default')

    start_date = models.DateField(default=date.today, blank=True, null=True)
    end_date = models.DateField(default=date.today, blank=True, null=True)

    def date_show(self):
        return _get_date_show(self) or 'Неизвестно'

    @staticmethod
    def day_show(number_days):
        return {
            '1': 'день',
            '2': 'дня',
            '3': 'дня',
            '4': 'дня',
            '5': 'дней',
            '6': 'дней',
            '7': 'дней',
            '8': 'дней',
            '9': 'дней',
            '10': 'дней',
            '11': 'дней',
            '12': 'дней',
            '13': 'дней',
            '14': 'дней',
        }.get(str(number_days), 'день')

    def duration_show(self):
        if self.start_date and self.end_date:
            number_days = int((self.end_date - self.start_date).days) + 1
            return '%s %s' % (str(number_days),
                              self.day_show(number_days),)
        return 'продолжительность неизвестна'

    def get_start_date_day_of_week(self):
        if self.start_date:
            return ''.join(self.start_date.strftime("%A"))
        return ''

    def get_end_date_day_of_week(self):
        if self.end_date:
            return ''.join(self.end_date.strftime("%A"))
        return ''

    event_types = models.ManyToManyField(EventType, blank=True)
    dance_styles = models.ManyToManyField(DanceStyle, blank=True)
    locations = models.ManyToManyField(EventLocation, blank=True)
    links = models.ManyToManyField(EventLink, blank=True)

    def get_event_types(self):
        if self.event_types.all():
            return "\n".join([p.title for p in self.event_types.all()])
        return ''

    def get_dance_styles(self):
        if self.dance_styles.all():
            return "\n".join([p.title for p in self.dance_styles.all()])
        return ''

    def get_locations(self):
        if self.locations.all():
            return "\n".join([p.address for p in self.locations.all()])
        return ''

    def get_links(self):
        if self.links.all():
            return "\n".join([p.link for p in self.links.all()])
        return ''

    author = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return '%s' % self.title

    class Meta:
        ordering = ('start_date',)


class Instructor(models.Model):
    name = models.CharField(max_length=100)

    def title(self):
        return self.name

    description = models.TextField(blank=True)

    @property
    def short_description(self):
        return truncatechars(self.description, 100)

    image = models.ImageField(blank=True)

    dance_styles = models.ManyToManyField(DanceStyle, blank=True)
    events = models.ManyToManyField(Event, blank=True)
    links = models.ManyToManyField(InstructorLink, blank=True)
    contacts = models.ForeignKey('Contacts', on_delete=models.CASCADE, null=True, blank=True)

    def get_dance_styles(self):
        if self.dance_styles.all():
            return "\n".join([p.title for p in self.dance_styles.all()])
        return ''

    def get_dance_styles_list(self):
        if self.dance_styles.all():
            return [p.title for p in self.dance_styles.all()]
        return []

    def get_events(self):
        if self.events.all():
            return "\n".join([p.title for p in self.events.all()])
        return ''

    def get_links(self):
        if self.links.all():
            return "\n".join([p.link for p in self.links.all()])
        return ''

    def get_links_list(self):
        if self.links.all():
            return [p.link for p in self.links.all()]
        return []

    author = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return '%s' % self.name

    class Meta:
        ordering = ('name',)


class DanceStudio(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    @property
    def short_description(self):
        return truncatechars(self.description, 100)

    logo = models.ImageField(blank=True)

    dance_styles = models.ManyToManyField(DanceStyle, blank=True)
    instructors = models.ManyToManyField(Instructor, blank=True)
    locations = models.ManyToManyField(DanceStudioLocation, blank=True)
    links = models.ManyToManyField(DanceStudioLink, blank=True)
    contacts = models.ForeignKey('Contacts', on_delete=models.CASCADE, null=True, blank=True)

    def get_dance_styles(self):
        if self.dance_styles.all():
            return "\n".join([p.title for p in self.dance_styles.all()])
        return ''

    def get_dance_styles_list(self):
        if self.dance_styles.all():
            return [p.title for p in self.dance_styles.all()]
        return []

    def get_instructors(self):
        if self.instructors.all():
            return "\n".join([p.title for p in self.instructors.all()])
        return ''

    def get_locations(self):
        if self.locations.all():
            return "\n".join([p.address for p in self.locations.all()])
        return ''

    def get_locations_address_list(self):
        if self.locations.all():
            return [p.address for p in self.locations.all()]
        return []

    def get_links(self):
        if self.links.all():
            return "\n".join([p.link for p in self.links.all()])
        return ''

    def get_links_list(self):
        if self.links.all():
            return [p.link for p in self.links.all()]
        return []

    author = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return '%s' % self.title

    class Meta:
        ordering = ('title',)


class DanceClass(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    @property
    def short_description(self):
        return truncatechars(self.description, 100)

    is_opened_lesson = models.BooleanField(default=False)
    # условно-бесплатное - получение билетов при репосте и выигрыше в лоттерее
    is_probably_free = models.BooleanField(default=False)

    first_lesson_free = models.BooleanField(default=False, blank=True)
    free_lesson_date = models.DateField(default=date.today, null=True, blank=True)
    every_first_lesson_free = models.BooleanField(default=False, blank=True)

    NEW = 'NEW'
    INTERMEDIATE = 'INM'
    ADVANCED = 'ADV'
    SHOW = 'SHW'
    PRACTICE = 'PRC'
    OTHER = 'OTH'

    EXPERIENCE_LEVEL_CHOICES = (
        (NEW, 'Начинающий'),
        (INTERMEDIATE, 'Средний'),
        (ADVANCED, 'Опытный'),
        (SHOW, 'Шоу'),
        (PRACTICE, 'Практика'),
        (OTHER, 'Другое')
    )
    experience_level = models.CharField(max_length=3, choices=EXPERIENCE_LEVEL_CHOICES, blank=True)

    def experience_level_show(self):
        experience_level_choices_dict = {k: v for k, v in self.EXPERIENCE_LEVEL_CHOICES}
        return "%s" % experience_level_choices_dict.get(self.experience_level, self.experience_level)

    start_date = models.DateField(default=date.today, null=True, blank=True)
    end_date = models.DateField(default=date.today, null=True, blank=True)

    def date_show(self):
        return _get_date_show(self) or 'Неизвестно'

    schedule_week_days = models.ManyToManyField(WeekDay, blank=True)

    def get_schedule_week_days(self):
        if self.schedule_week_days.all():
            return "\n".join([p.day for p in self.schedule_week_days.all()])
        return ''

    dance_studio = models.ForeignKey(DanceStudio, on_delete=models.CASCADE, null=True, blank=True)
    dance_styles = models.ManyToManyField(DanceStyle, blank=True)
    instructors = models.ManyToManyField(Instructor, blank=True)
    links = models.ManyToManyField(DanceClassLink, blank=True)

    def get_dance_styles(self):
        if self.dance_styles.all():
            return "\n".join([p.title for p in self.dance_styles.all()])
        return ""

    def get_instructors(self):
        if self.instructors.all():
            return "\n".join([p.title for p in self.instructors.all()])
        return ''

    def get_links(self):
        if self.links.all():
            return "\n".join([p.link for p in self.links.all()])
        return ''

    author = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        if self.dance_studio:
            return '%s in %s' % (self.title, self.dance_studio.title)
        return '%s' % (self.title,)

    class Meta:
        ordering = ('title',)


class DanceHallPhoto(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    photo = models.ImageField()

    author = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        ordering = ('created',)


class DanceHall(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    @property
    def short_description(self):
        return truncatechars(self.description, 100)

    photos = models.ManyToManyField('DanceHallPhoto', blank=True)

    def count_photos(self):
        return self.photos.count()

    locations = models.ManyToManyField(DanceHallLocation, blank=True)
    links = models.ManyToManyField(DanceHallLink, blank=True)
    contacts = models.ForeignKey('Contacts', on_delete=models.CASCADE, null=True, blank=True)

    def get_locations(self):
        if self.locations.all():
            return "\n".join([p.address for p in self.locations.all()])
        return ''

    def get_locations_address_list(self):
        if self.locations.all():
            return [p.address for p in self.locations.all()]
        return []

    def get_links(self):
        if self.links.all():
            return "\n".join([p.link for p in self.links.all()])
        return ''

    def get_links_list(self):
        if self.links.all():
            return [p.link for p in self.links.all()]
        return []

    author = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return '%s' % (self.title,)

    class Meta:
        ordering = ('title',)


class DanceShopPhoto(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    photo = models.ImageField()

    author = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        ordering = ('created',)


class DanceShop(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    @property
    def short_description(self):
        return truncatechars(self.description, 100)

    photos = models.ManyToManyField('DanceShopPhoto', blank=True)

    def count_photos(self):
        return self.photos.count()

    locations = models.ManyToManyField(DanceShopLocation, blank=True)
    links = models.ManyToManyField(DanceShopLink, blank=True)
    contacts = models.ForeignKey('Contacts', on_delete=models.CASCADE, null=True, blank=True)

    def get_locations(self):
        if self.locations.all():
            return "\n".join([p.address for p in self.locations.all()])
        return ''

    def get_locations_address_list(self):
        if self.locations.all():
            return [p.address for p in self.locations.all()]
        return []

    def get_links(self):
        if self.links.all():
            return "\n".join([p.link for p in self.links.all()])
        return ''

    def get_links_list(self):
        if self.links.all():
            return [p.link for p in self.links.all()]
        return []

    author = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return '%s' % (self.title,)

    class Meta:
        ordering = ('title',)


class Article(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    @property
    def short_description(self):
        return truncatechars(self.description, 100)

    image = models.ImageField(blank=True)

    is_linked_article = models.BooleanField(default=False)
    article_link = models.URLField(blank=True)

    author = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        if self.author:
            return '%s by %s' % (self.title, self.author.user.first_name)
        return '%s' % (self.title,)

    class Meta:
        ordering = ('created',)


class AbstractTag(models.Model):
    title = models.CharField(max_length=50)

    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return '%s' % (self.title,)

    class Meta:
        ordering = ('title',)


class VideoWikiTag(AbstractTag):
    start_time = models.TimeField(blank=True)
    end_time = models.TimeField(blank=True)


class AudioWikiTag(AbstractTag):
    pass


class PhotoWikiTag(AbstractTag):
    pass


class AbstractWiki(models.Model):
    title = models.CharField(max_length=200)
    dance_styles = models.ManyToManyField(DanceStyle, blank=True)

    def get_dance_styles(self):
        if self.dance_styles.all():
            return "\n".join([p.title for p in self.dance_styles.all()])
        return ''

    def get_dance_styles_list(self):
        if self.dance_styles.all():
            return [p.title for p in self.dance_styles.all()]
        return []

    def get_tags(self):
        if self.tags.all():
            return "\n".join([p.title for p in self.tags.all()])
        return ''

    def get_tags_list(self):
        if self.tags.all():
            return [p.title for p in self.tags.all()]
        return []

    author = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return '%s' % (self.title,)

    class Meta:
        ordering = ('title',)


class VideoWiki(AbstractWiki):
    link = models.ForeignKey('VideoWikiLink', on_delete=models.CASCADE, blank=True, null=True)
    tags = models.ManyToManyField(VideoWikiTag, blank=True)


class AudioWiki(AbstractWiki):
    singer = models.CharField(max_length=100, blank=True)
    link = models.ForeignKey('AudioWikiLink', on_delete=models.CASCADE, blank=True, null=True)
    tags = models.ManyToManyField(AudioWikiTag, blank=True)


class PhotoWiki(AbstractWiki):
    photographer = models.CharField(max_length=100, blank=True)
    image = models.ImageField(blank=True)
    tags = models.ManyToManyField(PhotoWikiTag, blank=True)


class AbstractWikiGroup(models.Model):
    title = models.CharField(max_length=100)

    author = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return '%s' % (self.title,)

    class Meta:
        ordering = ('created',)


class VideoWikiPlaylist(AbstractWikiGroup):
    link = models.ForeignKey('VideoWikiPlaylistLink', on_delete=models.CASCADE, blank=True, null=True)
    dance_style = models.ForeignKey('DanceStyle', on_delete=models.CASCADE)

    def get_videos(self):
        videos = VideoWiki.objects.filter(dance_styles__in=[self.dance_style])
        if videos:
            return '\n'.join([p.title for p in videos])
        return []


class AudioWikiPlaylist(AbstractWikiGroup):
    link = models.ForeignKey('AudioWikiPlaylistLink', on_delete=models.CASCADE, blank=True, null=True)
    dance_style = models.ForeignKey('DanceStyle', on_delete=models.CASCADE)

    def get_audios(self):
        audios = AudioWiki.objects.filter(dance_styles__in=[self.dance_style])
        if audios:
            return '\n'.join([p.title for p in audios])
        return ''

    def get_instances_list(self):
            audios = AudioWiki.objects.filter(dance_styles__in=[self.dance_style])
            if audios:
                return [p.title for p in audios]
            return []


class PhotoWikiAlbum(AbstractWikiGroup):
    photos = models.ManyToManyField(PhotoWiki, blank=True)

    def get_photos(self):
        if self.photos.all():
            return "\n".join([p.title for p in self.photos.all()])
        return ''

    def get_photos_list(self):
        if self.photos.all():
            return [p.title for p in self.photos.all()]
        return []


class VisitorMessage(models.Model):
    visitor_name = models.CharField(max_length=50)
    visitor_email = models.EmailField()
    visitor_phone_number = models.CharField(max_length=50, blank=True)
    message_subject = models.CharField(max_length=100)
    message_text = models.TextField()

    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return '%s (%s) - %s' % (self.visitor_name, self.visitor_email, self.message_subject)

    class Meta:
        ordering = ('created',)
