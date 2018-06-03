import numpy
from matplotlib import pyplot, mlab

x = numpy.array([0.02, 0.12, 0.19, 0.27, 0.42, 0.51, 0.64, 0.84, 0.88, 0.99])
t = numpy.array([0.05, 0.87, 0.94, 0.92, 0.54, -0.11, -0.78, -0.89, -0.79, -0.04])

# 散布図の生成
pyplot.scatter(x,t)

def getPhi(x, demension):
    list = []
    i = 0
    while i <= demension:
        list.append(x**i)
        i += 1

    return list

PHI = numpy.array([getPhi(xi, 3) for xi in x])

w = numpy.linalg.solve(numpy.dot(PHI.T, PHI), numpy.dot(PHI.T, t))
# w = numpy.linalg.so;lve(PHI, t)

print("w → ", w)

def f(x, w):
    ret = 0
    for x_, w_ in zip(x, w):
        ret += x * w

    return ret

sample = 1000
a = numpy.arange(0,1,1.0/sample)
# print("a:", a)
b = []

for ai in a:
    demension = 0
    bi = 0
    for wi in w:
        bi += wi * ai**demension
        demension += 1
    b.append(bi)

pyplot.plot(a, b, "r")

pyplot.show()