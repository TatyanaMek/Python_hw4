# Пользователь вводит число, Вам необходимо вывести число Пи с той точностью знаков после запятой, сколько указал пользователь
# (БЕЗ ИСПОЛЬЗОВАНИЯ МОДУЛЕЙ/БИБЛИОТЕК)

import math


num = int(input('Введите число '))
num = num + 2
pi = str(math.pi)[0:num]
print(float(pi))