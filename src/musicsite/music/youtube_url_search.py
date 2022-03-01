import requests
from bs4 import BeautifulSoup

headers = {            
        'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
        }
URL = f'https://www.youtube.com/results?search_query=사랑비+김태우'
# URL = f'https://www.acmicpc.net/problem/1024'
html = requests.get(URL, headers=headers)
soup = BeautifulSoup(html.content, 'html.parser')
#thumbnail > yt-img-shadow
print(soup)
datas = soup.select('.style-scope ytd-thumbnail no-transition')
# datas = soup.select_one('#problem_title')
