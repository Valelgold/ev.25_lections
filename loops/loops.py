# Циклы - это конструкция, при помощи которых можно организовать многократное исполнение определенного кода

# while <expression> == true:
#     <body>
# <else>:>
#     <body>
# i = 1
# while i <= 10:
#     print(f'Цикл выполнился {i} раз!')
#     i += 1
# else:
#     print('Конец цикла!') 
# print('Начало кода')


# name1 = ''
# name2 = ''
# i = 0

# while name1.lower() != 'john' and name2.lower() != 'jamie':
#     name1 = input('Введите первое имя: ')
#     name2 = input('Введите второе имя: ')
#     i += 1
#     if i > 4:
#         print('Цикл остановлен!!')
#         break
# else:
#     print('Вы ввели правильное имя!')

# admin = ['johnsnow23', 'ilovepython23']
# i = 3
# password = None
# username = None

# while username != admin[0] or password  != admin[1]:
#     username = input('Введите имя пользователя: ')
#     password = input('Введите пароль: ')
#     i -= 1
#     if i == 0:
#         print('Вы заблокировали на 5 минут!')
#         break
# else:
#     print(f'{admin[0]} вы успешно вошли в систему!')

# for <variable> in <interable oblect>:
#     <body>


# list_ = [0, 1, 2, 3, 4, 5]
# i = iter(list_)
# print(i)
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))

# for x in list_:
#     print(x)

# ----------------------------------------------------------------------------------------------------------------------------------------

# ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

# for x in ls:
#     print(f'Element: {x}')

# i = 0
# while i < len(ls):
#     print(f'Element: {ls[i]}')
#     i += 1

# -----------------------------------------------------------------------------------------------------------------------------------------

# secret_list = ['DeltaViski', 'LOTR123', 'JohnSnow']
# word = input('Vvedite secret kod: ')

# while word not in secret_list:
#     print('Incorrect word! Try one more time!')
#     word = input('Vvedite secret kod: ')
# print(f'You\'re welcome my friend, {word}')

# --------------------------------------------------------------------------------------------------------------------------------------------

# steps = 8
# path = 'UDDDUDUU'
# sea_level = 0
# dolina = 0
# for x in path:
#     if x == 'U':
#         sea_level += 1
#         if sea_level == 0:
#             dolina += 1
#     elif x == 'D' :
#         sea_level -= 1
      

# 2)
# step = 9
# steps = 'UDDUUDDUU'
# # res = 2 
# sea_level = 0
# dolina = 0
# for x in steps:
#     if x == 'U':
#         sea_level += 1
#         if sea_level == 0:
#             dolina += 1
#     elif x == 'D' :
#         sea_level -= 1

# print(dolina) 


































































