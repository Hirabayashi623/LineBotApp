# -*- coding:utf-8 -*-
import matplotlib.mlab as mlab
import matplotlib.pyplot as pyplot
import numpy as np

# 身長の疑似データを生成
# サンプル数を定義
sample = 100000

# 平均値と標準偏差を定義
ave, sigma = 170, 5
# 乱数によりデータを生成
data = np.random.normal(ave, sigma, sample)

# ヒストグラムの描画
n, bins, patches = pyplot.hist(data, normed=1, bins=30, alpha=0.75, align='mid')
# 戻り値の確認
print('n：', n)              # yの値の配列
print('bins：', bins)        # xの値の配列
print('patches：', patches)  # 謎

y = mlab.normpdf(bins, ave, sigma)
l = pyplot.plot(bins, y, 'r-', linewidth=1)

pyplot.title(r'$\mathrm{Histgram\ of\ Height:}\ \mu=%d,\ \sigma=%d$' % (ave, sigma))
pyplot.xlabel('Height')
pyplot.ylabel('Probability')

# グリッド表示（目盛線）
pyplot.grid(True)

pyplot.show()


