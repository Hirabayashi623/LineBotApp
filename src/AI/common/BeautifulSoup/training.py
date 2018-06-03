# -*- coding: utf-8 -*-
import urllib2

# 正規表現を用いるためのクラス
import re

from AI.common.BeautifulSoup.BeautifulSoup import BeautifulSoup

myHTML =  "<html>\
    <head>\
    <title>TITLE</title>\
    </head>\
    <body>\
    <h1 class='myClass' id='myID'>Head1</h1>\
    <h1>Head2</h1>\
    <dev></dev>\
    </body>\
    </html>"

# yahooのトップページにアクセスし、HTMLを取得する
results = urllib2.urlopen("https://www.yahoo.co.jp/")

# オブジェクトには参照値が格納されている？
# print results

# readメソッドで実際のHTML（XML）を参照
# print results.read()


# 引数にXMLを渡す
# soup = BeautifulSoup.BeautifulSoup(results.read())
soup = BeautifulSoup(myHTML)

# オブジェクトの参照でXMLが確認可能
print(soup)

# タグを取得する（ここではtitleタグ）
print(soup.title)
print(soup.title.string)

print(soup.h1)
print(soup.h1.string)

# 該当のタグを配列として取得できる
print(soup.findAll("h1"))
for w in soup.findAll("h1"):
    print(w.string)

# 正規表現を利用
print(soup.findAll(re.compile("^b")))

# タグの中に含まれる文字列を指定する
print(soup.findAll("h1", text=re.compile("e")))
print(soup.findAll("h1", text=re.compile("2")))

# selectメソッドでCSSのセレクタを使用できる  3.2.1では未実装？
# print soup.select("#myID")
# print soup.select(".myClass")



# XMLの出力
print(soup.prettify())

