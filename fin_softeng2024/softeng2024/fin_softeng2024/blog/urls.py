from django.urls import path
from . import views

app_name = 'blog'

urlpatterns=[
   path('', views.PostList.as_view(), name='blog'),
   path('<int:pk>/',views.PostDetail.as_view()),
]