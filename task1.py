# Пользователь вводит число, Вам необходимо вывести число Пи с той точностью знаков после запятой, сколько указал пользователь
# (БЕЗ ИСПОЛЬЗОВАНИЯ МОДУЛЕЙ/БИБЛИОТЕК)

from cmath import pi


d =  int(input("Сколько знаков после запятой Вы хотите увидеть в числе Пи?\n"))
print(f'вот,пожалуйста {round(pi, d)}')