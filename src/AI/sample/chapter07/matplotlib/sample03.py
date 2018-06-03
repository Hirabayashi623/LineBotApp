from AI.common import math as mymath
from matplotlib import pyplot, mlab

N = 8
L = []

# 1試合の平均点数を定義
score_mean = 0.8

f = mymath.poisson(score_mean)

L.append([f(x) for x in range(N+1)])


pyplot.plot(range(N+1), L[0], "r")

pyplot.xlabel("score")
pyplot.ylabel("Probablity")

pyplot.show()