# -*- coding: utf-8 -*-

#################
#  リスト list  #
#################
# リストの記述方法
a = [10, 20, 30]; print(a)

# 改行して記述することも可能
a = [
    10,
    20,
    30
    ]; print(a)

# 異なる型のリストを作ることもできる
a = ["a", 100]; print(a)

# リストへのアクセス
a = [10,20,30]
for n in a:
    print(n)

# n番目の要素を参照
a = ["A","B","C","D"]
print(a[0])
print(a[2])

print(a[2:4])
print(a[1:])
print(a[:2])

# 全要素を要素を1つ飛ばしで参照
print(a[::2])

# 配列の結合
print([1,2,3] + [4,5,6])

#リストのリスト
myList = [[1,2],[3,4],[5,6]]

for my in myList:
    print(my)

#################
#  タプル tuple #
#################
# 変更できないリスト
a = (1, 2, 3, 4, 5); print(a)

#a[3] = 2  #エラーになる

# タプル⇒りすとに変換
print(list((1,2,3,4,5)))
print(tuple([1,2,3,4,5]))

###################
#  ディクショナリ #
###################
# javaでいうMapクラス
d = {"apple":30, "banana":40, "peach":50}

# 各要素へのアクセス
print(d["apple"])
print(d["banana"])
print(d["peach"])

# すべての要素を参照
for k,v in d.items():
    print(k,v)

for k in d.keys():
    print(k)

for v in d.values():
    print(v)

#リスト関数
# map リストの各要素に対して処理を行い、処理結果を返す
a = [1,2,3]
def double(x):
    return x * 2
print(map(double, a))
print(map(lambda x : x * 2, a))
print([x * 2 for x in a])

# filter 各要素に対して処理を行い、処理結果が真となる要素のみを取り出す
a = [1,2,3]

def isodd(x):
    return x % 2
print(filter(isodd, a))
print(filter(lambda x: x % 2, a))
print([x for x in a if x % 2])

# set 重複のないリストを扱う
a = set(["red","blue", "green"])
b = set(["green", "yellow", "white"])

print(a)
print(b)
print(a - b)
print(a | b)
print(a & b)
print(a ^ b)






