# СОЗДАНИЕ СПИСКА
lst_1 = [1, 2, 3]
# СОЗДАНИЕ СПИСКА АНАЛОГ
lis_2 = list((1, 2, 3))
# СОЗДАНИЕ КОРТЕЖА
tuple_1 = (1, 2, 3)
# СОЗДАНИЕ КОРТЕЖА АНАЛОГ
tuple_2 = tuple((1, 2, 3))

# СПИСОК МОЖЕТ СОДЕРЖАТЬ РАЗНЫЕ ТИПЫ ЭЛЕМЕНТОВ
lst_3 = [1, 'str', {'k': 'v'}, [1, 2], (3, 4), None, False, object]
# print(lst_3)
for elem in lst_3:
    # print(elem)
    pass

# ОБРАЩЕНИЕ ПО ИНДЕКСУ
lst_3[-1] = None

# КОПИРОВАНИЕ И ОЧИСТКА КАК СЛВОАРИ
lst_4 = lst_3.copy()
lst_4.clear()

# print(lst_4)
# print(lst_3)

# ДОБАВЛЕНИ В КОНЕЦ
lst_5 = [3, 4]
lst_5.append(5)

# print(lst_5)
# УДАЛЕНИЕ ИЗ КОНЦА
last_elem = lst_5.pop()
# print(last_elem)
# print(lst_5)

lst_6 = [1, 2, 3, 4, 5]
# print(lst_6)
lst_6.remove(3)
# print(lst_6)

lst_7 = [1, 2, 3, 4, 5]
# print(lst_7)
lst_7[2] = 10
# ДОБАВЛЕНИЕ ПО УКАЗАННОМУ ИНДЕКСУ СО СДВИГОМ ВПРАВО
lst_7.insert(2, 10)
# print(lst_7)

lst_8 = [3, 1, 5, 2, 4]
# СОРТИРОВКА ВОЗРАСТАНИЕ
lst_8.sort()
# СОРТИРОВКА УБЫВАНИЕ
lst_8.sort(reverse=True)
# print(lst_8)

# lst_8.reverse()
# prin`t(lst_8)

lst_8 = ['aac', 'aab', 'ab', 'az']
# СОРТИРОВКА ВОЗРАСТАНИЕ СТРОКИ
lst_8.sort()
# print(lst_8)

# СОРТИРОВКА ВСЕ ЧИСЛА (ДРОБНЫЕ ЦЕЛЫЕ)
lst_8 = [1, 1.6, 2.3, 2]
lst_8.sort(reverse=True)
# print(lst_8)

lst_9 = [1, 2, 3, 4, 5]
# аналог у словаря some_dict.update({})

# АНАЛОГ 1
for elem in lst_8:
    lst_9.append(elem)

# АНАЛОГ 2
# РАСШИРЕНИЕ СПИСКА ДРУГИМ СПИСКОМ ИЛИ КОРТЕЖЕМ
lst_9.extend(lst_8)
# print(lst_9)

# ПОДСЧЕТ ЭЛЕАМЕНТОВ
lst_10 = [1, 1, 2, 3, 3]
count_1 = lst_10.count(0)
# print(count_1)

lst_11 = [1, 2, 3, 4, 2]
# ПОИСК ИНДЕКСА ПО ЗНАЧЕНИЕ
lst_11_2_idx = lst_11.index(2)
# print(lst_11_2_idx)

# СРЕЗЫ
lst_12 = lst_11[1:3]
# print(lst_12)

# СРЕЗЫ УДАМЛЕНИЕ
del lst_11[1:3]
# print(lst_11)

# ДЛИНА СПИСКА
# print(len(lst_11))

lst_13 = [1, 2, 3, 4, 5, 6, 7, 8]

# lst_13[0:9:1] АНАЛОГИЧЕН lst_13[0:9]
# ШАГИ
lst_14 = lst_13[0:len(lst_13):3]
print(lst_14)
# ШАГИ АНАЛОГ
lst_15 = lst_13[::3]
print(lst_15)
