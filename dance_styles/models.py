from django.db import models


class DanceStyleInSectionCountType(models.Model):
    SOLO = 'SOL'
    PARTNER = 'PRN'
    GROUP = 'GRP'

    COUNT_TYPE_SHOW = {
        SOLO: 'Одиночный',
        PARTNER: 'Парный',
        GROUP: 'Групповой'
    }

    COUNT_TYPE_CHOICES = (
        (SOLO, 'Одиночный'),
        (PARTNER, 'Парный'),
        (GROUP, 'Групповой')
    )

    count_type = models.CharField(max_length=3, choices=COUNT_TYPE_CHOICES, blank=True)

    def title_show(self):
        title_choices_dict = {k: v for k, v in self.COUNT_TYPE_CHOICES}
        return "%s" % title_choices_dict.get(self.count_type, self.count_type)

    def __str__(self):
        return '%s' % self.count_type


class DanceStyleInSectionBetweenPartnersDistance(models.Model):
    CLOSE = 'CLS'
    AVERAGE = 'AVG'
    DISTANT = 'DIS'

    DISTANCE_SHOW = {
        CLOSE: 'Близкая',
        AVERAGE: 'Средняя',
        DISTANT: 'Далекая'
    }

    DISTANCE_CHOICES = (
        (CLOSE, 'Близкая'),
        (AVERAGE, 'Средняя'),
        (DISTANT, 'Далекая')
    )

    distance = models.CharField(max_length=3, choices=DISTANCE_CHOICES, blank=True)

    def title_show(self):
        title_choices_dict = {k: v for k, v in self.DISTANCE_CHOICES}
        return "%s" % title_choices_dict.get(self.distance, self.distance)

    def __str__(self):
        return '%s' % self.distance


class DanceStyleInSectionAveragePrice(models.Model):
    LOW = 'LOW'
    AVERAGE = 'AVG'
    HIGH = 'HIG'

    PRICE_SHOW = {
        LOW: 'Низкий',
        AVERAGE: 'Средний',
        HIGH: 'Высокий'
    }

    PRICE_CHOICES = (
        (LOW, 'Низкий'),
        (AVERAGE, 'Средний'),
        (HIGH, 'Высокий')
    )

    price = models.CharField(max_length=3, choices=PRICE_CHOICES, blank=True)

    def title_show(self):
        title_choices_dict = {k: v for k, v in self.PRICE_CHOICES}
        return "%s" % title_choices_dict.get(self.price, self.price)

    def __str__(self):
        return '%s' % self.price


class DanceStyleInSectionAttendeeAge(models.Model):
    CHILDREN = 'CHD'
    MIXED = 'MXD'
    GROWN_UPS = 'GUP'

    ATTENDEE_AGE_CHOICES = (
        (CHILDREN, 'Дети'),
        (MIXED, 'Смешанная группа'),
        (GROWN_UPS, 'Взрослые')
    )

    attendee_age = models.CharField(max_length=3, choices=ATTENDEE_AGE_CHOICES, blank=True)

    def title_show(self):
        title_choices_dict = {k: v for k, v in self.ATTENDEE_AGE_CHOICES}
        return "%s" % title_choices_dict.get(self.attendee_age, self.attendee_age)

    def __str__(self):
        return '%s' % self.attendee_age
