import numpy as np
import matplotlib.pyplot as plt

x = np.random.randint(0,100,100)
y = np.random.randint(0,100,100)

def f(x, y):
    return y - x

def judge(z):
    ans = 1
    if z < 0:
        ans = -1
    return ans


# print(x)
# print(y)

t = np.array([judge(zi) for zi in f(x,y)])
print(t)

plt.scatter(x, y, t, color="red")
plt.scatter(x, y, -t, color="blue")

# パーセプトロン開始
# f(x, y) = ax + by + c = 0

# 初期値の設定
a = 0
b = 1
c = 0

def fi(x, y):
#     print("a=", a, ", b=", b, ", c=", c)
    return b * y - a * x - c

n = 0
while(n < 100):
    for i in np.arange(0, t.size):
        ti = b * y[i] - a * x[i] - c
        if judge(ti) != t[i]:
            a = a + x[i] * t[i]
            b = b + y[i] * t[i]
            c = c + t[i]
    n = n + 1

print("a=", a, ", b=", b, ", c=", c)

x4plot = np.arange(0, 100, 0.1)
y4plot = np.array([- a / b * xi - c / b for xi in x4plot])

plt.plot(x4plot, y4plot)
plt.show()