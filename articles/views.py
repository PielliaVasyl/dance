from django.shortcuts import render, get_object_or_404

from entities.models import Article


def article_list_show(request):
    title = 'Статьи о танцах'
    articles = Article.objects.all()
    context = {
        'title': title,
        'articles': articles
    }
    return render(request, 'articles/articles.html', context)


def article_show(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    title = '%s' % (article.title,)

    context = {
        'title': title,
        'article': article
    }
    return render(request, 'articles/article-single.html', context)

