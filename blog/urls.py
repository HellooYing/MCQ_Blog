from django.conf.urls import url
from . import views
urlpatterns = [

    url(r'^$',views.index,name='index'),
    url(r'^index_waterfall/',views.index_waterfall,name='index_waterfall'),
]