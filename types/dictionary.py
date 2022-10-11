# Dict() - Словарь -> упорядочная коллекция элементов.(Начиная с новой версии python(3.7) -> ordered)
# Каждый элемент в словаре хранится в виде праы: {ключ: значение}
# Ассоциативный массив, hash tables, object(js), structire == dictionary(py)

# Ключами могут выступать только неизменяемые типы данных и в словарях хранятся уникальные ключи.Тогда как значениями могут выступать любые типы данных.

# {'name':'John Snow', 'age': 18, 'number': 777999}

# thisdict = {
#     'brand': 'Ford',
#     'model': 'Mustang',
#     'year': 1967
# }

# print(thisdict) 
# print(type(thisdict))
# print(thisdict['model'])
# print(thisdict['year'])



# a = dict()
# b = {}
# print(a, b)
# print(type(a))
# print(type(b))

# dict_ = [('key1', 'value1'), ('key2', 'value2')]
# dict__= dict(dict_)
# print(dict__)

# -----------------------------------------------------------------------------------------
# print(dir(dict))

# items, keys, values

# user_info = {
#     'first_name': 'John',
#     'lat_name': 'Snow',
#     'age': 24,
#     'email': 'johnsnow@gmail.com',
#     'role': 'admin',


# print(user_info.items())
# print()
# print(user_info.keys())
# print()
# print(user_info.values())

# for value in user_info.values():
#     print(value)
# print(user_info)
# for key, value in user_info.items():
#     print(f'key: {key}, value: {value}')
# # 
# ls = list(user_info.items())
# print(ls[0][1])

# Изменения элементов в словаре

# dict_ = {'name': 'Jack', 'age': 24}

# print(dict_['name'])
# dict_['address'] = 'WinterFell'
# # dict_['name'] = 'John'
# print(dict_)

# dict_.update({'name': 'John', 'address': 'WinterFell'})
# print(dict_)


# ----------------------------------------------------------------------------------------------------


# Создание - fromkeys
# dict_ = {}
# ls = list(range(1, 101))
# new_dict = dict_.fromkeys(ls, 'values')
# print(new_dict)

# ---------------------------------------------------------------------
# get
# dict_ = {1: 'Pizza', 2: 'Burger', 3: 'Steak'}
# print(dict_.get(2))
# print(dict_[2])

# setdefault - работает также, как и get, но если нет такого ключа, то он создает новую пару значений из этого ключа

# dict_ = {'name': 'Eddard', 'last_name': 'Stark'}
# print(dict_)
# print(dict_.setdefault('age', 38))
# print(dict_)

# удаление элементов
# pop, popitem

# pop(<key>) - удаляет пару по ключу

# dict_ = {'name': 'John', 'last_name': 'Snow'}

# removed = dict_.pop('name')
# print(dict_)
# print(removed)

# popitem() - удаляет последнюю пару

# dict_ = {'name': 'Joehn', 'last_name': 'Snow'}

# removed = dict_.popitem()
# print(dict_)
# # print(removed)







