from django.shortcuts import render # render라고도 쓸 수 있는건가
from django.views.generic import ListView, DetailView
from .models import Post, Category, Tag
from .forms import CommentForm

class PostList(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    ordering = '-pk'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context= super(PostList, self).get_context_data()
        context['categories'] =Category.objects.all()
        context['no_category_post_count'] =Post.objects.filter(category=None).count()
        return context

def category_page(request, slug):
    if slug == 'no_category':
        category = '미분류'
        post_list = Post.objects.filter(Category=None)

    else:
        category = Category.objects.get(slug=slug)
        post_list = Post.objects.filter(category=category)


    return render(
        request,
        'blog/category_page.html',
        {
            'post_list': post_list,
            'categories': Category.objects.all(),
            'no_category_post_count': Post.objects.filter(category=None).count(),
            'category': category,
        }
    )

def tag_page(request,slug):
    tag = Tag.objects.get(slug=slug)
    post_list =tag.post_set.all()

    return render(
        request,
        'blog/tag_page.html',
        {
            'post_list' : post_list,
            'tag': tag,
            'categories' : Category.objects.all(),
            'no_category_post_count': Post.objects.filter(category= None).count()
        }
    )


class PostDetail(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data()
        context['categories'] =Category.objects.all()
        context['no_category_post_count']= Post.objects.filter(category=None).count()
        return context

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['form'] = CommentForm()
    #     context['comments'] = self.object.comments.all()
    #     return context
    #
    # def post(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #     form = CommentForm(request.POST)
    #     if form.is_valid():
    #         comment = form.save(commit=False)
    #         comment.post = self.object
    #         comment.save()
    #         return redirect(self.object.get_absolute_url())
    #     return self.get(request, *args, **kwargs)





# Create your views here.
# def index(request):
#     posts= Post.objects.all()
#
#     return render(
#         request,
# 'blog/index.html',
#         {
#             'post': posts,
#         }
#     )
