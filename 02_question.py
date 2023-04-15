"""
Задача 18: 
Требуется найти в списке A[1..N] самый близкий по величине элемент к заданному числу X.
Пользователь в первой строке вводит натуральное число N – количество элементов в списке.
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

*Пример:*

5
    1 2 3 4 5
    6
    -> 5

"""

n = int(input('Enter list length: '))

some_list = []
for i in range(0 , n + 1):
    some_list.append(i)

print(some_list)

x = int(input('Enter number to find: '))

diff = some_list[0]

for i in some_list:
    if i > x:
        if diff > x:
            if i - x < diff - x:
                diff = i
        else:
            if i - x < x - diff:
                diff = i
    elif diff > x:
        if x - i < diff - x:
            diff = i 
    else:
        if x - i < x - diff:
            diff = i 

print(diff)