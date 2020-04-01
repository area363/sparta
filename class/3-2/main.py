import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get("https://www.imdb.com/search/title/?count=100&groups=top_1000&sort=user_rating",headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

# select를 이용해서, tr들을 불러오기
players = soup.select('#main')
print(players)
# movies (tr들) 의 반복문을 돌리기
rank = 1
for player in players:
    # movie 안에 a 가 있으면,
    a_tag = movie.select_one('a')
    print(a_tag)
    # if a_tag is not None:
    #     title = a_tag.text
    #     star = movie.select_one('td.point').text
    #     print(rank,title,star)
    #     rank += 1