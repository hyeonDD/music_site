from django import forms
from music.models import Music

class MusicForm(forms.ModelForm):
    class Meta:
        model = Music
        fields = ('title', 'singer', 'album', 'genre', 'lyrics'\
                 ,'lyricists', 'release_date', 'URL')
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'singer' : forms.TextInput(attrs={'class':'form-control'}),
        }