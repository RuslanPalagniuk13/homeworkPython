# Задайте словарь из n чисел последовательности (1 + 1/n))^n и выведите на экран их сумму.
# Пример: Для n = 3 {1:2, 2:2.25, 3:2.37}
#   Необходимо сложить все значения словаря и вывести на экран.

n = int(input('Введите количество чисел в списке: '))

def sequence(n):

    return[round((1 + 1 / x)**x, 2) for x in range (1, n + 1)]   
        
print(sequence(n))
print(round(sum(sequence(n))), 2)

