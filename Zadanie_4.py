# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

def from_dec_to_bin(decimal_number):
    binary_number = ''
    while decimal_number > 0:
            binary_number = str(decimal_number % 2) + binary_number
            decimal_number = decimal_number // 2
    return binary_number

number = int(input('Введите число: '))
print(f'В двоичной системе число {number} равняется {from_dec_to_bin(number)}')