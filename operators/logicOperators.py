# Операторы сравнения
# Условные операторы
# Логические операторы

# Операторы сравнения
# <, >, ==(равно), <=, >=, !=(не равно)

# 1 < 5 -> True 
# # 7 > 9 -> False
# num1 = 15
# num2 = 15
# print(num1 != num2)

# num1 = 20
# num2 = 17
# print(num1 <= num2)

# Когда мы сравниваем строки то, оно не сравнивает кол-во букв в переменных, а ascii cod первого символа
# stroka1 = 'Hello'
# stroka2 = 'World'
# print(stroka1 < stroka2)
#     #104        87
# print('Hello world!')

# print(ord('H'))
# print(ord('а'))
# print(chr(1080), chr(109))
# print(ord('И'))

# # У всего есть asci code
# stroka1 = 'Hello'
# stroka2 = 'World John Snow'

# print(len(stroka1) < len(stroka2))

# Условные операторы [Операторы Ветвления]
# if
# elif
# else

# if <condition>: 
#     <body if> #сработает, если в выражении if придет true
# [elif] <condition>:       #мы можем использовать его сколько нам угодно раз
#     <body if> 
# [else]:
#     <body else> #срабатывает, если во всех выше стоящих условияз пришо false      #мы используем только в конце

# string = input('Enter smt: ')
# if string() == 'hello':
# elif string.lower() == 'john':
#     print('Welcome back John Snow! The king of North!')
# elif string.lower() == 'abra-kadabra':
#     print('Sim Salamon Kadabra!')
# else:
#     print('Совпадений не найдено!') 

# print(string)
# raise нужен для того, чтобы код остановился в случае ошибки

# email = input('Enter email: ')
# password1 = input('Enter the password' )

# if len(password1) < 8:

#     raise ValueError('Password too short!')
    
# password2 = input('Enter the password confirmation:') 

# if password1 != password1:
#     raise ValueError('Passwords didn\'t match!')
# else:
#     print('Successfully signed up!')

# age =input('Enter your age: ')

# if age.isdigit( ):
#     age = int(age)
#     print('uraa')
# else:
#     raise Exception ('Invalid values!')
# if age < 18:
#     print(f'Acces Denied! Come again after {18 - age} age')
# else:
#     print('You can buy it!')    

#Логические операторы
# and -> логическое и 
# or -> лог или 
# not -> лог отрицание

# my_age = 20
# your_age = 18
# result = my_age == 20 and your_age == 19
# print(result)

# result = my_age == 21 or your_age == 18
# print(result)

# result = not my_age == 21 and not your_age == 19
# print(result)


# user = 'John'
# is_google_user = True
# is_github_user = True
# is_age_greater_21 = False
# user_coins = 9000

# либо юзер гугла или гитхаба и либо возраст выше 21, либо баки(8000)

# if (is_google_user or is_github_user) and (is_age_greater_21 or user_coins > 8000):
#     print(f'You can enter the system Mr/Mrs {user} !')
# else:
#     print('Sorry, you couldn\'t enter!')

#Операторы идентификации
# in -> проверяет наличие элемента внутри кого либо интерируемого обьекта(строки, cписки и т.д)
# is -> сравнивает ячейки памяти двух обьектов 
    # == -> сравнивает по значению
# is not - отрицательое сравнение ячеек памяти

# str1 = 'Hello world'
# print(str1)
# choice = input('Enter the symbol: ')

# if choice in str1:
#     print(f'The symbol: {choice} exists!')
# else:
#     print(f'The symbol: {choice} does not exist')
















