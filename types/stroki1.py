#  String - Строки

'Hello world '
'hello world'

'''
Hello word
My name is John Snow
'''

# a = 5 # коммент

# Строки - Набор последовательных символов, которые мы используем для хранения и 
# представления текстовой информации.Набор методов и операций которые мы можем использовать с данными в виде текста

# Индексация в строке
# Индексация начинается с числа 0
# name = 'John' 
#        J = 0 = -4
#        o = 1 = -3
#        h = 2 = -2
#        n = 3 = -1
# print(name)
# print(name[1])
# print(name[-1])

# str1 = 'birthday'
# print(str1[5], str1[6], str1[7])
# print(str1[-3], str1[-2], str1[-1])
# print(str1 [0], str1[1], str1[2], str1[3], str1[4])

# Срезы по индексам
# [start: end: <step>]
# # len()
# str1 = 'birthdayrreroierdyfhiurkjfheiuksjfehuridkjfher'
# str2 = str1[0:5] #сделай срез до 5, 5-й индекс не будет включен 
# print(str2)
# print(str1 [5:7])
# print(len(str1))
# print(str1[5:])
# print(str1[:5])

# \ - мы используем для того, чтобы мы могли использовать всего одну чёрточку азазазз вместо двух
# text = 'Hello world! My name is John! I\'m North King!'
# print(text)
# print(len(text))

# print(text[:12])
# print(text[13: 29])
# print(text[30:])

# print(text[:12:4])
# print(text[::2])
# print(text[::-1])
# print(text[:12:-1])

# Конкатенация строк(слияние, соединение)

# word1 = 'Hello'
# word2 = 'World'
# probel = ' '

# result = word1 +probel + word2 
# print(result)
# print(word1 + probel + word2 + '!')

# Форматирование строк
# 1. С помощью %
# 2. С помощью (.format())
# 3. Интерполяция строк(f - строки)

#  %
# name = input('Enter your name:')
# last_name = input('Enter you last name:')
# print('Hello, My name is', name, last_name)
# print('Hello, My name is' + ' ' + name + ' ' + last_name)
# print('Hello, My name is %s %s' %(name, last_name))



# # .format
# name = input('Enter your name:')
# last_name = input('Enter you last name:')
# print('Hello, My name is {} {}'.format(last_name, name ))

# # f - строки
# name = input('Enter your name:')
# last_name = input('Enter you last name:')

# print(f'Hello, My name is {name} {last_name}!')

# Экранирование строк - механизм при помощи которого можно вставлять символы, которые сложно ввести с клавиатуры в строку
# \n - перенос строки
# \t - горизонтальная табуляция 
# \v - вертикальная табуляция

# name = 'John\nSnow'
# lastName = '\vSnow'
# last_name = '\tSnow'

# # print(name)
# print(lastName)
# print(last_name)

# r' - это сырая строка, здесь любой экранированный знак игнорируется
# string = r'hhhhh\n'
# print(string)

# printi(строка * любое число) - используется для того чтобы умножить 
# string = '1235'
# print( string * 20)

# # partition(patter) -> tuple
# string = 'Hello Makers Bootcamp '
# print(string.partition('Bootcamp'))



# string1 = 'Hello'
# string2 = 'eren'
# print(f' {string1}  {string2}')