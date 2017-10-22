from django.urls import reverse
from blog.models import Blog
from django.shortcuts import render, redirect,render_to_response
import os

def index(request):
    filelist=os.listdir('c:/code/myblog/blog/static/picture')#该文件夹下所有的文件（包括文件夹）
    for files in filelist:#遍历所有文件
        Olddir=os.path.join('c:/code/myblog/blog/static/picture',files);#原来的文件路径
        filename=os.path.splitext(files)[0];#文件名
        filetype=os.path.splitext(files)[1];#文件扩展名
        Newdir=os.path.join('c:/code/myblog/blog/static/picture',filename+".jpg");#新的文件路径
        os.rename(Olddir,Newdir);#重命名
    a=Blog.objects.all()
    return render(request,'index.html',context={"all_blog":a})
