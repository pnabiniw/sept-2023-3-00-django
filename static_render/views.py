from django.shortcuts import render


def static_home(request):
    return render(request, template_name='static_render/static_home.html',
                  context={"title": "Static Test"})


def portfolio(request):
    return render(request, template_name="static_render/portfolio.html")
