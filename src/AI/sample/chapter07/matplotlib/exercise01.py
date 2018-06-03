from matplotlib import pyplot
import numpy

# 通常のサイコロの出る目の確率分布を描写する

# サンプルの生成
data = numpy.random.randint(1, 7, 100000)
# print("data: ", data)

pyplot.hist(data, align="left", bins=6)
# pyplot.xlim([0,8])

pyplot.show()
