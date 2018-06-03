import numpy as np
import matplotlib.pyplot as plt

x = np.array([1,2,3,4,5])
y = np.array([2,3,6,5,7])

plt.plot(x, y
         , linewidth=3          # 線の幅を設定
         , color="red"          # 線の色を設定
         , linestyle="dashed"   # 線の種類を設定(破線)
         , marker="o"           # マーカーの設定
         )

plt.show()