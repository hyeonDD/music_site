# from django.shortcuts import render
from django.shortcuts import redirect, render, get_object_or_404
from .forms import MusicForm
from .models import Music
# Create your views here.
def index(request):
    """
    음악 목록 출력
    """
    play_list = Music.objects.order_by('-release_date')
    context = {'play_list': play_list}
    return render(request, 'play_list.html', context)

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
            form.save()
            print("데이터 저장됨")
            return redirect('music:index')
    else:
        print("데이터 저장x")
        form = MusicForm() # request.method가 'GET'인 경우 호출
    context = {'form': form}
    return render(request, 'music_form.html', context)