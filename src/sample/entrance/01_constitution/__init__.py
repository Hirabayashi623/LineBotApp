# Hello worldを出力する
print("Hello world !")

# セミコロンで区切ることで1行に複数コマンドを記載できる
a = 5; b = 3; c = a + b

print(c)

# 1行を複数行に分けて記述したい場合は\で区切る
total = 123 \
    + 456 \
    + 789

print(total)

# ブロックは{}ではなくインデントで表す

d = 3
if d == 5:
    print("AAA")    #ifの対象
    print("BBB")    #ifの対象
print("CCC")    #ifの対象外

