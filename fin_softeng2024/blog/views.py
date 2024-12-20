from django.shortcuts import redirect
from django.views.generic import ListView,DetailView
from .models import Post
from .forms import CommentForm

class PostList(ListView):
    model = Post
    template_name= 'blog/blog.html'
    ordering= '-pk'
    paginate_by = 3

class PostDetail(DetailView):
    model = Post
    template_name='blog/blog_details.html'

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        context['form'] = CommentForm()
        context['comments'] = self.object.comments.all()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object
            comment.save()
            return redirect(self.object.get_absolute_url())
        return self.get(request, *args, **kwargs)