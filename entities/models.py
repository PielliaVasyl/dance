from datetime import date

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.defaultfilters import truncatechars


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


class Link(models.Model):
    link = models.URLField()

    author = models.ForeignKey('UserProfile', on_delete=models.CASCADE, )
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return '%s' % self.link

    class Meta:
        ordering = ('link',)


class DanceType(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    image = models.ImageField(blank=True)

    @property
    def short_description(self):
        return truncatechars(self.description, 100)

    # parent_dance_type =
    # child_dance_type =

    author = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return '%s' % self.title

    class Meta:
        ordering = ('title',)


class EventType(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    @property
    def short_description(self):
        return truncatechars(self.description, 100)

    def title_show(self):
        title_show_dict = {
            'Fest': 'Фестивать',
            'Competition': 'Конкурс',
            'Master class': 'Мастер-класс',
            'Open air': 'Open air',
            'Party': 'Вечеринка'
        }
        return "%s" % title_show_dict.get(self.title, self.title)

    author = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return '%s' % self.title

    class Meta:
        ordering = ('created',)


class Location(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    address = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=50, blank=True)

    @property
    def short_description(self):
        return truncatechars(self.description, 100)

    def title_show(self):
        if self.address and self.city:
            return "%s, %s" % (self.address, self.city,)
        if self.address:
            return "%s" % (self.address,)
        if self.city:
            return "%s" % (self.city,)
        return ""

    dance_types = models.ManyToManyField(DanceType, blank=True)

    def get_dance_types(self):
        if self.dance_types.all():
            return "\n".join([p.title for p in self.dance_types.all()])
        return ''

    author = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return '%s at %s, %s' % (self.title, self.address, self.city)

    class Meta:
        ordering = ('created',)


class Event(models.Model):
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

    def status_show(self, status_choices=STATUS_CHOICES):
        status_choices_dict = {k: v for k, v in status_choices}
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

    def date(self):
        if self.start_date and self.end_date:
            return '{0} - {1}'.format(self.start_date.strftime('%d.%m'), self.end_date.strftime('%d.%m'))
        if self.start_date:
            return 'c {0}'.format(self.start_date.strftime('%d.%m'), )
        if self.end_date:
            return 'по {0}'.format(self.end_date.strftime('%d.%m'), )
        return 'Неизвестно'

    def duration_show(self):
        if self.start_date and self.end_date:
            return '%s день (дня)' % str(int((self.end_date - self.start_date).days) + 1)
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
    dance_types = models.ManyToManyField(DanceType, blank=True)
    locations = models.ManyToManyField(Location, blank=True)
    links = models.ManyToManyField(Link, blank=True)

    def get_event_types(self):
        if self.event_types.all():
            return "\n".join([p.title for p in self.event_types.all()])
        return ''

    def get_dance_types(self):
        if self.dance_types.all():
            return "\n".join([p.title for p in self.dance_types.all()])
        return ''

    def get_locations(self):
        if self.locations.all():
            return "\n".join([p.title for p in self.locations.all()])
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
        ordering = ('updated',)


class Instructor(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    @property
    def short_description(self):
        return truncatechars(self.description, 100)

    image = models.ImageField(blank=True)

    dance_types = models.ManyToManyField(DanceType, blank=True)
    events = models.ManyToManyField(Event, blank=True)
    links = models.ManyToManyField(Link, blank=True)

    def get_dance_types(self):
        if self.dance_types.all():
            return "\n".join([p.title for p in self.dance_types.all()])
        return ''

    def get_events(self):
        if self.events.all():
            return "\n".join([p.title for p in self.events.all()])
        return ''

    def get_links(self):
        if self.links.all():
            return "\n".join([p.link for p in self.links.all()])
        return ''

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

    dance_types = models.ManyToManyField(DanceType, blank=True)
    instructors = models.ManyToManyField(Instructor, blank=True)
    locations = models.ManyToManyField(Location, blank=True)
    links = models.ManyToManyField(Link, blank=True)

    def get_dance_types(self):
        if self.dance_types.all():
            return "\n".join([p.title for p in self.dance_types.all()])
        return ''

    def get_instructors(self):
        if self.instructors.all():
            return "\n".join([p.title for p in self.instructors.all()])
        return ''

    def get_locations(self):
        if self.locations.all():
            return "\n".join([p.title for p in self.locations.all()])
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
        ordering = ('title',)


class WeekDay(models.Model):
    MONDAY = 'MON'
    TUESDAY = 'TUE'
    WEDNESDAY = 'WED'
    THURSDAY = 'THU'
    FRIDAY = 'FRI'
    SATURDAY = 'SAT'
    SUNDAY = 'SUN'

    DAY_CHOICES = (
        (MONDAY, 'Понедельник'),
        (TUESDAY, 'Вторник'),
        (WEDNESDAY, 'Среда'),
        (THURSDAY, 'Четверг'),
        (FRIDAY, 'Пятница'),
        (SATURDAY, 'Суббота'),
        (SUNDAY, 'Воскресенье'),
    )

    day = models.CharField(max_length=3, choices=DAY_CHOICES, blank=True)

    def week_day_show(self):
        week_day_show_dict = {
            'MON': 'Пн',
            'TUE': 'Вт',
            'WED': 'Ср',
            'THU': 'Чт',
            'FRI': 'Пт',
            'SAT': 'Сб',
            'SUN': 'Вс'
        }
        return "%s" % week_day_show_dict.get(self.day, self.day)

    def __str__(self):
        return '%s' % self.day


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

    start_date = models.DateField(default=date.today, null=True, blank=True)
    end_date = models.DateField(default=date.today, null=True, blank=True)

    def date(self):
        if self.start_date and self.end_date:
            return '{0} - {1}'.format(self.start_date.strftime('%d.%m'), self.end_date.strftime('%d.%m'))
        if self.start_date:
            return 'c {0}'.format(self.start_date.strftime('%d.%m'), )
        if self.end_date:
            return 'по {0}'.format(self.end_date.strftime('%d.%m'), )
        return 'Неизвестно'

    schedule_week_days = models.ManyToManyField(WeekDay, blank=True)

    def get_schedule_week_days(self):
        if self.schedule_week_days.all():
            return "\n".join([p.day for p in self.schedule_week_days.all()])
        return ''

    dance_studio = models.ForeignKey(DanceStudio, on_delete=models.CASCADE, null=True, blank=True)
    dance_types = models.ManyToManyField(DanceType, blank=True)
    instructors = models.ManyToManyField(Instructor, blank=True)
    links = models.ManyToManyField(Link, blank=True)

    def get_dance_types(self):
        if self.dance_types.all():
            return "\n".join([p.title for p in self.dance_types.all()])
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

    photos = models.ManyToManyField('DanceHallPhoto', blank=True)

    def count_photos(self):
        return self.photos.count()

    location = models.ForeignKey('Location', null=True, blank=True)

    author = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        if self.location:
            return '%s at %s' % (self.title, self.location.address)
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
