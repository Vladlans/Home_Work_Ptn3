# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

import random
def create_list():
    numbers = list()
    for i in range(0,7):
        numbers.append(random.randint(1, 20))
    return numbers


def odd_index_summ(numbers):
    sum = 0
    for idx, item in enumerate(numbers):
            if idx % 2:
                sum += item
    return sum


nums = create_list()
print(nums)
print(odd_index_summ(nums))