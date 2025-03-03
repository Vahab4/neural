from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

x = []
y = []
figure, ax = plt.subplots()
ax.set_xlim(0, 100)
ax.set_ylim(0, 12)
line, = ax.plot(0, 0)

def animation_function(i):
    x.append(i * 15)
    y.append(i)
    line.set_xdata(x)
    line.set_ydata(y)
    return line,

animation = FuncAnimation(figure, func=animation_function, frames=np.arange(0, 10, 0.1), interval=10)
plt.show()
