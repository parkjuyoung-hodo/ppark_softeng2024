from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.views.generic import DetailView
from .models import Raspberry, Warning, Ara
from .forms import EmailForm
from django.db.models import Q


# Create your views here.

def landing(request):
    return render(
        request,
        'single_pages/landing.html'
    )

def raspberry(request):
    query = request.GET.get('q')
    category = request.GET.get('category')
    raspberry = Raspberry.objects.all().order_by('-created_at')

    if query:
        raspberry = raspberry.filter(
            Q(title__icontains=query) |
            Q(hook_text__icontains=query)
        )

    if category:
        raspberry = raspberry.filter(category=category)

    categories = Raspberry.objects.values_list('category', flat=True).distinct()

    return render(request, 'single_pages/raspberry.html', {
        'raspberry': raspberry,
        'categories': categories,
    })

class RaspberryDetailView(DetailView):
    model = Raspberry
    template_name = 'single_pages/raspberry_details.html'
    context_object_name = 'post'


def ara(request):
    query = request.GET.get('q')
    category = request.GET.get('category')
    ara = Ara.objects.all().order_by('-created_at')

    if query:
        ara = ara.filter(
            Q(title__icontains=query) |
            Q(hook_text__icontains=query)
        )

    if category:
        ara = ara.filter(category=category)

    categories = Ara.objects.values_list('category', flat=True).distinct()

    return render(request, 'single_pages/ara.html', {
        'ara': ara,
        'categories': categories,
    })

class AraDetailView(DetailView):
    model = Ara
    template_name = 'single_pages/ara_details.html'
    context_object_name = 'post'


def warning(request):
    warning = Warning.objects.all()
    return render(request, 'single_pages/warning.html', {'warning': warning})


def send_email_view(request):
    form = EmailForm()
    success = None
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
                success = True
            except Exception:
                success = False

    return render(request, 'single_pages/send_email.html', {'form': form, 'success': success})