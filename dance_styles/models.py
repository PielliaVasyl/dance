from django.db import models


class CountType(models.Model):
    SOLO = 'SOL'
    PARTNER = 'PRN'
    GROUP = 'GRP'

    COUNT_TYPE_CHOICES = (
        (SOLO, 'Одиночный'),
        (PARTNER, 'Парный'),
        (GROUP, 'Групповой')
    )

    count_type = models.CharField(max_length=3, choices=COUNT_TYPE_CHOICES, blank=True)

    def __str__(self):
        return '%s' % self.count_type


class BetweenPartnersDistance(models.Model):
    CLOSE = 'CLS'
    AREVAGE = 'AVG'
    DISTANT = 'DIS'

    DISTANCE_CHOICES = (
        (CLOSE, 'Близкое'),
        (AREVAGE, 'Среднее'),
        (DISTANT, 'Далекое')
    )

    distance = models.CharField(max_length=3, choices=DISTANCE_CHOICES, blank=True)

    def __str__(self):
        return '%s' % self.distance


class AveragePrice(models.Model):
    LOW = 'LOW'
    AVERAGE = 'AVG'
    HIGH = 'HIG'

    PRICE_CHOICES = (
        (LOW, 'Низкая'),
        (AVERAGE, 'Средняя'),
        (HIGH, 'Высокая')
    )

    price = models.CharField(max_length=3, choices=PRICE_CHOICES, blank=True)

    def __str__(self):
        return '%s' % self.price
