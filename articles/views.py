from django.shortcuts import render
from .models import Articles

def index(request):
    return render(request, "index.html")

def articles(request):
    articles = Articles.objects.all()
    context = {
        'articles' : articles,
    }
    return render(request, "articles.html", context)

def new(request):
    return render(request, "new.html")

def data_throw(request):
    return render(request, "data_throw.html")

def data_catch(request):
    data = request.GET.get("message")
    context = {
        "data": data
    }
    return render(request, "data_catch.html", context)

