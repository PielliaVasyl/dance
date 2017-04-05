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

    # parent_dance_type =
    # child_dance_type =

    author = models.ForeignKey('UserProfile', on_delete=models.CASCADE, )
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return '%s' % self.title

    class Meta:
        ordering = ('title',)


class EventType(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    author = models.ForeignKey('UserProfile', on_delete=models.CASCADE, )
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
        return "\n".join([p.dance_types for p in self.dance_types.all()])

    author = models.ForeignKey('UserProfile', on_delete=models.CASCADE, )
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
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=PLANNED, blank=True, )

    event_types = models.ManyToManyField(EventType, blank=True)
    dance_types = models.ManyToManyField(DanceType, blank=True)
    locations = models.ManyToManyField(Location, blank=True)
    links = models.ManyToManyField(Link, blank=True)

    def get_event_types(self):
        return "\n".join([p.title for p in self.event_types.all()])

    def get_dance_types(self):
        return "\n".join([p.title for p in self.dance_types.all()])

    def get_locations(self):
        return "\n".join([p.title for p in self.locations.all()])

    def get_links(self):
        return "\n".join([p.link for p in self.links.all()])

    author = models.ForeignKey('UserProfile', on_delete=models.CASCADE, )
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return '%s' % self.title

    class Meta:
        ordering = ('updated',)
