from django.db import models
import datetime
class Blog(models.Model):
    id = models.IntegerField(auto_created=True,primary_key=True)
    title = models.CharField('文章标题',max_length = 150)
    brief = models.CharField('文章简介',max_length = 150)
    article = models.TextField('正文')
    time = models.DateTimeField('时间',default = datetime.datetime.now)
    picture = models.CharField('配图地址',max_length = 150,default = '../static/picture/i.jpg')
    class Meta:
        ordering = ["-time"]

# class Img(models.Model):
#     blog = models.ForeignKey(Blog, blank=True,null=True,verbose_name='文章标题')
#     img1 = models.CharField('配图1', max_length = 150)
#     img2 = models.CharField('配图2', max_length = 150)
#     img3 = models.CharField('配图3', max_length = 150)
#     img4 = models.CharField('配图4', max_length = 150)
#     img5 = models.CharField('配图5', max_length = 150)

