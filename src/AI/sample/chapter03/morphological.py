# -*- coding: utf-8 -*-
from urllib import request, parse

from bs4 import BeautifulSoup
# from AI.common.log import myLog
# logger = myLog.getLogger()

appid_ = 'dj00aiZpPTJmejY0d3Y5VGhBMyZzPWNvbnN1bWVyc2VjcmV0Jng9NzE-'
pageurl = "http://jlp.yahooapis.jp/MAService/V1/parse";

# Yahoo!形態素解析の結果をリストで返します。
# 引数に=がつく場合は指定がない場合のデフォルト値の設定
def split(sentence, appid=appid_, results="ma", filter="1|2|3|4|5|9|10"):

    # 文字列のエンコードの設定（文字コードの変換？）
    sentence = sentence.encode("utf-8")

    # リクエストのパラメータを生成する key1:value1 → key1=value1&key2=value2....のイメージ
    params = parse.urlencode({'appid':appid, 'results':results, 'filter':filter,'sentence':sentence}).encode('utf_8')

    # URLを発行し、レスポンスを取得する
    results = request.urlopen(pageurl, params)

    # BeautifulSoupはXML解析用のライブラリ
    # 読み込むXMLを指定する
    soup = BeautifulSoup(results.read(),"html.parser")

    # XMLのma_result>word_list>serfaceタグの内容をリストにして返却？
    return [w.surface.string for w in soup.ma_result.word_list]

#######################################
###    参考情報
#######################################
"""
filter で解析する品詞の種類を指定
    1 → 形容詞
    2 → 形容動詞
    3 → 感動詞
    4 → 副詞
    5 → 連体詞
    6 → 接続詞
    7 → 接頭辞
    8 → 接尾辞
    9 → 名詞
    10 → 動詞
    11 → 助詞
    12 → 助動詞
    13 → 特殊（句読点，カッコ，記号など）

"""