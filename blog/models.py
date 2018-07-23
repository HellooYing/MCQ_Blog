#encoding: utf-8
from django.db import models
import datetime
from django.urls import reverse
from django.utils.six import python_2_unicode_compatible
@python_2_unicode_compatible
class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField('文章标题',max_length = 150)
    brief = models.CharField('文章简介',max_length = 150)
    article = models.TextField('正文')
    time = models.DateTimeField('时间',default = datetime.datetime.now())
    picture = models.CharField('配图地址',max_length = 150,default = '../static/picture/i.jpg')
    kind = models.IntegerField('类型',default = 0)
    zan = models.IntegerField('赞',default = 0)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})
    class Meta:
        ordering = ["-time"]

# class Img(models.Model):
#     blog = models.ForeignKey(Blog, blank=True,null=True,verbose_name='文章标题')
#     img1 = models.CharField('配图1', max_length = 150)
#     img2 = models.CharField('配图2', max_length = 150)
#     img3 = models.CharField('配图3', max_length = 150)
#     img4 = models.CharField('配图4', max_length = 150)
#     img5 = models.CharField('配图5', max_length = 150)
@python_2_unicode_compatible
class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    bkid = models.IntegerField('博客id',default = 10000)
    mean = models.TextField('正文')
    time = models.DateTimeField('时间',default = datetime.datetime.now())
    user = models.CharField('名字',max_length = 150,default = '匿名')
    zan = models.IntegerField('赞',default = 0)
    def __str__(self):
        return str(self.mean)
    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})
    class Meta:
        ordering = ["time"]