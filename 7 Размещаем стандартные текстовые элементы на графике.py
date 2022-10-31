
import numpy as np
import matplotlib.pyplot as plt

# y = np.arange(0, 5, 1) # [0, 1, 2, 3, 4]
# x = np.array([a*a for a in y]) # [0, 1, 4, 9, 16]

# y2 = [0, 2, 4, 5, 7]
# x2 = [i+1 for i in y2]

# lines = plt.plot(x, y, x2, y2)

# plt.minorticks_on() # Минорная сетка
# plt.grid(which="major", color="#444", lw = 1) # lw - linewidth = 2, толщина 2px
# # Мелкая сетка снижает производительность, поэтому без особой необходимости её лучше не использовать
# plt.grid(which="minor", color="#aaa", ls=":") # ls - linestyle

# plt.show()
# ========================================================================================================================================

fig = plt.figure(figsize=(7, 4)) # ,facecolor = '#eee'
fig.set(facecolor = '#eee')
ax = fig.add_subplot() # ax - ссылается на координатную ось
ax.set(facecolor = '#AAFFAA')
plt.figtext(0, 0.6, "Текст в области окна", fontsize=24, color="r") # От 0 до 1
fig.suptitle("Заголовок окна1")
ax.set_title('Заголовок окна2')
ax.set_xlabel("Ось x")
ax.set_ylabel("Ось y")
# plt.xlabel("Ось x") # Если одна координатная ось
# plt.ylabel("Ось y")
ax.text(0.05, 0.1, "Произвольный текст в координатных осях", bbox={"boxstyle":"darrow",'facecolor': '#AAAAFF',
'alpha': 0.3, 'pad': 1})
ax.annotate("Аннотация", xy=(0.2, 0.4), xytext=(0.6, 0.7),
arrowprops={"facecolor": "gray", "shrink": 0.1})




# ax2 = fig.add_subplot()
# fig.suptitle("Заголовок окна3")
# ax2.set_title('Заголовок окна4')

plt.show()