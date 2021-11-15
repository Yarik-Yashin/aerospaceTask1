import math  # импортируем библиотеку для математических вычислений
import matplotlib.pyplot as plt  # библиотека для построения графиков и визуалищации данных
import numpy as np  # библиотека numpy для работы с массивами


# функция вычисления плотности атмосферы
def func(x):
    return math.e ** (-x / 9) * 1.2


x = np.arange(0.0, 130.0, 0.3)  # массив значений X
y = np.vectorize(func)  # задаем функцию y
y = y(x)  # задаем массив значений Y
fig = plt.figure()  # создание объекта для рисования графиков
plt.title('Зависимость плотности атмосферы от высоты')  # заголовок
plt.xlabel('h, км')  # подпись оси OX
plt.ylabel('ρ, кг/м3')  # подпись оси OY
plt.grid(True)
plt.plot(x, y)
plt.show()
