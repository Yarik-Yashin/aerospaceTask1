import math  # импортируем библиотеку для математических вычислений
import matplotlib.pyplot as plt  # библиотека для построения графиков и визуалищации данных
import numpy as np


def func(x):
    return math.e ** (-x / 9) * 1.2


x = np.arange(0.0, 130.0, 0.3)
y = np.vectorize(func)
y = y(x)
fig = plt.figure()  # создание объекта для рисования графиков
plt.title('Зависимость плотности атмосферы от высоты')  # заголовок
plt.xlabel('h, км')  # подпись оси OX
plt.ylabel('ρ, кг/м3')  # подпись оси OY
plt.plot(x, y)
plt.show()
