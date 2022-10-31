import numpy as np
import matplotlib.pyplot as plt
# from matplotlib.ticker import MultipleLocator

# Ступенчатый
# fig = plt.figure(figsize=(4, 4))
# ax = fig.add_subplot() # Создаём координатные оси

# x = np.arange(0, 10) # 0..9
# # ax.step(x, x, "-go")
# ax.step(x, x, "-go", x, np.cos(x), "--x", where="mid") # Сначала по горизонтали, а потом по вертикали

# # ax.yaxis.set_major_locator(MultipleLocator(base=1)) # С шагом 1

# ax.grid()

# plt.show()

# ==============================================================================================================
# # Стековый график
# fig = plt.figure(figsize=(7, 4))
# ax = fig.add_subplot() # Создаём координатные оси

# x = np.arange(-2, 2, 0.1)
# y1 = np.array([-y**2 for y in x]) + 8
# y2 = np.array([-y**2 for y in x]) + 8
# y3 = np.array([-y**2 for y in x]) + 8
# ax.stackplot(x, y1, y2, y3) # Сумма значений

# # ax.yaxis.set_major_locator(MultipleLocator(base=1)) # С шагом 1

# ax.grid()

# plt.show()

# ==============================================================================================================
# Stem график
# fig = plt.figure(figsize=(7, 4))
# ax = fig.add_subplot() # Создаём координатные оси

# x = np.arange(-np.pi, np.pi, 0.3)
# ax.stem(x, np.cos(x), "-.r", "^b", ":g", bottom=0.5) # Тип линий, тип маркера, базовой линии

# # ax.yaxis.set_major_locator(MultipleLocator(base=1)) # С шагом 1

# ax.grid()

# plt.show()

# ==============================================================================================================
# Точечный график
fig = plt.figure(figsize=(7, 4))
ax = fig.add_subplot() # Создаём координатные оси

x = np.random.normal(0, 2, 500) # 500 значений. Нулевое среднее, мера разброса 2
y = np.random.normal(0, 2, 500) # 500 значений. Нулевое среднее, мера разброса 2

# ax.scatter(x, y)
ax.scatter(x, y, s=50, c="g", linewidths=1, marker="s", edgecolors="r")

# ax.yaxis.set_major_locator(MultipleLocator(base=1)) # С шагом 1

ax.grid()

plt.show()

# ==============================================================================================================
# как меняется обхват шеи человека с увеличением роста?

# соберем данные для роста и обхвата шеи
height_women_new = [1.48, 1.49, 1.49, 1.50, 1.51, 1.52, 1.52, 1.53, 1.53, 1.54, 1.55, 1.56, 1.57, 1.57, 1.58, 1.58, 1.59, 1.60, 1.61, 1.62, 1.63, 1.64, 1.65, 1.65, 1.66, 1.67, 1.67, 1.68, 1.68,  1.69, 1.70, 1.70, 1.71, 1.71, 1.71, 1.74, 1.75, 1.76, 1.77, 1.77, 1.78]
neck_women =       [29.1, 30.0, 30.1, 30.2, 30.4, 30.6, 30.8, 30.9, 31.0, 30.6, 30.7, 30.9, 31.0, 31.2, 31.3, 32.0, 31.4, 31.9, 32.4, 32.8, 32.8, 33.3, 33.6, 33.0, 33.9, 33.8, 35.0, 34.5, 34.7, 34.6, 34.2, 34.8, 35.5, 36.0, 36.2, 36.3, 36.6, 36.8, 36.8, 37.0, 38.5]


fig = plt.figure(figsize = (10,6))
ax = fig.add_subplot()
ax.scatter(height_women_new, neck_women)
 
# добавим подписи
ax.set_xlabel('Рост, см', fontsize = 16)
ax.set_ylabel('Обхват шеи, см', fontsize = 16)
ax.set_title('Зависимость роста и окружности шеи у женщин в России', fontsize = 18)

plt.show()