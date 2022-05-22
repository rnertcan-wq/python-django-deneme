from django.http.response import HttpResponse
from blog.models import Blog, Category

from django.shortcuts import render



# Create your views here.
def index(request):
    context = {
        "blogs": Blog.objects.filter(is_activate=True, is_home=True),
        "categories": Category.objects.all()
    }
    return render(request, "blog/index.html", context)

def blogs(request):
    context = {
        "blogs": Blog.objects.filter(is_activate=True),
        "categories": Category.objects.all()
    }
    return render(request, "blog/blogs.html", context)

def blog_details(request, slug):

    blog = Blog.objects.get(slug=slug)



    return render(request, "blog/blog-details.html", {
        "blog": blog
    })

def blogs_by_category(request, slug):
    context = {
        "blogs" : Blog.objects.filter(is_activate=True, category__slug=slug),
        "categories": Category.objects.all()
    }
    return render(request, "blog/blogs.html", context)