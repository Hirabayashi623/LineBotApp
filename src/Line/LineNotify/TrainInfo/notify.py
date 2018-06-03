from bs4 import BeautifulSoup as bs
import urllib.request as ur
import src.Line.LineNotify.LineNotifyIF as ln

def Soup(url):
    req = ur.urlopen(url)
    html = bs(req,"html.parser")
    return html

url = 'http://www.jikokuhyo.co.jp/search/detail/line_is/kanto_chuokaisoku'
match = Soup(url).find(class_="corner_block_row_detail_d").string.replace('\n','')
text = '中央線快速の運行情報\r\n> ' + match

ln.notify(text)

url = 'http://www.jikokuhyo.co.jp/search/detail/line_is/kanto_shonanshinjuku'
match = Soup(url).find(class_="corner_block_row_detail_d").string.replace('\n','')
text = '湘南新宿ラインの運行情報\r\n> ' + match

ln.notify(text)

url = 'http://www.jikokuhyo.co.jp/search/detail/line_is/kanto_nambu'
match = Soup(url).find(class_="corner_block_row_detail_d").string.replace('\n','')
text = '南武線の運行情報\r\n> ' + match

ln.notify(text)