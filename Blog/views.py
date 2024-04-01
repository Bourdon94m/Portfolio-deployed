from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Category, BlogPost


# Create your views here.

def index(request):
    posts = BlogPost.objects.all()  # Get all Posts from models
    categories = Category.objects.all()  # Get all categories from models

    return render(request, 'main/index.html', context={"categorys": categories,
                                                       "posts": posts})


def detail(request, slug):
    product = get_object_or_404(BlogPost, slug=slug)
    categories = Category.objects.all()

    return render(request, 'main/detail_post.html', context={"product": product,
                                                             "categories": categories})


def ressources_page(request):
    return render(request, 'main/ressources.html')