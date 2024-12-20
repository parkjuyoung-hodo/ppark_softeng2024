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
    query = request.GET.get('q')  # 검색어 가져오기
    category = request.GET.get('category')  # 카테고리 값 가져오기
    portfolios = Portfolio.objects.all()  # 전체 데이터 가져오기

    if query:  # 검색어가 있을 경우
        portfolios = portfolios.filter(title__icontains=query)

    if category:  # 카테고리 값이 있을 경우
        portfolios = portfolios.filter(category=category)

    categories = Portfolio.objects.values_list('category', flat=True).distinct()  # 중복 없는 카테고리 목록

    return render(request, 'single_pages/raspberry.html', {
        'portfolios': portfolios,  # 필터링된 데이터
        'categories': categories,  # 카테고리 목록
    })
