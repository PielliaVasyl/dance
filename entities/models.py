from datetime import date

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    user = models.OneToOneField(User)

    role = models.CharField(max_length=50, blank=True, default=None, null=True)

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

    # some properties like initiative, Proximity, technical difficulty, physical complexity, etc

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

    PLANNED = 'PL'
    DENIED = 'DN'
    POSTPONED = 'PP'
    HELD = 'HL'

    STATUS_CHOICES = (
        (PLANNED, 'Заплонировано'),
        (DENIED, 'Отменено'),
        (POSTPONED, 'Перенесено'),
        (HELD, 'Проведено'),
    )
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=PLANNED, blank=True)

    start_date = models.DateField(default=date.today, blank=True)
    end_date = models.DateField(default=date.today, blank=True)

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

    image = models.ImageField(blank=True)

    dance_types = models.ManyToManyField(DanceType, blank=True)
    events = models.ManyToManyField(Event, blank=True)
    links = models.ManyToManyField(Link, blank=True)
    locations = models.ManyToManyField(Location, blank=True)

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

    def get_locations(self):
        if self.locations.all():
            return "\n".join([p.title for p in self.locations.all()])
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


class Shop(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    logo = models.ImageField(blank=True)

    links = models.ManyToManyField(Link, blank=True)
    locations = models.ManyToManyField(Location, blank=True)

    def get_links(self):
        if self.links.all():
            return "\n".join([p.link for p in self.links.all()])
        return ''

    def get_locations(self):
        if self.locations.all():
            return "\n".join([p.title for p in self.locations.all()])
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

    def __str__(self):
        return '%s' % self.day


class DanceClass(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    first_lesson_free = models.BooleanField(default=False, blank=True)
    free_lesson_date = models.DateField(default=date.today, null=True, blank=True)
    every_first_lesson_free = models.BooleanField(default=False, blank=True)

    start_date = models.DateField(default=date.today, null=True, blank=True)
    end_date = models.DateField(default=date.today, null=True, blank=True)
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


class Article(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    image = models.ImageField(blank=True)

    is_linked_article = models.BooleanField(default=False)
    article_link = models.URLField(blank=True)

    author = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        if self.author:
            return '%s by %s' % (self.title, self.author.user.name)
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
