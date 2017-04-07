from django.shortcuts import render

from entities.models import DanceClass


def classes_show(request):
    title = 'EventScheme'
    classes = DanceClass.objects.all()
    context = {
        'title': title,
        'classes': classes
    }
    return render(request, 'classes.html', context)
