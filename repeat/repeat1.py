# Даны две переменные s1 = "America" и s2 = "Japan".  Выведите новую строку в который будут записаны первый, средний и последний элемент двух переменных.  Необходимо использовать срезы.
# Вывод: "AJrpan".

# s1 = "America"
# s2 = "Japan"
# # res = '1s1-1s2-ms1-ms2-ls1-ls2'
# # kol / 2 = avr_middle
# first_s1 = s1[0]
# first_s2 = s2[0]
# middle_s1 = s1[len(s1)// 2]
# middle_s2 = s2[len(s2) // 2]
# last_s1 = s1[-1]
# last_s2 = s2[-1]
# res = first_s1 + first_s2 + middle_s1 +middle_s2 + last_s1 + last_s2
# print(res)


# 11. Объявите переменную string значением которой будет несколько хэштегов, разделённых символом '#'. Разделите их в отдельные строки.
# Например: #makers#bootcamp#программирование#it#курсы 
# Вывод: ['makers', 'bootcamp', 'программирование', 'it', 'курсы']

# str1 = '#makers#bootcamp#программирование#it#курсы '
# res = str1[1:].split('#')
# print(res) 

# dano -> [1--100]
# число / 3 -> fu
# число / 5 -> ba 
# число /3, /5 -> fuba
# вывод: 3 fu 
#        5 ba 
#        15 fuba
# for number in range(1, 100):
#     # print(number)
#     if  number % 3 == 0 and number % 5 == 0:
#         print(f'{number} fu')
#     elif number % 5 == 0:
#         print(f'{number} fu')
#     elif number % 3 == 0:
#         print(f'{number} fuba')
    







# string = 'корова любит молоко'
# result = string.replace('о', 'ж', 2 )






