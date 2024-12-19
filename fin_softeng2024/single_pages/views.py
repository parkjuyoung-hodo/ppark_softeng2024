from django.shortcuts import render
from .models import Portfolio

# Create your views here.

def landing(request):
    return render(
        request,
        'single_pages/landing.html'
    )

def about_me(request):
    return render(
        request,
        'single_pages/about_me.html'
    )

def raspberry(request):
    portfolios = Portfolio.objects.all()
    categories = Portfolio.objects.values_list('category', flat=True).distinct()

    return render(request, 'single_pages/raspberry.html', {
        'portfolios': portfolios,
        'categories': categories,
    })

