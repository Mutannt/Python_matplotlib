import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# img = Image.open("Типы графиков 1.PNG") # Сформировано изображение на основе выбранного
img = np.array(Image.open("Типы графиков 1.PNG")) # Обычный numpy массив

# fig = plt.figure(figsize=(6, 4))
# ax = fig.add_subplot() # Создаём координатные оси
# ax.imshow(img)

# Если используется одна фигура и одна координатная ось, то можно короче
# plt.imshow(img)


# Двумерный массив из случайных чисел в диапазоне от 0 до 255, размером 100 на 100
data = np.random.randint(0, 255, (100, 100))

# plt.imshow(data, cmap="plasma")

# b = plt.imshow(img, origin="lower", cmap="plasma", aspect="equal", alpha=0.7)
# plt.colorbar(b)

plt.pcolormesh(data, edgecolors="black", cmap="plasma")


plt.show()
