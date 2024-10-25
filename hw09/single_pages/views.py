from django.shortcuts import render

# Create your views here.
def landing_page(request):
    return render(request, 'single_pages/landing.html', {'title': 'Home'})

def juyoung_page(request):
    return render(request, 'single_pages/juyoung_page.html', {'title': 'Juyoung Page'})

def eunbin_page(request):
    return render(request, 'single_pages/eunbin_page.html', {'title': 'Eunbin Page'})


def blog_list(request):
    post_list = [
        {
            'title': 'First Post',
            'content': 'This is the first post'
        },
        {
            'title': 'Second Post',
            'content': 'This is the second post'
        }
    ]
    return render(request, 'single_pages/blog.html', {'title': 'Blog List', 'posts': post_list})