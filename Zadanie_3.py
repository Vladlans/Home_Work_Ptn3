#Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

float_numbers = [1.1, 1.2, 3.1, 5, 10.01]
remainder_of_numbers = list()
for i in float_numbers:
    if i%1:
        remainder_of_numbers.append(round(i%1,2))
print(f'Разница между максимальным и минимальным значениесм дробной части равна {max(remainder_of_numbers) - min(remainder_of_numbers)}')