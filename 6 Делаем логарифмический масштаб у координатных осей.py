import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(7, 4))
ax = fig.add_subplot()

x = np.arange(-10*np.pi, 10*np.pi, 0.1)
# ax.plot(x, np.sinc(x) * np.exp( - np.abs(x/10)) )
# ax.semilogy(x, np.sinc(x) * np.exp( - np.abs(x/10)) )
# ИЛИ
# ax.plot(x, np.sinc(x) * np.exp( - np.abs(x/10)) )
# ax.set_yscale("log") # Взять по оси y логарифмический масштаб
# ax.set_xscale("log") # Взять по оси x логарифмический масштаб
# ax.set_yscale("log", subs=[2,9]) # По основанию 10 или base=5

# ax.set_xscale("symlog", lintresh=2, linescale=5) # от -2 до 2 будет использоваться линейный масштаб, а всё что за логарифмический

ax.loglog(x, np.sinc(x) * np.exp( - np.abs(x/10)) ) # Логарифмический масштаб по обеим осям



ax.grid()
plt.show()