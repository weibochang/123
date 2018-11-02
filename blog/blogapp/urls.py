from django.conf.urls import url, include
from blogapp import views
from blogapp.uploads import upload_image
from rest_framework.routers import DefaultRouter

publisherlist = views.PublisherList.as_view(
    {
        'get': 'list',
        'post': 'create'
    }
)

publisherdetail = views.PublisherList.as_view(
    {
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        # 'delete': 'destory'
    }
)

router = DefaultRouter()
router.register(r'publish',views.PublisherList)


urlpatterns = [
    url(r'^index/(\d*)', views.index, name='index'),
    url(r'^search/', views.search, name='search'),
    url(r'^list/(\d*)', views.list, name='list'),
    url(r'^show/(\d*)', views.show, name='show'),
    url(r'^blog_list/(?P<bid>\d*)', views.category_list, name='blog_list'),
    url(r'^comment/', views.comment, name='comment'),
    url(r'^tags_list/(?P<tid>\d*)', views.category_list, name='tags_list'),
    url(r'^a/', views.a),
    url(r'^ifcom/', views.ifcom),
    url(r'^upload/(?P<dir_name>[^/]+)$', upload_image, name='upload_image'),
    url(r'^write/', views.write, name='write'),
    # url(r'^publisher/$', views.PublisherList.as_view()),
    # url(r'^publisher/(?P<pk>[0-9]+)/', views.PublisherDetail.as_view( )),
    url(r'^publisher/$', publisherlist),
    url(r'^publisher/(?P<pk>[0-9]+)/', publisherdetail),
    url(r'^',include(router.urls))

]
