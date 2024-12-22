from django.urls import path
from . import views

app_name = 'single_pages'

urlpatterns = [
    path('about_me/', views.about_me),
    path('', views.landing),
    path('raspberry/', views.raspberry, name='raspberry'),
    path('raspberry/<int:pk>/', views.RaspberryDetailView.as_view(), name='raspberry_details'),
]