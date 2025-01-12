from django.shortcuts import render


def index(request):
    return render(request, "index.html")

def users(request):
    return render(request, "users.html")

def hello(request):
    name = "보근"
    tags = ["python", "django", "html", "css"]
    books = ["해변의 카프카", "코스모스", "어린왕자", "AI"]


    context = {
        "name" : name,
        "tags" : tags,
        "books" : books,
    }
    return render(request, "hello.html", context)