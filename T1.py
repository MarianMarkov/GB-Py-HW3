"""Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В
последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X"""
import random
n = int(input("Количество элементов массива:"))
Nums = []
print("Массив")
for i in range(n):
    Nums.append(random.randint(0,10))
    print(Nums[i])
x = int(input("Искомое число: "))
c = 0
for i in range(n):
    if Nums[i] == x:
        c += 1
print("- >", c)