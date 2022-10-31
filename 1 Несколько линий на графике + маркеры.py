import matplotlib.pyplot as plt
import numpy as np


# x = np.array([1, 1, 5, 5, 1])
# y = np.array([1, 5, 5, 1, 1])

y = np.arange(0,5) # [0, 1, 2, 3, 4]
x = np.array([a*a for a in y]) # [0, 1, 4, 9, 16]

y2 = np.array([0, 1, 2, 3])
x2 = [i+1 for i in y2]

# lines = plt.plot(x, y, "--ro", x2, y2, ":b^", color="#000") # ИЛИ g - green или в rgb(0, 0, 0, 0.7) 0.8 - прозрачность
lines = plt.plot(x, y, "--rs", x2, y2, "--b^", marker="*", markerfacecolor="w")
# print(lines)
# plt.setp(lines, linestyle="-.")
# ИЛИ plt.plot(x2, y2)
plt.grid() # Сетка
plt.show()