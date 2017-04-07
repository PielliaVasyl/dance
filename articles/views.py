from django.shortcuts import render

from entities.models import Article


def article_list_show(request):
    title = 'Article List'
    articles = Article.objects.all()
    context = {
        'title': title,
        'articles': articles
    }
    return render(request, 'article_list.html', context)
