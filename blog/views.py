from django.urls import reverse
from blog.models import Blog
from django.shortcuts import render, redirect, render_to_response
import os
import json


def index(request):
    filelist = os.listdir('c:/code/myblog/blog/static/picture')
    for files in filelist:
        Olddir = os.path.join('c:/code/myblog/blog/static/picture', files)
        filename = os.path.splitext(files)[0]
        filetype = os.path.splitext(files)[1]
        Newdir = os.path.join(
            'c:/code/myblog/blog/static/picture', filename + ".jpg")
        os.rename(Olddir, Newdir)
    a = Blog.objects.all()
    dict1={}
    for i in a:
        dict1['title'+str(i.id)]=i.title
        dict1['brief'+str(i.id)]=i.brief
        dict1['time'+str(i.id)]=i.time
        dict1['picture'+str(i.id)]=i.picture
        dict1['article'+str(i.id)]=i.article
    return HttpResponse(json.dumps(dict1), content_type="application/json")
