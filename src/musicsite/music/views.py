# from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
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