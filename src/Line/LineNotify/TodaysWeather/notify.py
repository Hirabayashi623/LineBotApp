from bs4 import BeautifulSoup as bs
from urllib import request as req
import src.Line.LineNotify.LineNotifyIF as ln

url = 'https://weather.yahoo.co.jp/weather/jp/13/4410.html'

request = req.urlopen(url)

soup = bs(request, "html.parser")

message = soup.find(class_='forecastCity').find("img").get('alt')

ln.notify('今日の天気：' + message)