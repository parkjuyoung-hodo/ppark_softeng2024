from django.urls import path
from .views import PostList, PostDetail, category_page, tag_page

urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('blog/', PostList.as_view(), name='post_list'),
    path('blog/<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('blog/category/<int:category_id>/', category_page, name='category_page'),
    path('blog/tag/<slug:slug>/', tag_page, name='tag_page'),
]
