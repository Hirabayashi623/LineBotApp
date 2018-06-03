# -*- coding: utf-8 -*-
import math

#yahoo!形態素解析
from src.AI.sample.chapter03 import morphological
from src.AI.common.log import myLog

def getwords(doc):

    # 大文字を小文字に変更して配列に格納
    words = [s.lower() for s in morphological.split(doc)]

    # 配列をタプルに変更して返却
    return tuple(w for w in words)





####################################################
###    ナイーブベイズのアルゴリズムのおさらい    ###
####################################################
"""
今回の目標は、文章が与えられたときに、カテゴリに属する確率を求める
→P(カテゴリ| 文章)

求めた確率を元に、一番高い確率のカテゴリを文章のカテゴリとする

P(カテゴリ| 文章) * P(文章) = P(文章| カテゴリ) * P(カテゴリ)
→ P(カテゴリ| 文章) = P(文章| カテゴリ) * P(カテゴリ) / P(文章)
※P(文章)=ある文書が与えられる確率　→固定

P(カテゴリ)=カテゴリが生起する確率 →カテゴリが与えられた件数/総文書数　とする
※訓練フェーズで登録回数を保存しておく

P(文章|カテゴリ)＝カテゴリが与えられたときの文書の生起確率
→単語の共起性（ある単語が出現したときに別の単語も現れやすい）を無視する
→文書の確立を単語の確立の積として単純化する（ナイーブ：単純な）
→P(文書|カテゴリ)＝P(単語1|カテゴリ)* P(単語2|カテゴリ) * P(単語3|カテゴリ) ...

P(単語｜カテゴリ)＝ある単語がカテゴリに含まれる確率
 → あるカテゴリに単語が出現した回数 / カテゴリに出現した全単語数
※訓練フェーズで出現した単語があるカテゴリに分類される回数を保存しておく

"""


class NaiveBayes:
    # コンストラクタ
    def __init__(self):
        # 空のセット（重複のないリスト）を準備する →出現した単語を保存しておく
        self.vocabularies = set() # 単語の集合

        # 単語の生起数を登録するためのディクショナリを準備 →カテゴリ：d（単語：生起数）で登録
        self.wordcount = {}       # {category : { words : n, ...}}

        # カテゴリの生起数を登録するためのディクショナリを準備 →カテゴリ：生起数で登録
        self.catcount = {}        # {category : n}

    def wordcountup(self, word, cat):
        # 単語の生起数にカテゴリを追加 ※setdefaultは、なければ追加、あればなにもしない
        self.wordcount.setdefault(cat, {})

        # カテゴリに単語と初期値0を追加
        self.wordcount[cat].setdefault(word, 0)

        # カテゴリ内の単語の生起率をインクリメント
        self.wordcount[cat][word] += 1

        # 単語のセットに単語を追加する
        self.vocabularies.add(word)

    def catcountup(self, cat):
        # カテゴリを追加
        self.catcount.setdefault(cat, 0)

        # カテゴリの生起数をインクリメント
        self.catcount[cat] += 1


    # 訓練フェーズの実装
    def train(self, doc, cat):
        # 文書から単語の一覧を取得する
        word = getwords(doc)

        # 取得した単語それぞれについてカテゴリごと内の単語の生起数をインクリメント
        for w in word:
            self.wordcountup(w, cat)

        # カテゴリの生起数をインクリメント
        self.catcountup(cat)

    # 推測フェーズの実装
    # カテゴリの生起率を求める
    def priorprob(self, cat):
        return float(self.catcount[cat]) / sum(self.catcount.values())

    # カテゴリ内の単語の出現数の取得関数
    def incategory(self, word, cat):
        if word in self.wordcount[cat]:
            return float(self.wordcount[cat][word])
        return 0.0

    # 推測フェーズの実装
    # カテゴリ内の単語の生起率を求める P(単語｜カテゴリ)
    def wordprob(self, word, cat):
        return (self.incategory(word, cat) + 1.0) / (sum(self.wordcount[cat].values()) + len(self.vocabularies) * 1.0)

    # 推測フェーズの実装
    # 確率値の対数の算出 P(カテゴリ) * Π P(単語｜カテゴリ) = P(カテゴリ) * P(文書｜文書)
    # 単純に掛け算をしていくと値が小さくなってしまうため、対数で計算 ※大小関係が重要なため
    def score(self, word, cat):
        score = math.log(self.priorprob(cat))
        for w in word:
            score += math.log(self.wordprob(w, cat))
        return score

    # 推測フェーズの実装
    # カテゴリの推測
    def classifier(self, doc):
        best = None
        upd_flg = 0
        max = 0
        words = getwords(doc)

        #カテゴリごとに確率の対数を求める
        for cat in self.catcount.keys():
            prob = self.score(words, cat)

            if upd_flg == 0:
                upd_flg = 1
                max = prob
                best = cat
            elif prob > max:
                max = prob
                best = cat
        return best

    def show(self):
        print(self.wordcount)
        print(self.catcount)


##########################
###    スムージング    ###
##########################
"""
訓練フェーズで出現しなかった単語について、
P(その単語|カテゴリ)＝0となってしまう　※ゼロ頻度問題・スパースネスの問題
→確率が0にならないように補正をかける（スムージング）する必要がある

今回は加算スムージング法で実装    ※精度が悪い
→精度の高いものに「線形補完法」や「ヘルドアウト補完法」がある
"""