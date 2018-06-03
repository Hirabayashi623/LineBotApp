import numpy as np
import matplotlib.pyplot as plt

# f(x) = sgn+(ωΦ(x))
# ω' = ω+tΦ(x)

# データ点を特徴ベクトルへ変換
def phi(x, y):
    return np.array([x, y, 1])

# パラメータ
w = np.zeros(3)  # [0,0,0]

# データの個数
N = 100

# データ点
X = np.random.randn(N, 2)

# 適当な分離平面
def h(x, y):
    w0 = np.array([1, -1, 0])
    return np.dot(w0, phi(x, y))

# 正解配列
T = np.array([1 if h(x,y) >= 0 else -1 for x,y in X])

plt.scatter([xi for xi, yi in X if h(xi, yi) >= 0], [yi for xi, yi in X if h(xi, yi) >= 0], color="red")
plt.scatter([xi for xi, yi in X if h(xi, yi) < 0], [yi for xi, yi in X if h(xi, yi) < 0], color="blue")

# ここからが本番
n = 0
while n < 1000:
    list  = np.arange(N)
    np.random.shuffle(list)

    misses = 0
    for n in list:
        x_n, y_n = X[n]
        t_n = T[n]

        # 予測
        predict = np.sign((w * phi(x_n, y_n)).sum())
        # 値が不正解ならパラメータを更新する
        if predict != t_n:
            w += t_n * phi(x_n, y_n)
            misses += 1

    if misses == 0:
        break
    n += 1

print("w=", w, ", n=", n)

#########################
###     図を書く準備
#########################

# 格子列生成用の配列を準備
seq = np.arange(-3,3, 0.01)
# x座標, y座標を格子文作成
xlist, ylist = np.meshgrid(seq, seq)
# 格子ごとの値を決定
zlist = np.array([np.sign(np.dot(w, phi(xi, yi))) for xi, yi in zip(xlist, ylist) ])

# カラーマップの作成
plt.pcolor(xlist, ylist, zlist, alpha=0.2, edgecolors="white")

plt.show()
