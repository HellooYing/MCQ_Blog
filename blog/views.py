#encoding: utf-8
from django.urls import reverse
from blog.models import Blog
from django.shortcuts import render, redirect, render_to_response,get_object_or_404
from django.http import HttpResponse
import os
import json
from datetime import datetime
from PIL import Image
def index(request):
    path=os.path.realpath(__file__)
    path1=path.strip(r'views.py')
    filelist = os.listdir(path1+'static/picture')
    for files in filelist:
        Olddir = os.path.join(path1+'static/picture', files)
        filename = os.path.splitext(files)[0]
        filetype = os.path.splitext(files)[1]
        Newdir = os.path.join(path1+'static/picture', filename + ".jpg")
        os.rename(Olddir, Newdir)
    a = Blog.objects.all()
    return render(request, "index.html",context={"all_blogs": a})

def index_waterfall(request):
    a = Blog.objects.all()
    dict1={}
    length=[]
    path=os.getcwd()+r'/blog/static/picture/i'
    print(os.getcwd())
    for i in a:
        dict1['title['+str(i.id)+']']=i.title
        length.append(i.id)
        dict1['brief['+str(i.id)+']']=i.brief
        dict1['time['+str(i.id)+']']=i.time
        dict1['picture['+str(i.id)+']']=i.picture
        dict1['article['+str(i.id)+']']=i.article
        path2=str(i.id)+'.jpg'
        img=os.path.join(path+path2)
        img2=Image.open(img)
        wch=img2.size[0]/img2.size[1]
        dict1['wch['+str(i.id)+']']=wch
    dict1['length']=len(length)
    class CJsonEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, datetime):
                return obj.strftime('%Y-%m-%d %H:%M:%S')
            elif isinstance(obj, date):
                return obj.strftime('%Y-%m-%d')
            else:
                return json.JSONEncoder.default(self, obj)
    return HttpResponse(json.dumps(dict1, cls=CJsonEncoder), content_type="application/json")

def detail(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    return render(request, 'detail.html', context={'post': post})
