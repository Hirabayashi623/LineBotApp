import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 1, 0.01)
y = np.arange(0, 1, 0.01)
z = np.array([[np.exp(-((xi - 0.5)**2 + (yi - 0.5)**2)) for xi in x] for yi in y])

# print(x)
# print(y)
# print(z)

plt.contourf(x,y,z)

plt.show()