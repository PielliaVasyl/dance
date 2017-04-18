from django.shortcuts import render

from entities.models import Article


def article_list_show(request):
    title = 'Статьи о танцах'
    articles = Article.objects.all()
    context = {
        'title': title,
        'articles': articles
    }
    return render(request, 'articles/articles.html', context)
