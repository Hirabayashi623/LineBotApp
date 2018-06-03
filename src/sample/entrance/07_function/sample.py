# 関数の定義
def add(x, y):
    print(x + y)
add(3,5)

# キーワード付き引数を指定することも可能
def repeat_msg(msg, repeat=3):
    for i in range(repeat):
        print(msg, end="")
    print("")
repeat_msg("Hello")
repeat_msg("Yahoo",repeat=2)

# 引数いろいろ
def func(a1, a2, *args, **params):
    print(a1)
    print(a2)
    print(args)
    print(params)

func("A","B","C","D",k1="k1",k2="k2",k3="k3")

# 複数の値を返却することも可能
def func01():
    return 3, "ABC"
n,s = func01(); print(n, s)

# グローバル変数



# ラムダ式
func03 = lambda x, y: x + y; print(func03(3,5))

# イテレータ
class MyClass01:
    def __init__(self):
        self.data = (1,2,3,4,5)
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index < len(self.data):
            self.index += 1
            return self.data[self.index -1]
        else:
            raise StopIteration

for n in MyClass01():
    print(n,end="")
print("")


# ジェネレータ
def readfile(f):
    for line in f:
        yield line.rstrip()

f = open("sample.txt")
for line in readfile(f):
    if(line == "__END__"):
        break
    print(line)
f.close()

# デコレータ
def mydecorater(func):
    def wrapper():
        print("###    START   ###")
        func()
        print("###     END    ###")
    return wrapper

@mydecorater
def hello():
    print("hello")

hello()




