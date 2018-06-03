import numpy
import AI.common.math as mymath
from matplotlib import pyplot, mlab

# 表の出る確率を1/2と定義
p = 0.5

# なぞ
L = []

# 試行回数の配列を準備
trial_count = (10, 20, 30, 40, 50)

# 色の配列を準備
colors = ["r", "g", "b", "c", "y"]

# 確率密度関数を取得
f = mymath.binomial(p)

for n in trial_count:
    # n回の試行でx回表が出る確率配列を追加
    L.append([f(n, x) for x in range(n)])

print("L:", L)

for prob, color in zip(L, colors):
    pyplot.plot(prob, color)

# grid線の表示
pyplot.grid()

# 横軸と縦軸のラベルの表示
pyplot.xlabel("trial count")
pyplot.ylabel("Probability")

# 判例の表示
pyplot.legend([str(n) for n in trial_count])

# グラフを表示する
pyplot.show()
