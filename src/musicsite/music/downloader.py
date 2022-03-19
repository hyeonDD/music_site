import os
import youtube_dl
from youtube_search import YoutubeSearch
import json
import os

VIDEO_DOWNLOAD_PATH = f"{os.path.dirname(os.path.realpath(__file__))}/static/audio"
print(VIDEO_DOWNLOAD_PATH)

def search_url(search):
    results = YoutubeSearch(search, max_results=10).to_json()
    result = json.loads(results) # 결과json을 dict 형으로 바꿈
    result = result["videos"][0]["url_suffix"] # 결과로 /watch?v= ??? 이나옴
    return result

def download_video_and_subtitle(video_url, file_name):
    if os.path.isfile(f"{VIDEO_DOWNLOAD_PATH}/{file_name}.mp3"):
        print("파일이 이미 존재합니다")
        return 0

    download_path = os.path.join(VIDEO_DOWNLOAD_PATH, file_name+'.%(ext)s')

    # for video_url in youtube_video:

    # youtube_dl options
    ydl_opts = {
        'format': 'bestaudio/best',  # 가장 좋은 화질로 선택(화질을 선택하여 다운로드 가능)
        'outtmpl': download_path, # 다운로드 경로 설정
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    try:
        print('video_url',video_url)
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
    except Exception as e:
        print('error', e)

def downloader_run(search):
    url = search_url(search)
    download_video_and_subtitle("https://www.youtube.com"+url,url[9:])
    return url[9:]

if __name__ == '__main__':

    # url = search_url('사랑비 김태우')
    # print(url)
    # download_video_and_subtitle("https://www.youtube.com"+url,url[9:])
    # print('Complete download!')
    downloader_run('사랑비 김태우')