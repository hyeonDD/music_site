import requests
from bs4 import BeautifulSoup
import functools
import operator

STATIC_THUMBNAIL_PATH = 'src/musicsite/music/static/thumbnail/'

class MusicInfo:
    def __init__(self, URL='') -> None:
        self.headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}        
        # URL = f'https://www.melon.com/search/total/index.htm?q=사랑비김태우'        
        # URL = f'https://www.melon.com/search/total/index.htm?q=허각 바다'        
        html = requests.get(URL, headers=self.headers)
        self.soup = BeautifulSoup(html.content, 'html.parser')

    def parsing(self, selector):                
        datas = self.soup.select_one(f'{selector}')
        return datas
    
    def download_thumbnail(self, url, filename):
        thumbnail_url = str(url.parsing('.thumb > .image_typeAll'))

        benchmark = thumbnail_url.rindex('https://cdnimg.melon.co.kr/') # 썸네일 url 지점 찾기
        benchmark2 = thumbnail_url.rindex("optimize")
        thumbnail_url = thumbnail_url[benchmark:benchmark2+8] # 지점을 기준으로 짜르기        
   
        with open(STATIC_THUMBNAIL_PATH+filename+'.jpg', 'wb') as file:
            res = requests.get(thumbnail_url, headers=self.headers)
            img_data = res.content
            file.write(img_data)

def musicInfoRun(search):
    get_detail_URL = MusicInfo(f'https://www.melon.com/search/song/index.htm?q={search}') #클래스 이름으로 검색
    tmp = str(get_detail_URL.parsing('.btn_icon_detail')) # str형으로 변환하기위해 잠시저장
    benchmark = tmp.rindex('goSongDetail') # goSongDetail 지점 찾기
    benchmark2 = tmp.rindex("');")
    tmp = tmp[benchmark+14:benchmark2] # 지점을 기준으로 짜름 (SongID가 짤려서나옴)    

    get_detail_URL = MusicInfo('https://www.melon.com/song/detail.htm?songId='+tmp)    
    music_title = get_detail_URL.parsing('.song_name').text.split()[1:] # 노래 이름
    music_title = ''.join(music_title)

    music_singer = get_detail_URL.parsing('.artist').text.strip() # 노래 가수    
    _, music_album, _ , release_date, _, music_genre, *_ = get_detail_URL.parsing('.meta').text.strip().split('\n') # 앨범, 발매일, 장르
    try :
        music_lyrics = get_detail_URL.parsing('.lyric').text.strip() # 노래 가사
    except AttributeError:
        print("노래가사 준비중")
        music_lyrics = '- 노래가사 준비중 -'

    music_lyricists = get_detail_URL.soup.select('.entry > .ellipsis') # 작사/작곡만 여러개 조회를 위해 select 사용
    li_music_lyricists = [i.text.strip() for i in music_lyricists]
    music_lyricists_detail = get_detail_URL.soup.select('.meta span.type') # 작사/작곡만 여러개 조회를 위해 select 사용
    li_music_lyricists_detail = [i.text.strip() for i in music_lyricists_detail]
    try :
        music_lyricists_detail = str(functools.reduce(operator.add,list(zip(li_music_lyricists_detail,li_music_lyricists)))) # 작사/작곡 묶기
    except TypeError:
        print("작사/작곡 준비중")
        music_lyricists_detail= '- 작사/작곡 준비중 -'
    
    get_detail_URL.download_thumbnail(get_detail_URL, music_title) # 썸네일 이미지 다운로드

    return music_title, music_singer, music_album, release_date.replace('.','-'), music_genre, music_lyrics, music_lyricists_detail
    

if __name__ == '__main__':  
    """ # a, *_ = musicInfoRun('러브블러썸 케이윌')
    a, *_ = musicInfoRun('사랑비 김태우')
    
    # _,_,_,a,*_ = musicInfoRun('러브119 케이윌')
    print(a)
    print(type(a))

    # musicInfoRun('러브119 케이윌') """
    musicInfoRun('러브블러썸 케이윌')