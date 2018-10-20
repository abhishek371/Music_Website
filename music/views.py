from django.shortcuts import render
from .models import Album
from django.http import Http404


def index(request):
    all_albums = Album.objects.all()#getting all the album
    return render(request, 'music/index.html',{'all_albums' :all_albums})

def detail(request,album_id):
    try:
        album= Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("Album does not Exist")
    return render(request,'music/detail.html',{'album' :album})

