import requests
from bs4 import BeautifulSoup

# URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200309',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
soup = BeautifulSoup(data.text, 'html.parser')


# select를 이용해서, tr들을 불러오기
songs = soup.select('#body-content >div.newest-list> div.music-list-wrap > table.list-wrap > tbody > tr')
# songs (tr들) 의 반복문을 돌리기
rank = 1
for song in songs:
    # song 안에 a.title 있으면,
    a_tag = song.select_one('td.info > a.title')
    if a_tag is not None:
        title = a_tag.text.strip()
        artist = song.select_one('td.info > a.artist').text
        print(rank,title,"|",artist)
        rank += 1