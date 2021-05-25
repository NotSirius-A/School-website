from django.conf.urls import url
from django.http.response import Http404
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from .models import Article
from .forms import ArticleForm

def article_list_view(request, *args, **kwargs):
    """Django-view,
    display a list of articles
    """


    articles = Article.objects.filter(show_on_lists=True)
    articles = articles.order_by("-date")

    num_of_elements_per_page = 8

    p = Paginator(articles, num_of_elements_per_page)
    page = p.get_page(request.GET.get('p'))

    #put articles in a list instead of looping through 'page' in templates, 
    # so its more readable in the front end
    articles = [x for x in page]

    print(p.num_pages)

    context = {
        'articles': articles,
        'page': page,
        'last_page_num': p.num_pages,
    }

    return render(request, 'articles/article_list.html', context=context)


def article_entire_view(request, *args, **kwargs):
    """Django-view,
    display an entire article on the page
    """


    url_info = request.path_info.split('/')
    url_info = [x for x in url_info if x != '']

    slug = url_info[-1]

    try:
        result = Article.objects.filter(slug=slug)[0]
    except IndexError:
        raise Http404("Article does not exist")

    context = {
        'article': result,
    }

    return render(request, 'articles/article_entire.html', context=context)


@login_required
def article_form_view(request, *args, **kwargs):
    """Django-view,
    display a form where an auth'ed user can create articles
    """


    form = ArticleForm(request.POST or None)

    if form.is_valid():
        form.save()
        
        #after the form has been verified and saved redirect users to the list of articles
        return redirect('article_list')


    context = {
        'form': form,
    }

    return render(request, 'articles/article_form.html', context=context)
