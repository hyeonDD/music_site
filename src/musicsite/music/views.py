# from django.shortcuts import render
from django.shortcuts import render
from .models import Music
# Create your views here.
def index(request):
    """
    음악 목록 출력
    """
    play_list = Music.objects.order_by('-release_date')
    context = {'play_list': play_list}
    return render(request, 'play_list.html', context)