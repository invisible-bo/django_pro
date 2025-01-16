from django.shortcuts import render
from .models import Articles

def index(request):
    return render(request, "index.html")

def articles(request):
    articles = Articles.objects.all().order_by("-pk")
    context = {
        'articles' : articles,
    }
    return render(request, "articles.html", context)

def new(request):
    return render(request, "new.html")

def create(request):
    title = request.GET.get("title")
    content = request.GET.get("content")

    # 새로운 Article 저장
    Articles.objects.create(title=title, content=content)
    return render(request, "create.html")


def data_throw(request):
    return render(request, "data_throw.html")

def data_catch(request):
    data = request.GET.get("message")
    context = {
        "data": data
    }
    return render(request, "data_catch.html", context)

