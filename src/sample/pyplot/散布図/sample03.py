import numpy as np
import matplotlib.pyplot as plt

# 横軸の値を設定
x = np.random.rand(100)
# 縦軸の値を設定
y = np.random.rand(100)

# 散布図を生成
plt.scatter(
    x,                  # 値を設定①
    y,                  # 値を設定②
    s=600,              # サイズを変更
    c='pink',           # 色を変更
    alpha=0.5,          # 不透明度を設定
    linewidths="2" ,    # 線のサイズを設定
    edgecolors="red"    # 線の色を設定
    )

# グラフのタイトルを設定
plt.title("Sample Title")

# 横軸にコメントを記述
plt.xlabel("x axis")
# 縦軸にコメントを記述
plt.ylabel("y axis")
# グリッド線を記述
plt.grid(True)

# グラフの描画
plt.show()