from django.shortcuts import render

from entities.forms import VisitorMessageForm


def about_show(request):
    title = 'О Компании'
    context = {
        'title': title
    }
    return render(request, 'static_pages/about.html', context)


def contacts_show(request):
    title = 'Наши контакты'
    message_form = VisitorMessageForm(request.POST or None)
    msg_sent = False

    context = {
        'title': title,
        'msg_sent': msg_sent,
        'form': message_form
    }

    if message_form.is_valid():
        message_form.save()
        context['form'] = VisitorMessageForm()
        context['msg_sent'] = True

    return render(request, 'static_pages/contacts.html', context)


def dance_party_calendar_show(request):
    title = 'Календарь танцевальных вечеринок'

    context = {
        'title': title
    }
    return render(request, 'static_pages/dance_party_calendar.html', context)


def page_not_found(request):
    title = 'Страница не найдена - Ошибка 404'

    context = {
        'title': title
    }
    return render(request, 'static_pages/404.html', context)


def page_500(request):
    title = 'Ошибка сервера - Ошибка 500'

    context = {
        'title': title
    }
    return render(request, 'static_pages/500.html', context)


def page_permission_denied(request):
    title = 'Отказано в доступе - Ошибка 403'

    context = {
        'title': title
    }
    return render(request, 'static_pages/403.html', context)


def page_bad_request_view(request):
    title = 'Неверный запрос - Ошибка 400'

    context = {
        'title': title
    }
    return render(request, 'static_pages/400.html', context)
