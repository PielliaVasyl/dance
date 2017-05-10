from django.db import models


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
