#encoding: utf-8
from django.urls import reverse
from blog.models import Blog,Comment
from django.shortcuts import render, redirect, render_to_response,get_object_or_404
from django.http import HttpResponse
import os
import json
from datetime import datetime
from PIL import Image
import shutil

def index(request):
    path=os.path.realpath(__file__)
    path1=path.strip(r'views.py')
    shutil.copy(path1+"../db.sqlite3",path1+"../../db.sqlite3")
    filelist = os.listdir(path1+'static/picture')
    for files in filelist:
        Olddir = os.path.join(path1+'static/picture', files)
        filename = os.path.splitext(files)[0]
        filetype = os.path.splitext(files)[1]
        Newdir = os.path.join(path1+'static/picture', filename + ".jpg")
        os.rename(Olddir, Newdir)
    a = Blog.objects.all()
    return render(request, "index.html",context={"all_blogs": a})

def phone(request):
    path=os.path.realpath(__file__)
    path1=path.strip(r'views.py')
    shutil.copy(path1+"../db.sqlite3",path1+"../../db.sqlite3")
    filelist = os.listdir(path1+'static/picture')
    for files in filelist:
        Olddir = os.path.join(path1+'static/picture', files)
        filename = os.path.splitext(files)[0]
        filetype = os.path.splitext(files)[1]
        Newdir = os.path.join(path1+'static/picture', filename + ".jpg")
        os.rename(Olddir, Newdir)
    a = Blog.objects.all()
    return render(request, "phone.html",context={"all_blogs": a})

def categories(request):
    path=os.path.realpath(__file__)
    path1=path.strip(r'views.py')
    shutil.copy(path1+"../db.sqlite3",path1+"../../db.sqlite3")
    filelist = os.listdir(path1+'static/picture')
    for files in filelist:
        Olddir = os.path.join(path1+'static/picture', files)
        filename = os.path.splitext(files)[0]
        filetype = os.path.splitext(files)[1]
        Newdir = os.path.join(path1+'static/picture', filename + ".jpg")
        os.rename(Olddir, Newdir)
    a = Blog.objects.all()
    return render(request, "categories.html",context={"all_blogs": a})

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
        dict1['picture['+str(i.id)+']']='../static/picture/i'+str(i.id)+'.jpg'
        dict1['article['+str(i.id)+']']=i.article
        dict1['zan['+str(i.id)+']']=i.zan
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
    try:
        com = Comment.objects.filter(bkid=pk)
    except:
        com=0
    if com!=0:
        return render(request, 'detail.html', {'post': post,'com':com})
    else:
        return render(request, 'detail.html', {'post': post})



def comm(request):
    a=Comment()
    a.bkid=request.GET.get("bkid")  
    a.mean=request.GET.get("review")
    a.user=request.GET.get("name")
    a.save()
    aa = Blog.objects.all()
    return render(request, "index.html",context={"all_blogs": aa})
    

def zan(request):
    post=Blog.objects.get(id=request.GET.get("id"))
    post.zan=post.zan+1
    post.save()
    aa = Blog.objects.all()
    return render(request, "index.html",context={"all_blogs": aa})

def change(request):
    return render(request, "change.html",context={})

def change_img(request):
    if request.method == 'POST':
        myFile =request.FILES["pic"]
        file_name="i"+request.POST['bkid']+".jpg"
        p=os.getcwd()
        path=os.path.join(p+"/static/picture",file_name)
        if os.path.exists(path):
            os.remove(path)
        path=os.path.join(p+r"/blog/static/picture",file_name)
        if os.path.exists(path):
            os.remove(path)
        destination = open(os.path.join(p+r"/static/picture",file_name),'wb+')
        for chunk in myFile.chunks():
            destination.write(chunk)  
        destination = open(os.path.join(p+r"/blog/static/picture",file_name),'wb+')
        for chunk in myFile.chunks():
            destination.write(chunk)  
        destination.close()  
        return redirect('/change/')
    else:
        return render(request,'change.html')

def touzi(request):
    return render(request, "touzi.html",context={})

def compiler(request):
    dict2={}
<<<<<<< HEAD
    path=os.path.abspath(os.path.join(os.getcwd(), ".."))
    with open(path+r'/z.c语言代码输入.txt', 'r') as f:
        dict2['c']=f.read()
    with open(path+r'/z.token序列.txt', 'r') as f:
        dict2['token']=f.read()
    with open(path+r'/z.符号表.txt', 'r') as f:
        dict2['synbl']=f.read()
    with open(path+r'/z.四元式.txt', 'r') as f:
        dict2['four']=f.read()
    with open(path+r'/z.优化后的四元式.txt', 'r') as f:
        dict2['op']=f.read()
    with open(path+r'/z.目标代码.txt', 'r') as f:
=======
    with open('..\z.c语言代码输入.txt', 'r') as f:
        dict2['c']=f.read()
    with open('..\z.token序列.txt', 'r') as f:
        dict2['token']=f.read()
    with open('..\z.符号表.txt', 'r') as f:
        dict2['synbl']=f.read()
    with open('..\z.四元式.txt', 'r') as f:
        dict2['four']=f.read()
    with open('..\z.优化后的四元式.txt', 'r') as f:
        dict2['op']=f.read()
    with open('..\z.目标代码.txt', 'r') as f:
>>>>>>> refs/remotes/origin/master
        dict2['oc']=f.read()
    c=dict2['c']
    token=dict2['token'].split(" ")
    synbl=dict2['synbl']
    four=dict2['four'].split(" ")
    op=dict2['op'].split(" ")
    oc=dict2['oc'].split("\n")
    return render(request, "compiler.html",context={"c":c,"token":token,"synbl":synbl,"four":four,"op":op,"oc":oc })

def compiler_get(request):
    c=request.GET.get("code")
<<<<<<< HEAD
    path=os.path.abspath(os.path.join(os.getcwd(), ".."))
    with open(path+r'/z.c语言代码输入.txt', 'w') as f:
        f.write(c)
    os.system('java -jar cp.jar')  
    return render(request, "compiler.html",context={})

=======
    with open('..\z.c语言代码输入.txt', 'w') as f:
        f.write(c)
    os.system('java -jar cp.jar')  
    return render(request, "compiler.html",context={})
>>>>>>> refs/remotes/origin/master
