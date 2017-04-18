from django.shortcuts import render

# Create your views here.


def index(request):
    title = 'Home page'
    context = {
        'title': title,
    }
    return render(request, 'atropos/base.html', context)
