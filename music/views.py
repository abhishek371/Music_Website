from django.shortcuts import render,get_object_or_404
from .models import Album



def index(request):
    all_albums = Album.objects.all()#getting all the album
    return render(request, 'music/index.html',{'all_albums' :all_albums})

def detail(request,album_id):
    '''try:
        album= Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("Album does not Exist")'''
    album = get_object_or_404(Album,pk=album_id)
    return render(request,'music/detail.html',{'album' :album})


def favorite(request,album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        selected_Song = album.song_set.get(pk=request.POST['song'])
    except (KeyError,Song.DoesNotExist):
        return render(request, 'music/detail.html', {'album': album,'error_message':"You did not elect a valid song"})
    else:
        selected_Song.is_favorite = True
        selected_Song.save()
        return render(request,'music/detail.html',{'album':album})


