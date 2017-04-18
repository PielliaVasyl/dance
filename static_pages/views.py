from django.shortcuts import render, redirect

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
