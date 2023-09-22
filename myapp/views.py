from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("<h1>Hello I'm learning Django</h1>")


def root(request):
    people = [
        {"first": "Jon", "last": "Doe", "address": "KTM"},
        {"first": "Jane", "last": "Doe", "address": "PKR"},
        {"first": "Bruce", "last": "Wayne", "address": "BKT"},
        {"first": "Hary", "last": "Potter", "address": "LTP"},
    ]
    return render(request, template_name="myapp/root.html", context={"title": "Root Page",
                                                                     "people": people})
    # return HttpResponse("""
    # <html>
    # <head></head>
    # <body>
    # <h1>Hello World</h1>
    # </body>
    # </html>
    # """)

