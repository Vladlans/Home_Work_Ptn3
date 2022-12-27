# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

import random
import math


def create_list():
    numbers = list()
    for i in range(0,7):
        numbers.append(random.randint(1, 20))
    return numbers


def finding_products(numbers):
    product_of_numbers = list()
    j = -1
    for i in range(math.ceil(len(numbers)/2)):
            product_of_numbers.append(numbers[i]*numbers[j])
            j += -1
    return product_of_numbers


nums = create_list()

print(nums)

print(finding_products(nums))