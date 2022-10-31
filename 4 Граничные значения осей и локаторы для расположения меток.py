import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import NullLocator, LinearLocator, MultipleLocator, IndexLocator, FixedLocator, LogLocator, MaxNLocator

fig = plt.figure(figsize=(7, 4))
ax = fig.add_subplot()
ax.plot(np.arange(1, 5, 0.25))


ax.grid()
# ax.yaxis.set_major_locator(NullLocator())
# ax.yaxis.set_major_locator(LinearLocator(5))
ax.yaxis.set_major_locator(MultipleLocator(base=2))


# 2 IndexLocator, FixedLocator, LogLocator, MaxNLocator
fig2 = plt.figure(figsize=(7, 4)) # Доп. фигура
ax2 = fig2.add_subplot()

x = np.arange(-np.pi/2, np.pi, 0.1)

ax2.plot(x,np.sin(x)) # Случайные значения
ax2.set_title('IndexLocator, FixedLocator, LogLocator, MaxNLocator')


# ax2.grid()
# Минорная сетка
ax2.minorticks_on()
ax2.grid(which="major", lw = 2) # lw = 2, толщина 2px
ax2.grid(which="minor")

# ax2.xaxis.set_major_locator(IndexLocator(base=0.5, offset=0)) # offset=0.57
# ax2.xaxis.set_major_locator(FixedLocator([-2, -1, 0, 1, 2, 3]))
# ax2.xaxis.set_major_locator(LogLocator(base=2))
# ax2.xaxis.set_major_locator(MaxNLocator(6))
ax2.xaxis.set_minor_locator(NullLocator())


plt.show()