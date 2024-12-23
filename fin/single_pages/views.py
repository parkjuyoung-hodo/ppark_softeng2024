from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.views.generic import DetailView
from .models import Portfolio, TeamMember
from .forms import EmailForm


# Create your views here.

def landing(request):
    return render(
        request,
        'single_pages/landing.html'
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


def warning(request):
    team_members = TeamMember.objects.all()
    return render(request, 'single_pages/warning.html', {'team_members': team_members})


def send_email_view(request):
    form = EmailForm()
    success = None  # 성공 여부를 나타내는 변수
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            sender_name = form.cleaned_data['sender_name']
            sender_email = form.cleaned_data['sender_email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            try:
                send_mail(
                    subject=f"{subject} (보낸 사람: {sender_name})",
                    message=message,
                    from_email=sender_email,
                    recipient_list=[settings.EMAIL_HOST_USER],
                )
                success = True  # 성공
            except Exception:
                success = False  # 실패

    return render(request, 'single_pages/send_email.html', {'form': form, 'success': success})