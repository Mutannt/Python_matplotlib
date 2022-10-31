import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter, FormatStrFormatter, FuncFormatter, ScalarFormatter, FixedFormatter

# # Отрицательные значения в квадратные, а положит в круглые
# def format0y(x, pos):
#     return f"[{x}]" if x < 0 else f"({x})"

fig = plt.figure(figsize=(7, 4)) # Доп. фигура
ax = fig.add_subplot()

x = np.arange(-np.pi/2, np.pi, 0.1)

# ax.plot(x,np.sin(x)) # Синус
ax.plot(x, np.sin(x) * 1e5) # Синус

# ax2.set_xticklabels([])
# ax2.set_yticklabels([])

# ax.xaxis.set_major_formatter(NullFormatter())
# ax.xaxis.set_major_formatter(FormatStrFormatter("x = %.2f"))
# ax.yaxis.set_major_formatter(FuncFormatter(format0y))

# sf = ScalarFormatter()
# sf.set_powerlimits((-4, 4)) # Берётся интервал от 10е-4 до 10е4, если превышает, то выносится за скобку
# ax.yaxis.set_major_formatter(sf)

ax.xaxis.set_major_formatter(FixedFormatter([-3, -2, -1, 0, 1, 2, 3]))


ax.grid()
plt.show() 