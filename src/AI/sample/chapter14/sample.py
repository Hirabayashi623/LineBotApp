import numpy as np
from matplotlib import pyplot as plt

# ガウス関数を定義(12次元)
def phi(x):
    # ガウス基底「幅」
    s = 0.1
    # 第一引数で指定した配列に第2引数で指定した値を格納して返却する
    return np.append(1, np.exp(-(x - np.arange(0, 1 + s, s)) ** 2 / (2 * s * s)))


# データを生成
x0 = np.array([0.02, 0.12, 0.19, 0.27, 0.42, 0.51, 0.64, 0.84, 0.88, 0.99])
t0 = np.array([0.05, 0.87, 0.94, 0.92, 0.54, -0.11, -0.78, -0.79, -0.89, -0.04])

# Φを取得
PHI = np.array([phi(xi) for xi in x0])

# Φw = t の連立方程式を解く
#     (Φ.T)Φw = (Φ.T)t
w = np.linalg.solve(np.dot(PHI.T, PHI), np.dot(PHI.T, t0))

# 元のデータから散布図を生成
plt.plot(x0, t0,'o')

# 求めた関数からグラフを作成
x1 = np.arange(0, 1.1, 0.01)
t1 = [np.dot(w, phi(xi)) for xi in x1]
# 普通の線形回帰（青）
plt.plot(x1, t1, color="b")

# α：大きいほど分散が小さくなる→wが0に近い値だという事前知識が強くなる
#     →wを0に近い値にしようとする力が強いため、過学習を抑えられる
#     →が、しんの解にたどり着くまでに多くのデータを必要とする
#    逆にαが小さいとwを押さえつける力が弱くなる
#    →特にα=0のときは普通の線形回帰と一致する
alpha = 0.1
#β：「精度」と呼ばれ、ノイズがどれだけ含まれても良いかを表す量
#     大きいとブレは少なく、小さいとブレが大きくても許される
beta = 9.0

sigma_N = np.linalg.inv(alpha * np.identity(PHI.shape[1]) + beta * np.dot(PHI.T, PHI))
mu_N = beta * np.dot(sigma_N, np.dot(PHI.T, t0))

# ベイズ線形回帰グラフ（赤）
plt.plot(x1, [np.dot(mu_N, phi(x)) for x in x1], 'r')

plt.show()