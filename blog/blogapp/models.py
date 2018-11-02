from django.db import models
from userapp.models import BlogUser
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
class Banner(models.Model):
    title = models.CharField('标题',max_length=50)
    img = models.ImageField('轮播图',upload_to='static/images/banner')
    img_url = models.URLField('图片链接',max_length=100)
    index = models.IntegerField('索引')
    is_active=models.BooleanField('是否激活',default=False)
    operator = models.ForeignKey(BlogUser)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name='轮播图'
        verbose_name_plural = verbose_name
class BlogCategory(models.Model):
    name = models.CharField('分类名称',max_length=20,default='')
    class Meta:
        verbose_name='博客分类'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name
class Tags(models.Model):
    name = models.CharField('标签名称',max_length=20,default='')
    class Meta:
        verbose_name='标签'
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.name
class Post(models.Model):
    #  ！！！！这里的用户到底是如何注册进入的，为啥我记得是老师注册的超级用户呢
    user = models.ForeignKey(BlogUser,verbose_name='作者')
    category=models.ForeignKey(BlogCategory,verbose_name='博客分类',default='')
    tags=models.ManyToManyField(Tags,verbose_name='标签')
    title = models.CharField('标题',max_length=50)
    content = RichTextUploadingField('内容')
    pub_date = models.DateTimeField('发布日期',auto_now_add=True)
    img = models.ImageField('博客封面',upload_to='static/images/post',default=None)
    views_num = models.IntegerField('浏览量',default=0)
    is_recommend=models.BooleanField('是否推荐博客',default=False)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name='博客'
        verbose_name_plural=verbose_name
class Comment(models.Model):
    post = models.ForeignKey(Post,verbose_name='博客')
    views = models.IntegerField('评论的点击量',default=0)  # 这是一个 用户评论被点击的数字
    user = models.ForeignKey(BlogUser,verbose_name='作者')
    pub_date = models.DateTimeField('发布时间',auto_now_add=True)
    content = models.TextField('内容')
    def __str__(self):
        return self.content
    class Meta:
        verbose_name='评论'
        verbose_name_plural=verbose_name
class FriendlyLink(models.Model):
    title = models.CharField('标题',max_length=50)
    link = models.URLField('链接',max_length=100,default='')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name='友情链接'
        verbose_name_plural=verbose_name
class Poster(models.Model):
    title = models.CharField('标题',max_length=50)
    link = models.URLField('广告地址',max_length=100,default='')
    img = models.ImageField('图片',upload_to='static/images/poster')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name='广告位'
        verbose_name_plural=verbose_name




