import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import *

# 1
fig = plt.figure(figsize=(7, 4))
ax = fig.add_subplot()

# line1, = ax.plot(np.arange(0, 5, 0.25), label = "Линия 1")
# line2, = ax.plot(np.arange(0, 10, 0.5), label = "Линия 2")

# # Показать легенды на графике
# plt.legend((line2, line1), ["label 1", "label 2"], loc="upper right")
# plt.legend((line2, line1), ["label 1", "label 2"], bbox_to_anchor=(0.5, 0.7))
# plt.legend((line2, line1), [r"$f(x) = a \cdot b + c$", r"$f(x) = k \cdot x + b$"], facecolor="#aaa", framealpha=0.5)

# 2 Дорбавить ломанную линию
li = Line2D([1, 2, 3], [4, 2, 5])
ax.add_line(li)
ax.set(xlim=(0,4), ylim=(0, 6)) # Если это первый график, то нужно определить пределы линии

# 3 Добавить прямоугольник
rect = Rectangle((0, 0), 2.5, 0.5, facecolor="g")
ax.add_patch(rect)

plt.show()

