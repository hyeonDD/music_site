from django import forms
from music.models import Music

class MusicForm(forms.ModelForm):
    class Meta:
        model = Music
        # fields = ('title', 'singer', 'album', 'genre', 'lyrics'\
        #          ,'lyricists', 'release_date', 'URL')        
        # labels = {
        #     'title': '제목',
        #     'singer': '가수',
        #     'album': '앨범',
        #     'genre': '장르',
        #     'lyrics': '가사',
        #     'lyricists': '작사',
        #     'release_date': '발매일',
        #     'URL': 'Youtube URL',
        # }
        fields = ('title', 'singer')
        labels = {
            'title': '제목',
            'singer': '가수',
        }