from cProfile import label
import numpy as np
import matplotlib.pyplot as plt

# http://kodesource.top/graphics/matplotlib/basic/index.php

# # 1 ======================================================================================================================================
# x = np.arange(0, 50, 10)
# y = [value * 3 for value in x]

# f, ax1 = plt.subplots()
# ax1.plot(x, y)
# ax1.set_title('Нормальное распределение')

# ax1.set_xlabel('x - label')
# ax1.set_ylabel('y - label')
# plt.show()

# 3 ======================================================================================================================================
# # x = [1,2,3]
# # y = [2,4,1]
# Но надо запускать всю папку в VS Code
# with open("test.txt") as f:
#     data = f.read()
# data = data.split('\n')

# x = [row.split(' ')[0] for row in data]
# y = [row.split(' ')[1] for row in data]

# f, ax1 = plt.subplots()
# ax1.plot(x, y)
# ax1.set_title('Нормальное распределение')

# ax1.set_xlabel('x - label')
# ax1.set_ylabel('y - label')
# plt.show()

# 4 Импорт из .csv файла ======================================================================================================================================
# import pandas as pd
# df = pd.read_csv('fdata.csv', sep=';', parse_dates=True, index_col=0)
# df.plot()
# plt.show()

# # 5 Две и более линий на одном графике с подходящими легендами =====================================================
# fig = plt.figure(figsize=(7, 4)) # Доп. фигура
# ax = fig.add_subplot()

# # x1 = [10,20,30]
# # y1 = [20,40,10]
# # x2 = [10,20,30]
# # y2 = [40,10,30]

# x = np.arange(-np.pi/2, np.pi, 0.1)
# y2 = np.arange(0,5) # [0, 1, 2, 3, 4]
# x2 = np.array([a*a for a in y2]) # [0, 1, 4, 9, 16]

# line1 = ax.plot(x, np.sin(x), label = "Линия 1") 
# line2 = ax.plot(x2, y2, label = "Линия 2")

# # Показать легенды на графике
# plt.legend()

# ax.set_title('Две и более линий на одном графике с подходящими легендами')
# ax.set_xlabel('x - label')
# ax.set_ylabel('y - label')

# ax.grid()
# plt.show() 


# 6-7 Две и более линий различной ширины и цвета, стиля на одном графике с подходящими легендами =========================================
# fig = plt.figure(figsize=(9, 4)) # Доп. фигура
# ax = fig.add_subplot()

# x1 = [10,20,30]
# y1 = [20,40,10]
# x2 = [10,20,30]
# y2 = [40,10,30]

# line1 = ax.plot(x1, y1, "--r", label = "Линия 1 w3 Пунктирная", linewidth = "3") 
# line2 = ax.plot(x2, y2, ":b", label = "Линия 2 w5 Штрих", linewidth = "5")
# # ИЛИ
# # lines = ax.plot(x1, y1, "--r",  x2, y2, "b")
# # plt.setp(lines[0], label = "Линия 1 w3", linewidth = "3")
# # plt.setp(lines[1], label = "Линия 2 w5", linewidth = "5")

# # Показать легенды на графике
# plt.legend()

# ax.set_title('Две и более линий различной ширины и цвета, стиля на одном графике с подходящими легендами')
# ax.set_xlabel('x - label')
# ax.set_ylabel('y - label')

# ax.grid()
# plt.show() 

# 8 установки маркеров линий ======================================================================================================================
# fig = plt.figure(figsize=(9, 4)) # Доп. фигура
# ax = fig.add_subplot()

# x1 = [1,4,3,6,7]
# y1 = [2,6,3,6,3]


# line1 = ax.plot(x1, y1, "-.r", label = "Линия 1 w3 Пунктирная", linewidth = "3", marker="o", markerfacecolor="b",  markersize=12) 

# # ИЛИ
# # lines = ax.plot(x1, y1, "--r",  x2, y2, "b")
# # plt.setp(lines[0], label = "Линия 1 w3", linewidth = "3")
# # plt.setp(lines[1], label = "Линия 2 w5", linewidth = "5")

# # Показать легенды на графике
# plt.legend()

# ax.set_title('Две и более линий различной ширины и цвета на одном графике с подходящими легендами')
# ax.set_xlabel('x - label')
# ax.set_ylabel('y - label')

# ax.grid()
# plt.show() 

# 9 отображениe значений пределов текущей оси и установки новых значений оси ==============================================================

# fig = plt.figure(figsize=(9, 4)) # Доп. фигура
# ax = fig.add_subplot()

# x = range(1, 50)
# y = [value * 3 for value in x]

# # Граничные значения по осям
# line1 = ax.plot(x, y, label = "Линия") 
# ax.set(xlim=(0, 100), ylim=(0, 200))
# ИЛИ ax.axis([0, 100, 0, 200])

# # Показать легенды на графике
# plt.legend()

# fig.suptitle("Рисуем линию")
# ax.set_title('Рисуем линию')
# ax.set_xlabel('x - label')
# ax.set_ylabel('y - label')

# ax.grid()
# plt.show() 

# 10 построения графиков разброс с позициями x и y. ==============================================================

# fig = plt.figure(figsize=(9, 4)) # Доп. фигура
# ax = fig.add_subplot()

# x1 = [2, 3, 5, 6, 8]
# y1 = [1, 5, 10, 18, 20]

# x2 = [3, 4, 6, 7, 9]
# y2 = [2, 6, 11, 20, 22]

# # Граничные значения по осям x и y
# ax.axis([0, 10, 0, 30]) 
# # use pylab to plot x and y as red circles
# ax.plot(x1, y1,'b*', x2, y2, 'ro')

# # Показать легенды на графике
# plt.legend()

# fig.suptitle("Разброс точек1")
# ax.set_title('Разброс точек2')
# ax.set_xlabel('x - label')
# ax.set_ylabel('y - label')

# ax.grid()
# plt.show() 


# 11 построения графиков разброс с позициями x и y. ==============================================================

# fig = plt.figure(figsize=(9, 4)) # Доп. фигура
# ax = fig.add_subplot()

# t = np.arange(0., 5., 0.2)

# # Граничные значения по осям x и y
# ax.axis([0, 5, 0, 120]) 
# # use pylab to plot x and y as red circles
# ax.plot(t, t,'g_', t, t**2, 'bs', t, t**3, 'r^')

# # Показать легенды на графике
# plt.legend()

# fig.suptitle("Разброс точек1")
# ax.set_title('Разброс точек2')
# ax.set_xlabel('x - label')
# ax.set_ylabel('y - label')

# ax.grid()
# plt.show() 


# 12 создания нескольких типов диаграмм (простая кривая и построение нескольких величин) на одном наборе осей ==================================


fig = plt.figure(figsize=(9, 4)) # Доп. фигура
ax = fig.add_subplot()

t = np.arange(0., 5., 0.2)

# Граничные значения по осям x и y
ax.axis([0, 5, 0, 120]) 
# use pylab to plot x and y as red circles
ax.plot(t, t,'g_', t, t**2, 'bs', t, t**3, 'r^')

# Показать легенды на графике
plt.legend()

fig.suptitle("Разброс точек1")
ax.set_title('Разброс точек2')
ax.set_xlabel('x - label')
ax.set_ylabel('y - label')

ax.grid()
plt.show() 
