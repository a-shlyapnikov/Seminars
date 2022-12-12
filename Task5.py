# Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.
a = int(input('Введите число: '))
if (not a % 5 and not a % 10 or not a % 15) and a % 30:
    print('yes')
else:
    print('no')
# if (a % 5 == 0 and a % 10 == 0 or a % 15 == 0) and a % 30 != 0:
#     print('Кратно')
# else:
#     print('Не кратно')
