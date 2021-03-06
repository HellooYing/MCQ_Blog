from django.conf.urls import url
from . import views
from django.views.generic.base import RedirectView
app_name = 'blog'

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^phone/$',views.phone,name='phone'),
    url(r'^categories/$',views.categories,name='categories'),
    url(r'^index_waterfall/',views.index_waterfall,name='index_waterfall'),
    url(r'^favicon.ico$',RedirectView.as_view(url=r'static/favicon.ico')),
    url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    url(r'^comm$', views.comm, name='comm'),
    url(r'^change_img$', views.change_img, name='change_img'),
    url(r'^zan$', views.zan, name='zan'),
    url(r'^change/$', views.change, name='change'),
    url(r'^compiler/$', views.compiler, name='compiler'),
    url(r'^compiler_get/$', views.compiler_get, name='compiler_get'),
    url(r'^touzi/$', views.touzi, name='touzi'),
]