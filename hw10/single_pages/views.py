from django.shortcuts import render
import pandas as pd

# Create your views here.
def landing_page(request):
    return render(request, 'single_pages/landing.html', {'title': 'Home'})

def juyoung_page(request):
    return render(request, 'single_pages/juyoung_page.html', {'title': 'Juyoung Page'})

def eunbin_page(request):
    return render(request, 'single_pages/eunbin_page.html', {'title': 'Eunbin Page'})


def blog_list(request):

    df = pd.read_csv("data.csv")
    post_list = []
    for i, row in df.iterrows():
        post_list.append({
            "title": row["title"],
            "content": row["content"],
            "date": row["date"]
        })

    print(post_list)

    return render(request, 'single_pages/blog.html', {'title': 'Blog List', 'posts': post_list})