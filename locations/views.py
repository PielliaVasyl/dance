from django.shortcuts import render


def locations_show(request):
    title = 'Карта'

    context = {
        'title': title,
    }
    return render(request, 'locations/locations.html', context)
