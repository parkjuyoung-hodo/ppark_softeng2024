from django.urls import path
from . import views

app_name = 'single_pages'

urlpatterns = [
    path('', views.landing),
    path('raspberry/', views.raspberry, name='raspberry'),
    path('raspberry/<int:pk>/', views.RaspberryDetailView.as_view(), name='raspberry_details'),
    path('warning/', views.warning, name='warning'),
    path('send-email/', views.send_email_view, name='send_email'),
]