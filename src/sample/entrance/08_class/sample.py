# -*- coding: utf-8 -*-
# クラスの定義
class MyClass:
    """A sinple example class"""

    # コンストラクタ
    def __init__(self):
        self.name = ""
        print("MyClass")

    # メソッド定義
    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name

    # デストラクタ
    def __del__(self):
        print("DEL")

    # インスタンスの文字列表現 ※JavaでいうtoString()メソッド
    def __str__(self):
        return "My name is " + self.name

#クラスのインスタンス化
a = MyClass()

# メソッドのコール
a.setName("Tanaka")
print(a.getName())
print(a)

# クラスの継承
class SubClass(MyClass):
    def __init__(self):
        # 親クラスの呼び出し super(親クラス,子クラス)
        super(MyClass,self).__init__()
        print("SubClass")

a = SubClass()
a.setName("Toru")
print(a)

# クラスの削除
del a
