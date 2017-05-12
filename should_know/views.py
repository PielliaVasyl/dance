from django.shortcuts import render


def should_know_show(request):
    title = 'Полезно знать'

    context = {
        'title': title,
    }
    return render(request, 'should_know/should-know.html', context)
