# Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.

numbers = [1, 10, 1, 5, 9, 5, 10, 7, 1]
def new_numbers(numbers):
    new = []

    for number in numbers:
        if number in new:
            continue
        else:
            new.append(number)
    return new

print(new_numbers(numbers))