import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2, 2, 1000)

y = np.sin(x)*(1/x)*np.cos(x**2+1/x)

plt.figure(figsize=(8, 6))

plt.plot(x, y, linestyle='-', color='orange', linewidth=2, label=r'$Y(x) = \sin(x) \cdot \frac{1}{x} \cdot \cos(x^2 + \frac{1}{x})$')  # Графік функції

plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)

plt.xlabel('x')
plt.ylabel('Y(x)')
plt.title('Графік функції Y(x)=sin(x) * (\frac{1}{x}) * cos(x^2 + \frac{1}{x})')

plt.legend()

plt.grid(True)

plt.show()