from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home_view(request, *args, **kwargs):
    # return HttpResponse("<h1>hello World<h1>")
    return render(request, 'home.html', {})


def contact_view(request, *args, **kwargs):
    return render(request, 'contact.html', {})


def about_view(request, *args, **kwargs):
    my_context = {
        "my_text": "This is about me.",
        "my_number": 123,
        "my_list": [10, 20, 30]
    }
    return render(request, 'about.html', my_context)
