from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Content


# Create your views here.
def index(request):
    content_list = Content.objects.order_by('-publication_date')
    content_in_carousel = content_list[:2]
    list_potensi = Content.objects.filter(status=3)
    template = loader.get_template('desajono/index.html')
    context = {
        'content_list' : content_list,
        'content_in_carousel' : content_in_carousel,
        'potensi' : list_potensi
    }
    return HttpResponse(template.render(context, request))

def see_article(request, slug, year, month):
    content = Content.objects.filter(publication_date__year=year, publication_date__month = month).get(slug=slug)
    another_content_list = Content.objects.exclude(publication_date__year=year, publication_date__month = month, slug=slug).filter(status=content.status)
    template = loader.get_template('desajono/content.html')
    context = {
        'content' : content,
        'another_content' : another_content_list
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
