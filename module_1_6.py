# 2. Работа со словарями:
#- Создайте переменную my_dict и присвойте ей словарь из нескольких пар ключ-значение.
# Например: Имя(str)-Год рождения(int).
# Выведите на экран словарь my_dict.

# Выведите на экран одно значение по существующему ключу, одно по отсутствующему
# из словаря my_dict без ошибки.

# Добавьте ещё две произвольные пары того же формата в словарь my_dict.

# Удалите одну из пар в словаре по существующему ключу из словаря my_dict и
#  выведите значение из этой пары на экран.
#- Выведите на экран словарь my_dict.

my_dict={'Olga': 1976,'Vadim': 1986,'Vlad': 1980}
print(my_dict)
print(my_dict.get('Olga','Max'))
print(my_dict.update({'Eva': 2005,'Diana': 2010}))
print(my_dict)
del(my_dict['Eva'])
print(my_dict)

# 3. Работа с множествами:
#   - Создайте переменную my_set и присвойте ей множество, состоящее из разных
#     типов данных с повторяющимися значениями.
#   - Выведите на экран множество my_set (должны отобразиться только уникальные значения).
#   - Добавьте 2 произвольных элемента в множество my_set, которых ещё нет.
#   - Удалите один любой элемент из множества my_set.
#   - Выведите на экран измененное множество my_set.

my_set= {1,100,10001,100,52,'Olga',1976,'Vadim',1986,'Vlad'}
print(my_set)
my_set.update([33,44])
print(my_set)
my_set.remove(33)
print(my_set)
