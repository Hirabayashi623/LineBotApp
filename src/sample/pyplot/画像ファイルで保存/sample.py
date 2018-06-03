import matplotlib.pyplot as plt
import numpy as np
import datetime
import os

x = np.random.rand(100)
y = np.random.rand(100)

plt.scatter(x, y)

path = os.getcwd() + '\sample_{0:%Y%m%d%H%M%S}.png'.format(datetime.datetime.now())

plt.savefig(path)
