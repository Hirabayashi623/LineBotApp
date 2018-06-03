import numpy as np
import matplotlib.pyplot as plt

# 横軸の値を設定
x = np.random.rand(100)
# 縦軸の値を設定
y = np.random.rand(100)

# 散布図を生成
plt.scatter(x, y)

# グラフの描画
plt.show()