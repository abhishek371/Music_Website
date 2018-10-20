from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$',views.index,name='index'),#music home page

    #/music/712/  712 is album id

    url(r'^(?P<album_id>[0-9]+)/$',views.detail,name='detail'),


]