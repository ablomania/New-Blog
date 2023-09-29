from django.shortcuts import render
from .models import Articles, Usercomments
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    myarticles = Articles.objects.all().order_by('-date_posted')[:5]
    lastarticle = Articles.objects.filter().last()
    context = {
        'myarticles' : myarticles, 'lastitem' : lastarticle,
    }
    return HttpResponse(template.render(context, request))


def read(request,id):
    template = loader.get_template('read.html')
    lastarticle = Articles.objects.filter().last()
    openarticle = Articles.objects.get(id=id)
    otherarticles = Articles.objects.all().order_by('date_posted')
    if openarticle.id == lastarticle.id:
        readerf = 1
    else:
        readerf = openarticle.id +1
    if openarticle.id == 1:
        readerb = 1
    else:
        readerb = openarticle.id - 1
    context = {
        'open' : openarticle, 'otherarticles' : otherarticles, 'readerf': readerf, 'readerb': readerb,
    }
    openarticle = readerf
    return HttpResponse(template.render(context, request))

def articles(request):
    template = loader.get_template('articles.html')
    myarticles = Articles.objects.all()
    context = {
        'myarticles' : myarticles,
    }
    return HttpResponse(template.render(context, request))

def contact(request):
    template = loader.get_template('contact.html')
    context = {
        'name' : 'Abel Amarteifio', "Telephone" : '0598779958', 'email': 'abelamarteifio@gmail.com'
    }
    return HttpResponse(template.render(context, request))

def comment(request,name):
    template = loader.get_template('comments.html')
    mycomments = Usercomments.objects.get(comments = name)
    context = {
        'mycomments' : mycomments,
    }
    return HttpResponse(template.render(context, request))