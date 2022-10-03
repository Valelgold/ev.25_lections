# print(dir(str)) #методы строк

# replace(old, new [count]) - меняем в строке old на new значение, если вы укажете count, то он заменит его ровно count раз.

# text = 'ha ha ha ha'
# result = text.replace('a', 'i', 1)
# print(text) 
# print(f'result after replace: {result}')

# str1 = 'Hello world! My name is John Snow'
# result = str1.replace('John Snow', 'Jamie Lanister')
# print(result)

# print(id('H'))
# print(id('H'))
# print(id('h'))
# У каждой буквы, cимвола и тд, есть свобственный код, это значит, что нужно быть точнее.

# strip() - Убирает пробельные символы в начале и в конце строки
# rstrip, lstrip 

# text = input('enter the text: ')
# print(text)
# res = text.strip()
# print(res)
# print(len(res))

# text = '   hello world   '
# print(len(text))
# res = text.lstrip()
# print(res)
# print(len(res))

# print(dir(str))

# isdigit ->            Проверяют
# isnumeric -> ->  состоит ли наша строка
# isdecimal ->      полностью из чисел

# text = '57s'
# if text.isdigit():
#     num = int(text)
#     print(num)
# else:
#     print('Oops! Invalid symbols!')

# text = '\u0031'
# print(text)
# print(text.isnumeric)

# isalnum() -> проверяет состоит ли наша строка из чисел и символов латинского алфавита и киррилицы

# str1 = '56a'
# print(str1.isalnum()) 
# str2 = '56_a'
# print(str2.isalnum()) 

# isalpha() -> состоит ли наша строка полностью из символов латинского либо киррильского алфавита 

# text = 'Hello world'
# print(text[:5:].isalpha())

# islower()
# isupper()
# istitle()

# str1 = '144'
# print(str1.istitle())

# idex(value, [start], [end]) -> выводит индекс значения value которое мы передаем в нашей строке

# count(value, [start]) -> считает количество вхождений value в нашу строку

# text = 'hello o o hello'
# print(text.count('hello'))
# print(text.count('o'))
# print(text.count(' '))

# text = 'Hello world! My name is John Snow'
# print(text.index('John'))
# res = text.index('o')
# print(res)
# res = text.index('o', res+1)
# print(res)
# res = text.index('o', res+1)
# print(res)
# res = text.index('o', res+1)
# print(res)




# # text = 'oooHello world! My name is John Snowooo'
# text = input('Enter the text: ')
# i = 0
# res = -1 
# while i < text.count('o'): #4
#     res = text.index('o', res+1)
#     print (res)
#     i += 1 #инкремент i = i + 1 # i++

# find(value,[start], [end]) -> делает тоже самое что и index, но есть одно отличие, в том что если value нет в строке то возращается индекс -1 
# rfind - делает то же самое просто оно начинает искать нужную букву с права на лево
# text = 'Hello'
# print(text.find('l'))
# print(text.find('hi'))

# swapcase() -> Переводит все символы в противополжный регистр
# upper() -> все символы в верхний регистр
# lower() -> все символы в нижний регистр

# text = 'hellO World, JoHN, SNow'
# print(text)
# print(text.swapcase())
# print(text.upper())
# print(text.lower())

# capitalize - переводит первую букву в верхний регистр 

# name = input('Enter your name:').capitalize()
# print(f'hello! mr/mrs {name}!')

# titile() -> переводит первые символы всех слов в верхний регистр 

# text = 'john jamie sansa nursultan jerry'
# print(text)
# print(text.title())
# print(text.capitalize())

# name = input('Vvedite FIO: ')
# print(name.title())

# split(разделитель) - дробит строку по разделителю, который находится в строке, все части строки сохраняются в тип данных list

# text = 'Let me speak by my heart in English! Cause My name is John Snow!'
# ls = text.split(' ')
# print(ls)  
# print(len(ls)) 

# 'разделитель'.join(iterable(list)) -> соединяет по разделителю строки, которые находятся в list
# list_ = ('1', '5' , '6', '7')
# list = ''.join(list_)
# print(list)

# startswith(), endswith()

# string = 'I love makers'
# print(string.startswith('I '))
# print(string.endswith('makers'))

# zfill(width)  - заполняет первые символы нулями, можем написать любое значение 
# string = 'makers'
# print(string.zfill(57))

# ljust(width, fillchar), rjust(width, fillchar) - также как и zfill заполняет пустоты/дополняет их, но только с этими командами мы можем выбирать с какой стороны и какими символами их заполнять
# string = 'makers'
# print(string.ljust(9, '&'))
# print(string.rjust(23, '('))


# text = 'tatakae'
# # print(text.replace('kae', 'new'))
# # text = text.replace('kae', 'new')
# # print(text)
# # print(len(text))
# print(text[:4].islower())


string = "cow loves good milk"
result = string.replace('o', 'e', 2)
print(result)

# string = "cow loves good milk"
# print(string.replace('o', 'e', 2))