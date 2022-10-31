import numpy as np
import matplotlib.pyplot as plt
import time

# x = np.arange(-2*np.pi, 2*np.pi, 0.1)

# plt.ion() # Включить интерактивный режим
# for delay in np.arange(0, np.pi, 0.1):
#     y = np.cos(x + delay)

#     plt.clf() # Очищаем окно
#     plt.plot(x, y) # Перерисовываем данные

#     # Обновить данные в окне
#     plt.draw()
#     plt.gcf().canvas.flush_events() # Обработка внутренних событий matplotlib и перерисовку окна

#     time.sleep(0.02) # Задержка на 20м секунд
#     # Медленный вариант. Здесь на каждой итерации полностью перерисовывается всё окно
# plt.ioff() # Выключить интерактивный режим
# plt.show()


# Быстрый вариант через объекно - ориентированный подход
plt.ion() # Включить интерактивный режим
fig, ax = plt.subplots() # Создание координатной оси и фигуры
x = np.arange(-2*np.pi, 2*np.pi, 0.1)
y = np.cos(x + 0) # deley = 0
line, = ax.plot(x, y)


for delay in np.arange(0, np.pi, 0.1):
    y = np.cos(x + delay)

    line.set_ydata(y) # Обновляем данные косинусоиды. Каждый раз передаём новые данные

    # Обновить данные в окне
    plt.draw()
    plt.gcf().canvas.flush_events() # Обработка внутренних событий matplotlib и перерисовку окна

    time.sleep(0.02) # Задержка на 20м секунд
plt.ioff() # Выключить интерактивный режим
plt.show()