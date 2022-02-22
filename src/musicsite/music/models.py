from platform import release
from django.db import models

# Create your models here.
class Music(models.Model):
    title = models.CharField(max_length=100) #제목
    singer = models.CharField(max_length=30) #가수
    album = models.CharField(max_length=30) #앨범
    genre = models.CharField(max_length=30) #장르
    lyrics = models.CharField(max_length=1000) #가사
    lyricists = models.CharField(max_length=100) #작사,작곡가들
    release_date = models.DateField() #발매일