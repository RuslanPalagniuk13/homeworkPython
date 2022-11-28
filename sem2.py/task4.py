# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 

from random import randint
numbers = []
for i in range(10):
    numbers.append(randint (-10,10))
print(numbers)

def get_numbers(numbers):
    count =0 
    for element in numbers:
        count +=1
    return count
print('Количество элементов: ', get_numbers(numbers))

x = int(input('Введите первый элемент из списка: '))
y = int(input('Введите второй элемент из списка: '))

for i in range(len(numbers)):
    mult = numbers[x -1]*numbers[y - 1]
print(f'Произведение элементов на указанных позициях: {numbers[x -1]} * {numbers[y -1]} =', mult)