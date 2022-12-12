# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
#
# Примеры:
#
# - 1, 4, 8, 7, 5 -> 8
# - 78, 55, 36, 90, 2 -> 90

# a = int(input('Ввиедите число a: '))
# b = int(input('Ввиедите число b: '))
# c = int(input('Ввиедите число c: '))
# d = int(input('Ввиедите число d: '))
# e = int(input('Ввиедите число e: '))
# max_num = a
# list = [a, b, c, d, e]
# for i in list:
#     if max_num < i:
#         max_num = i
# print(max_num)

# def max_number(list):
#     return max(list)
# print(max_number([1, 4, 29, 50, 3]))

list =[]
for i in range(5):
    list.append(int(input('Введите число: ')))
print(max(list))

