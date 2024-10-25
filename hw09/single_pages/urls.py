from django.urls import path
from . import views

app_name = "single_pages"

urlpatterns = [
    path('eunbin_page/', views.eunbin_page, name='eunbin_page'),
    path('juyoung_page/', views.juyoung_page, name='juyoung_page'),
    path("", views.landing_page, name='landing_page'),
    path("blog/", views.blog_list, name='blog_list'),
]