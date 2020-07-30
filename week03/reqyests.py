# # import requests  # requests 라이브러리 설치 필요
# #
# # # requests 를 사용해 요청(Request)하기
# # response_data = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')
# #
# # # 응답(response) 데이터인 json을 쉽게 접근할 수 있게 만들어 city_air 에 담고
# #
# # city_air = response_data.json()
# #
# # # 값을 출력
# # print(city_air['RealtimeCityAir']['row'][0]['NO2'])
#
#
# import requests
#
# response_data = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')
#
# city_air = response_data.json()
#
#
# gu_info = city_air['RealtimeCityAir']['row']
#
# for gu_info in gu_infos
#     print(gu_info[''])

import requests
from bs4 import BeautifulSoup

# 타겟 URL을 읽어서 HTML를 받아오고,

data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200716')
soup = BeautifulSoup(data.text, 'html.parser')
trs = soup.select('#old_content > table > tbody > tr')
for tr in trs:
    a_tag = tr.select_one('.title a')
    if a_tag is not None:
        title = a_tag.text
        rank = tr.select_one('.ac img')['alt']
        point = tr.select_one('.point').text
        print(rank, title, point)

