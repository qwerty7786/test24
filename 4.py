import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10,10)
y = [1/i for i in x]
plt.title('Гипербола')
plt.xlabel('Ось Х')
plt.ylabel('Ось Y')
plt.grid()
plt.plot(x,y)
plt.show()