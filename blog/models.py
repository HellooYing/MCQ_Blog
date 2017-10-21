from django.db import models
import datetime
class Blog(models.Model):
    title = models.CharField('文章标题',max_length = 150)
    brief = models.CharField('文章简介',max_length = 150)
    article = models.TextField('正文')
    time = models.DateTimeField('时间',default=datetime.datetime.now)
    picture = models.ImageField('配图')

# class Img(models.Model):
#     blog = models.ForeignKey(Blog, blank=True,null=True,verbose_name='文章标题')
#     img1 = models.CharField('配图1', max_length = 150)
#     img2 = models.CharField('配图2', max_length = 150)
#     img3 = models.CharField('配图3', max_length = 150)
#     img4 = models.CharField('配图4', max_length = 150)
#     img5 = models.CharField('配图5', max_length = 150)

