from django.shortcuts import render,get_object_or_404
from .models import post,category

# Create your views here.

def blog(request):
    posts = post.objects.all()
    return render(request,"blog/blog.html",{'posts':posts})

def Category (request,category_id):
    Category = get_object_or_404(category, id=category_id)
    return render(request,"blog/category.html",{'Category':Category})