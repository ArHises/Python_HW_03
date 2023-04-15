"""
Задача 16: 
Требуется вычислить, сколько раз встречается некоторое число X в списке A[1..N]. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai.
Последняя строка содержит число X

*Пример:*

5
    1 2 3 4 5
    3
    -> 1

"""
import random

n = int(input('Enter list length: '))
x = int(input('Enter number to find: '))

some_list = []
for _ in range(0 , n + 1):
    number = random.randint(1, 10)
    some_list.append(number)
print(some_list)

counter = 0
for i in some_list:
    if i == x:
        counter += 1

print(counter)