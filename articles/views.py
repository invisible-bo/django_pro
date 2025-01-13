from django.shortcuts import render


def index(request):
    return render(request, "index.html")


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

def data_throw(request):
    return render(request, "data_throw.html")

def data_catch(request):
    data = request.GET.get("message")
    context = {
        "data": data
    }
    return render(request, "data_catch.html", context)

