from django.shortcuts import render
from .models import Articles, Usercomments
from django.http import HttpResponse
from django.template import loader

# Create your views here.
#Index page
def index(request):
    template = loader.get_template('index.html')
    myarticles = Articles.objects.all().order_by('-date_posted')[:5]
    lastarticle = Articles.objects.filter().last()
    context = {
        'myarticles' : myarticles, 'lastitem' : lastarticle,
    }
    return HttpResponse(template.render(context, request))

#for reading page
def read(request,id):
    template = loader.get_template('read.html')
    lastarticle = Articles.objects.filter().last()
    openarticle = Articles.objects.get(id=id)
    otherarticles = Articles.objects.all().order_by('date_posted')
    mycomments = Usercomments.objects.filter(relatedarticle_id=openarticle.id).values()[:15]
    if openarticle.id == lastarticle.id:
        readerf = 1
    else:
        readerf = openarticle.id +1
    if openarticle.id == 1:
        readerb = 1
    else:
        readerb = openarticle.id - 1
    context = {
        'open' : openarticle, 'otherarticles' : otherarticles, 'readerf': readerf, 'readerb': readerb, 'mycomments': mycomments,
    }
    if request.method == 'POST':
        name = request.POST['name']
        comment = request.POST['comment']
        new_comment = Usercomments(name=name, comnt=comment, relatedarticle_id = openarticle.id)
        new_comment.save()
    openarticle.id = readerf
    return HttpResponse(template.render(context, request))

#for articles page
def articles(request):
    template = loader.get_template('articles.html')
    myarticles = Articles.objects.all()
    context = {
        'myarticles' : myarticles,
    }
    return HttpResponse(template.render(context, request))

#for contact page
def contact(request):
    template = loader.get_template('contact.html')
    context = {
        'name' : 'Abel Amarteifio', "Telephone" : '0598779958', 'email': 'abelamarteifio@gmail.com'
    }
    return HttpResponse(template.render(context, request))

