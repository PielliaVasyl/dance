from django.shortcuts import render


def about_show(request):
    title = 'О Компании'
    context = {
        'title': title
    }
    return render(request, 'static_pages/about.html', context)


def contacts_show(request):
    title = 'Наши контакты'
    context = {
        'title': title
    }
    return render(request, 'static_pages/contacts.html', context)
