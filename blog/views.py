from django.urls import reverse
from blog.models import Blog
from django.shortcuts import render, redirect,render_to_response
def index(request):
    return render(request,'index.html',{})
