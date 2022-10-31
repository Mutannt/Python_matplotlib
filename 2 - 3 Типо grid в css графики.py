# Отображение нескольких координатных осей в одном окне
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.gridspec import GridSpec

# axes1 = plt.subplot(2, 3, 1) # Своя каординатная ось
# plt.plot(np.random.random(10)) # Случайные значения
# axes2 = plt.subplot(2, 3, 2) # Своя каординатная ось
# plt.plot(np.random.random(10)) # Случайные значения
# axes3 = plt.subplot(2, 3, 3) # Своя каординатная ось
# plt.plot(np.random.random(10)) # Случайные значения
# axes4 = plt.subplot(2, 1, 2) # Индекс 2 т.к. создаём график ниже
# plt.plot(np.random.random(10)) # Случайные значения

# axes1.grid()
# axes2.grid()
# axes3.grid()
# axes4.grid()

# plt.show()



# 2 Несколько на одной
# f, ax = plt.subplots(2, 2) # Возвращает ссылку на фигуру и на список каординатных осей
# fig = plt.figure(figsize=(7, 4)) # Доп. фигура
# ax1 = fig.add_axes([0.0, 0, 1.0, 1.0]) # Расположение и размер координатных осей
# от [0, 1], определяют долю от ширины и высоты всего окна
# # ИЛИ
# # ax1 = fig.add_subplot(1,2,1) # Расположение и размер координатных осей
# ax1.plot(np.random.random(10)) # Случайные значения
# # plt.plot(np.random.random(10)) # Случайные значения
# # Параметры
# f.set_size_inches(7, 4) # Размер 7 x 4 дюйма
# f.set_facecolor("#eee") # Цвет фона

# f.suptitle("Заголовок фигуры")
# fig.suptitle("Заголовок доп. фигуры")
# ax1.set_title('Заголовок оси1')
# ax[0, 0].set_title('Заголовок оси 1')
# ax[0, 1].set_title('Заголовок оси 2')
# ax[1, 0].set_title('Заголовок оси 3')
# ax[1, 1].set_title('Заголовок оси 4')


# ax[0, 0].plot(np.arange(0, 5, 0.2))
# ax[0, 0].grid()
# ax[0, 1].plot(np.arange(5, 0, -0.2))
# ax[0, 1].grid()
# plt.show()


# 3
# fig = plt.figure(figsize=(7, 4))
# gs = GridSpec(ncols=3, nrows=2, figure=fig)

# ax1 = plt.subplot(gs[0, 0])
# ax1.plot(np.arange(0, 5, 0.2))
# ax2 = fig.add_subplot(gs[1, 0:2])
# ax2.plot(np.random.random(10))
# ax3 = fig.add_subplot(gs[:, 2])
# ax3.plot(np.random.random(10))

# fig.suptitle("Заголовок фигуры")
# ax1.set_title('Заголовок оси1')
# ax2.set_title('Заголовок оси2')
# ax3.set_title('Заголовок оси3')


# plt.show()
