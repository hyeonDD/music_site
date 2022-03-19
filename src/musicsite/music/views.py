# from django.shortcuts import render
from django.shortcuts import redirect, render, get_object_or_404
from .forms import MusicForm
from .models import Music
from .music_info import MusicInfo, music_info_run
from .downloader import downloader_run
# Create your views here.
def index(request):
    """
    음악 목록 출력
    """
    music_list = Music.objects.order_by('-release_date')
    context = {'music_list': music_list}
    return render(request, 'music_list.html', context)

def detail(request, music_id):
    """
    음악 내용 출력
    """

    music = get_object_or_404(Music, pk=music_id)
    context = {'music': music}
    return render(request, 'music_detail.html', context)

def register_music(request):
    """
    음악 등록
    """

    if request.method == "POST":
        form = MusicForm(request.POST)
        if form.is_valid():
            #db에 넣기
            music_title, music_singer, music_album, release_date, music_genre, music_lyrics, music_lyricists_detail = music_info_run(form.cleaned_data['title']+form.cleaned_data['singer'])
            #음악 다운로드
            url = downloader_run(form.cleaned_data['title']+form.cleaned_data['singer'])
            print(form.cleaned_data['title'])
            print(form.cleaned_data['singer'])
            Music.objects.create(title=music_title,\
                                         singer=music_singer,\
                                         album=music_album,\
                                         genre=music_genre,\
                                         lyrics=music_lyrics,\
                                         lyricists=music_lyricists_detail,\
                                         release_date=release_date,\
                                         URL=url,
                                        )
            print("데이터 저장됨")
            return redirect('music:index')
    else:
        print("데이터 저장x")
        form = MusicForm() # request.method가 'GET'인 경우 호출
    context = {'form': form}
    return render(request, 'music_form.html', context)