from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Content
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from .forms import CommentForm


# Create your views here.
def index(request):
    content_list = Content.objects.order_by('-publication_date')
    content_in_carousel = content_list[:2]
    page = request.GET.get('page', 1)
    news = content_list.filter(status=1)
    information = content_list.filter(status=2)
    list_potensi = content_list.filter(status=3)
    paginator = [Paginator(news, 4), Paginator(information,4)]
    try:
        news_content = paginator[0].page(page)
        information_content = paginator[1].page(page)
    except PageNotAnInteger:
        news_content = paginator[0].page(1)
        information_content = paginator[1].page(1)
    except EmptyPage:
        news_content = paginator[0].page(paginator[0].num_pages)
        information_content = paginator[1].page(paginator[1].num_pages)
    template = loader.get_template('desajono/index.html')
    context = {
        'news_content' : news_content,
        'information_content' : information_content,
        'content_in_carousel' : content_in_carousel,
        'potensi' : list_potensi
    }
    return HttpResponse(template.render(context, request))
    #return HttpResponse(news_content)

def see_article(request, slug, year, month):
    content = Content.objects.filter(publication_date__year=year, publication_date__month = month).get(slug=slug)
    another_content_list = Content.objects.exclude(publication_date__year=year, publication_date__month = month, slug=slug).filter(status=content.status).order_by('-publication_date')[:3]
    template = loader.get_template('desajono/content.html')
    #Komentar
    post = get_object_or_404(Content, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    context = {
        'content' : content,
        'another_content' : another_content_list,
        'post': post,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form
    }
    return HttpResponse(template.render(context, request))
    #return HttpResponse(another_content_list)

def open_technopark(request):
    content = Content.objects.all()
    template = loader.get_template('desajono/technopark.html')
    context = {
        'content' : content,
    }
    return HttpResponse(template.render(context, request))
