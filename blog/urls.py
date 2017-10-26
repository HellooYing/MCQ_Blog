from django.conf.urls import url
from . import views
from django.views.generic.base import RedirectView

urlpatterns = [
    
    url(r'^$',views.index,name='index'),
    url(r'^index_waterfall/',views.index_waterfall,name='index_waterfall'),
    url(r'^favicon.ico$',RedirectView.as_view(url=r'static/favicon.ico')),
]