# -*- coding: utf-8 -*-
# if文
from test.test_decimal import file
num = 1
if num > 10:
    print("BIG")
elif num == 10:
    print("NOMAL")
else:
    print("SMALL")

# whle文
n = 0
while n < 10:
    print(n)
    n += 1
else:
    print("END")

# 各要素に対して処理を繰り返す
myStr = ""
for n in [1,2,3]:
    myStr += str(n) + " "
print(myStr)

myStr = ""
for k in {"one":1, "two":2, "three":3}:
    myStr += k + " "
print(myStr)

myStr = ""
for c in "123":
    myStr += c + " "
print(myStr)

myStr = ""
for line in open("sample.txt"):
    myStr += line
print(myStr)

n = 0
for x in range(10):
    n += 1
else:
    print(n)


# 例外処理
str = "ABC"
try:
    c = str[5]
except IndexError:
    print("IndexError")
finally:
    print("Finally")

# 例外を自作、例外を意図的に発生される
class MyException(Exception):
    def __init__(self, file, lineno):
        self.file = file
        self.lineno = lineno

try:
    raise MyException("sample.txt", 3)
except MyException as e:
    print("MyException")
    print(e.file)
    print(e.lineno)


# with構文　withを用いるとwithブロック終了時に終了処理が自動的に呼ばれる

f = open("sample.txt")
print(f.read())
f.close()

with open("sample.txt") as f:
    print(f.read())

f = open("sample.txt")
with f:
    print(f.read())

# assert文　テストの際に値が期待通りに設定されているか確認するための仕組み
try:
    a = 5
    assert a == 3
except AssertionError:
    print("想定と異なります")

# del文　オブジェクトの削除
a = 1
b = 2
c = 3
del a, b, c

# print文　標準出力
print("AAA") ,  # 改行なし出力
print("BBB")

# フォーマット指定 formatの引数が順に0,1,2...に差し込まれるイメージ
print("My name is {0:s}" .format("Ryo"))
print("{0:d}".format(5))
print("{0:+d}".format(5))
print("{0:07.2f}".format(5))

#exec文　引数の文字列をPythonのスクリプトとして実行する
exec("print('Hello world!')")



