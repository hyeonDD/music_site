from platform import release
from django.db import models

# Create your models here.
class Music(models.Model):
    title = models.CharField(max_length=100) #제목
    singer = models.CharField(max_length=30) #가수
    album = models.CharField(max_length=30, null = True) #앨범
    genre = models.CharField(max_length=30, null = True) #장르
    lyrics = models.CharField(max_length=1000, null = True) #가사
    lyricists = models.CharField(max_length=100, null = True) #작사,작곡가들
    release_date = models.DateField(null = True) #발매일
    URL = models.CharField(max_length=100, null= True)

    def __str__(self):
        return self.title