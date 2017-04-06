from django.shortcuts import render

from entities.models import Classes


def classes_show(request):
    title = 'EventScheme'
    classes = Classes.objects.all()
    context = {
        'title': title,
        'classes': classes
    }
    return render(request, 'classes.html', context)
