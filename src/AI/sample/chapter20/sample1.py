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
    return y - x

# シグモイド関数の定義
def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-z))

# 正解配列
# ロジスティック回帰では0or1
T = np.array([1 if h(x,y) > 0 else 0 for x,y in X])

plt.scatter([xi for xi, yi in X if h(xi, yi) >= 0], [yi for xi, yi in X if h(xi, yi) >= 0], color="red")
plt.scatter([xi for xi, yi in X if h(xi, yi) < 0], [yi for xi, yi in X if h(xi, yi) < 0], color="blue")

# ここからが本番

# 学習率の初期値
eta = 0.1
n = 0

for i in np.arange(100):
    list  = np.arange(N)
    np.random.shuffle(list)

    for n in list:
        x_n, y_n = X[n]
        t_n = T[n]

        # 予測
        feature = phi(x_n, y_n)
        predict = sigmoid(np.inner(w, feature))
        # 値が不正解ならパラメータを更新する
        w -= eta * ( predict - t_n ) * feature

    # イテレーションごとに学習率を小さくする
    eta *= 0.9

print("w=", w)

#########################
###     図を書く準備
#########################

# 格子列生成用の配列を準備
seq = np.arange(-3,3, 0.01)
# x座標, y座標を格子文作成
xlist, ylist = np.meshgrid(seq, seq)
# 格子ごとの値を決定
zlist = np.array([sigmoid(np.inner(w, phi(xi, yi))) for xi, yi in zip(xlist, ylist) ])

# カラーマップの作成
# plt.pcolor(xlist, ylist, zlist, alpha=0.2, edgecolors="white")
plt.imshow(zlist, extent=[-3,3,-3,3], origin='lower', cmap=plt.cm.PiYG)

plt.show()
