from bs4 import BeautifulSoup as bs
import urllib.request as ur
import requests
from urllib import request as req

# 発行したトークンを指定
line_notify_token = 'KjRlCxnU73OC8bv8xo5bke8WHcbQrvsShuRX2dVVQad'

# LINE通知APIのパスを指定
line_notify_api = 'https://notify-api.line.me/api/notify'

def notify(message):
    payload = {'message': message}
    headers = {'Authorization': 'Bearer ' + line_notify_token}
    requests.post(line_notify_api, data=payload, headers=headers)

def Soup(url):
    req = ur.urlopen(url)
    html = bs(req,"html.parser")
    return html

url = 'http://www.jikokuhyo.co.jp/search/detail/line_is/kanto_chuokaisoku'
match = Soup(url).find(class_="corner_block_row_detail_d").string.replace('\n','')
text = '中央線快速の運行情報\r\n> ' + match

notify(text)

url = 'http://www.jikokuhyo.co.jp/search/detail/line_is/kanto_shonanshinjuku'
match = Soup(url).find(class_="corner_block_row_detail_d").string.replace('\n','')
text = '湘南新宿ラインの運行情報\r\n> ' + match

notify(text)

url = 'http://www.jikokuhyo.co.jp/search/detail/line_is/kanto_nambu'
match = Soup(url).find(class_="corner_block_row_detail_d").string.replace('\n','')
text = '南武線の運行情報\r\n> ' + match

notify(text)

url = 'https://weather.yahoo.co.jp/weather/jp/13/4410.html'

request = req.urlopen(url)

soup = bs(request, "html.parser")

message = soup.find(class_='forecastCity').find("img").get('alt')

notify('今日の天気：' + message)