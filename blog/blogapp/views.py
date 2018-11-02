from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from .models import Banner, Post, BlogCategory, Comment, FriendlyLink, Poster, Tags
from django.db.models import Q
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator


# Create your views here.
def index(request, pIndex):
    banner_list = Banner.objects.all()
    recomment_list = Post.objects.filter(is_recommend=True)
    post_list = Post.objects.all().order_by('-pub_date')
    blogcategory = BlogCategory.objects.all()
    comment_list2 = Post.objects.filter(comment__content__isnull=False).order_by('-pub_date')
    comment_list = []


    for i in comment_list2:
        if i in comment_list:
            pass
        else:
            if len(comment_list) <8:
                comment_list.append(i)
            else:
                break
    print(comment_list)
    friendly_link_list = FriendlyLink.objects.all()
    poster_list = Poster.objects.all()
    blog_all = Post.objects.all().count()
    # 分页内容
    p = Paginator(post_list, 10)
    all = p.num_pages
    if pIndex == '':
        pIndex = 1
    page_list = p.page(pIndex)
    lp = 0
    np = 0
    if page_list.has_next():
        np = 1
    if page_list.has_previous():
        lp = 1
    page_num_list = p.page_range

    return render(request, 'index.html', locals())


def search(request):
    kw = request.POST.get('keyword', None)
    con_kw = '“{}”的搜索结果'.format(kw)
    con_list = Post.objects.filter(Q(title__contains=kw) | Q(content__contains=kw))

    com_list2 = Post.objects.filter(comment__content__isnull=False).order_by('-pub_date')
    poster_list = Poster.objects.all()
    friendly_link_list = FriendlyLink.objects.all()
    tags_list = Tags.objects.all()
    comment_list = []
    # # pIndex = int(pIndex)
    # p = Paginator(con_list, 3)
    # # page_list = p.page(pIndex)
    # all = p.num_pages
    # page_num_list = p.page_range
    for i in com_list2:
        if i in comment_list:
            pass
        else:
            comment_list.append(i)

    ctx = {
        'page_list': con_list,
        'com_list': comment_list,
        'poster_list': poster_list,
        'title': con_kw,
        'friendly_link_list': friendly_link_list,
        'tags_list': tags_list,
        # 'all':all,
        # 'page_num_list':page_num_list
    }
    return render(request, 'list.html', ctx)


def list(request, pIndex):
    con = Post.objects.all().order_by('-pub_date')
    com_list2 = Post.objects.filter(comment__content__isnull=False).order_by('-pub_date')
    poster_list = Poster.objects.all()
    comment_list = []
    for i in com_list2:
        if i in comment_list:
            pass
        else:
            comment_list.append(i)
    print(pIndex)
    tags_list = Tags.objects.all()
    friendly_link_list = FriendlyLink.objects.all()

    # 分页的内容
    p = Paginator(con, 10)
    all = p.num_pages
    if pIndex == '':
        pIndex = 1
    page_list = p.page(pIndex)
    previous_page = 0
    next_page = 0
    if page_list.has_next():
        next_page = 1
    if page_list.has_previous():
        previous_page = 1
    page_num_list = p.page_range
    ctx = {
        'title': ' 博客列表',
        'post_list': con,
        'comment_list': comment_list,
        'poster_list': poster_list,
        'tags_list': tags_list,
        'friendly_link_list': friendly_link_list,
        'page_list': page_list,
        'page_num_list': page_num_list,
        'all': all,
        'lp': previous_page,
        'np': next_page,
        'pIndex': pIndex,
    }

    return render(request, 'list.html', ctx)


def show(request, con_id):
    post_list = Post.objects.get(id=con_id)
    post_list.views_num += 1
    post_list.save()
    # 相同分类下的内容
    # same_cate = Post.objects.filter(category__name=post_list.user)
    com_list2 = Post.objects.filter(comment__content__isnull=False).order_by('-pub_date')
    poster_list = Poster.objects.all()
    friendly_link_list = FriendlyLink.objects.all()
    recommment_list = Post.objects.filter(
        Q(title__contains=post_list.title) | Q(content__contains=post_list.title)).exclude(id=con_id)
    comment_list = []  # 这个是博客的对象
    com_list = Comment.objects.filter(post__id=con_id)  # 这个是评论的对象
    blog_all = Post.objects.all().count()
    tags = post_list.tags.values()
    print(tags, '******************************')
    for i in com_list2:
        if i in comment_list:
            pass
        else:
            comment_list.append(i)
    ctx = {
        'post': post_list,
        'poster_list': poster_list,
        'comment_list': comment_list,
        'friendly_link_list': friendly_link_list,
        'recomment_list': recommment_list,
        'com_list': com_list,
        'blog_all': blog_all,
        'tags': tags
    }
    return render(request, 'show.html', ctx)


def category_list(request, bid=-1, tid=-1):
    tags_list = Tags.objects.all()
    post_list = None
    if bid != -1:
        post_list = Post.objects.filter(category__id=bid)
    if tid != -1:
        post_list = Post.objects.filter(tags__id=tid)
        tags_list = Tags.objects.exclude(id=tid)
    com_list2 = Post.objects.filter(comment__content__isnull=False).order_by('-pub_date')
    comment_list = []
    poster_list = Poster.objects.all()

    friendly_link_list = FriendlyLink.objects.all()
    for i in com_list2:
        if i in comment_list:
            pass
        else:
            comment_list.append(i)

    ctx = {
        'page_list': post_list,
        'title': ' 博客列表',
        'comment_list': comment_list,
        'poster_list': poster_list,
        'tags_list': tags_list,
        'friendly_link_list': friendly_link_list,

    }
    return render(request, 'list.html', ctx)


def comment(request):
    # request.session.get('键', 默认值)

    post_id = request.POST.get('post_id')
    nickname = request.POST.get('nickname')
    try:
        email = request.POST.get('email')
    except:
        email = ''
    content = request.POST.get('comment-textarea')
    print(content,'*((*(*(*(*(*(*(*(*(*((*((((*)*)*)*)*)*)*)*')
    user_id = request.session.get('user_id', 'xxx')
    if user_id == 'xxx':
        return redirect(reverse(('blog:show'), args=(post_id,)))

    c = Comment()
    c.post_id = post_id
    c.content = content
    c.user_id = request.session.get('user_id', 'xxx')
    c.save()
# return redirect(reverse('booktest:fan2', args=(2,3)))

    return redirect(reverse(('blog:show'), args=(post_id,)))

def a(request):
    return render(request, 'login.html')


def ifcom(request):
    print('+' * 60)
    nocom = '+' * 60
    if not request.session.get('is_login', None):
        nocom = '请登录后在发布评论'
    return JsonResponse({'a': 'love_forever', 'b': 'sure'})
    # return JsonResponse({'nocom': nocom})
def write(request):
    cate = BlogCategory.objects.all()
    tags = Tags.objects.all()
    if request.method == 'POST':
        user_id = request.session.get('user_id')
        title = request.POST.get('title')
        cate = request.POST.get('cate')
        tag = request.POST.get('tag')
        con = request.POST.get('con')
        img1 = request.FILES.get('img')
        img = 'media/static/images/post/%s'%(img1)
        img3 = 'static/images/post/%s'%(img1)
        with open(img,'wb') as pic:
            for c in img1.chunks():
                pic.write(c)
        print(img,'**********img********')
        a = Post()
        a.user_id = user_id
        a.title=title
        a.img=img3
        a.category_id = cate
        a.content = con
        a.tags_id=tag
        a.save()

        return redirect('/blog/index/')



    return render(request,'write.html',locals())

# DRF部署的部分
import json
from django.core import serializers
from blogapp import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status,mixins,generics
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import permissions
from blogapp.permissions import IsOwnerOrReadOnly
from rest_framework import viewsets
from rest_framework.reverse import reverse


# def publisher(request):
#     data = []
#     queryset = Banner.objects.all()
#     # data = serializers.serialize('json',queryset)
#     # return HttpResponse(data, content_type='application/json')
#     s = serializers.BannerSerializer(queryset,many=True)
#     return HttpResponse(json.dumps(s.data), content_type='application/json')

# @api_view(['GET','POST'])
# def publisher_list(request):
#     if request.method == 'GET':
#         queryset = Banner.objects.all()
#         s = serializers.BannerSerializer(queryset,many=True)
#         return Response(s.data)
#     if request.method == 'POST':
#         s = serializers.BannerSerializer(data=request.data)
#         if s.is_valid():
#             s.save()
#             return Response(s.data,status=status.HTTP_201_CREATED)
#         else:
#             return Response(s.errors,status=status.HTTP_400_BAD_REQUEST)
#
# @api_view(['GET','PUT','DELETE'])
# def publisher_detail(request,pk):
#     try:
#         publisher = Banner.objects.get(id=pk)
#     except:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'POST':
#         s = serializers.BannerSerializer(publisher)
#         return Response(s.data)
#     if request.method == 'PUT':
#         s = serializers.BannerSerializer(publisher,data=request.data)
#         if s.is_valid():
#             s.save()
#             return Response(s.data)
#         else:
#             return Response(status=status.HTTP_204_NO_CONTENT)
#     if request.method == 'DELETE':
#         publisher.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

class PublisherList(viewsets.ModelViewSet):
    queryset = Banner.objects.all()
    serializer_class = serializers.BannerSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    # def get(self,request,*args,**kwargs):
    #     return self.list(request,*args,**kwargs)
    # def post(self,request,*args,**kwargs):
    #     return self.create(request,*args,**kwargs)

    # def get(self,request,format=None):
    #     queryset = Banner.objects.all()
    #     s = serializers.BannerSerializer(queryset,many=True)
    #     return Response(s.data,status=status.HTTP_200_OK)
    # def post(self,request,format=None):
    #     s = serializers.BannerSerializer(data=request.data)
    #     if s.is_valid():
    #         s.save()
    #         return Response(s.data,status=status.HTTP_201_CREATED)
    #     else:
    #         return Response(s.errors,status=status.HTTP_400_BAD_REQUEST)
# class PublisherDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Banner.objects.all()
#     serializer_class = serializers.BannerSerializer
#     permission_classes = (IsOwnerOrReadOnly,)

    # def get(self,request,*args,**kwargs):
    #     return self.retrieve(request,*args,**kwargs)
    # def put(self,request,*args,**kwargs):
    #     return self.update(request,*args,**kwargs)
    # def delete(self,request,*args,**kwargs):
    #     return self.destroy(request,*args,**kwargs)

    # def get_object(self,pk):
    #     try:
    #         return Banner.objects.get(pk=pk)
    #     except:
    #         raise Http404
    # def get(self,request,pk,format=None):
    #     publisher = self.get_object(pk)
    #     s = serializers.BannerSerializer(publisher)
    #     return Response(s.data,status=status.HTTP_200_OK)
    # def pub(self,request,pk,format=None):
    #     publisher = self.get_object(pk)
    #     s = serializers.BannerSerializer(publisher,data=request.data)
    #     if s.is_valid():
    #         s.save()
    #         return Response(s.data)
    #     else:
    #         Response(s.errors,status=status.HTTP_400_BAD_REQUEST)
    # def delete(self,request,pk,format=None):
    #     publisher = self.get_object(pk)
    #     publisher.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)