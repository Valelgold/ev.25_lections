# Типы данных -> Числа int(), float()

#  = -> оператор присваинвания
# number = 5 # variable (переменная)
# print(number)
# number = 51
# print(number)

#  +
# a = 5
# b = 15
# result = a + b
# print(result)

# print(5+15)

# tommorow_day -> snake case 
# ABC -> верхний регистр 

# a = 100

# b = 1000

# c = 500 #int

# d = 56.20 #float

# print(a + b + c + d)

# -
# num1 = 996
# num2 = 67.55
# print(num1 - num2)

# *
# num1 = int(input('Введите чилсло 1:'))
# num2 = int(input('Введите чилсло 2:'))
# result = num1 * num2
# print('Результат произведения чисел', num1, 'и', num2, 'равно', result)
# print


# num1 = input('Введите число :')
# print(num1)
# print(type(num1))

# num = '15'
# num = int(num)
# print(type(num))

# # / and // and %
# / -> Обычное деление 
# //-> Целочисленное дление(деление без остатка)
# % -> Модульное делени (остаток от деления)

# num1 = 5
# num2 = 2
# print(num1 / num2)
# print(num1 // num2)
# print (num1 % num2)
# ** -> возведение в степень

# num1 = 5 
# print(num1 ** 123456787)
# pow(a,b,<mod>) -> функия возведения числа а в степень 
# print(pow(2,5,5)) # 2 ** 5 % 5 -> 2



#  divmod (a,b) -> она выводит два числаб первое число это результат целочисленного деления (//), а второе число это модульное деление (%) дыух чисел
# res = divmod(32,5)
# print (res)


# round() -> функция округления числа
# res = 24 / 13
# print (round(res, 1))

# abs() - абсолютное значение -> abs (5-) = 5 -> (-5) = 5


# print(abs(-101))
# print(abs(50))


# import math
# from math import pi, sqrt

# print(pi)
# print(sqrt(25))


# print(math.pi)
# math.sqrt -> корень числа

# print(math.sqrt(25))
# print(math.sqrt(101))
# print(math.sqrt(6))

# dir() - возвращает методы обьекта или функции определенного модуля 

# import math

# print(dir(math))

# '''Множественное присваивание'''

# a = 5 

# a, b, c = 1, 2 ,3
# v = 5
# n = 7
# d= 3

# v, n , d =d, v, n 
# print(v, n ,d)

# '''1.Даны две переменные num1 сo значением 10 и num2 со значением 3.
# Поменяйте значения этих переменных между собой. ВАЖНО: Нельзя использовать множественное присваивание.'''

# num1 = 10
# num2 = 3
# num3 = num1
# num1 = num2
# num2 = num3
# print(num1, num2)

# print('hello' * 3) #дублирование строк

# str1 = '12'
# num1 = 2
# print(str1 + str(num1))

'''Инкремент и Дикремент'''

# Инкремент - это увелечение значения какой-либо переменной.Пример: a = 1 (a += 1 -> a = a + 1)

# a = 5 
#  a += 1
# a = a + 10
# print(a)

# Дикримент - уменьшение значения какой-либо перемнной. (a -= 1 -> a = a - 1)

# a = 0
# a -= 1
# print(a) Тут обратное инкременту 

# *

# a = 5
# a *= a
# print(a)

# /
# a = 10
# a /= 2
# print(a)

# '''
# id() -> номер в ячейки  памяти
# '''
# a = 1
# b = 1
# print(id(a))
# print(id(b))

# type() -> выводит заданной переменной
# a = 9
# b = 'hello'
# print(type(a))
# print(type(b))

# var = int(input('Введите число))

# '''примем от пользователя два значения, переведем в тип данных int и возведем первое число в степень второго числа'''

# num1 =  int(input('Введите число'))
# num2 = int(input('Введите степень'))
# print(num1 ** num2)

# '''
# Модуль random - предоставляет функции для генерации случайных чисел, буквы, символы
# '''

# import random

# print(dir(random))

# num = random. randint(1111, 99999)
# print(num)

# from random import choice
# import string 

# # print(string.ascii_letters)
# a = choice(string.ascii_letters)
# print(a)

'''
Задача 1
Дана переменная с радиусом окружности, найдите периметр и площадь окружности, найдите периметр и
 площадь окружности, результат выведите в терминал
'''

# from math import pi
# r = 8
# print (pi * r**2, 2 * r * pi)

# from math import pi

# r = int(input('Введите радиус: '))
# result_P = 2 * r * pi
# result_S = pi * (r ** 2)
# print ('площадь окружност', round(result_S))
# print ('периметр окружност', round(result_P))






