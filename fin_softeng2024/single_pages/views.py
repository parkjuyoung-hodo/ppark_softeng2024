from django.shortcuts import render
from django.views.generic import DetailView
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
    query = request.GET.get('q')
    category = request.GET.get('category')
    portfolios = Portfolio.objects.all().order_by('-created_at')

    if query:
        portfolios = portfolios.filter(title__icontains=query)

    if category:
        portfolios = portfolios.filter(category=category)

    categories = Portfolio.objects.values_list('category', flat=True).distinct()  # 중복 없는 카테고리 목록

    return render(request, 'single_pages/raspberry.html', {
        'portfolios': portfolios,
        'categories': categories,
    })

class RaspberryDetailView(DetailView):
    model = Portfolio
    template_name = 'single_pages/raspberry_details.html'
    context_object_name = 'post'
