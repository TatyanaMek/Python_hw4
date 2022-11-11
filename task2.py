# Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.



number = int(input("Необходимо ввести число: "))
spisok = []
i = 2
while i <= number:
    if number % i == 0:
        spisok.append(i)
        number //= i
    else:
        i +=1
print(spisok)