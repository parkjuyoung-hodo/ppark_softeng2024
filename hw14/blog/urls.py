from django.urls import path
from .views import PostList, PostDetail, PostCreate, category_posts, tag_page, PostUpdate

urlpatterns = [
    path('',PostList.as_view(), name='post_list'),
    path('blog/',PostList.as_view(), name='post_list'),
    path('blog/<int:pk>/',PostDetail.as_view(), name='post_detail'),
    path('category/<int:category_id>/', category_posts, name='category_posts'),
    path('tag/<slug:slug>/', tag_page, name='tag_page'),
    path('blog/create_post/', PostCreate.as_view(), name='create_post'),
    path('blog/update_post/<int:pk>/', PostUpdate.as_view(), name='update_post'),
]