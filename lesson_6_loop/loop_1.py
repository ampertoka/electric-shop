# java
# for, while, foreach
# python
# for (for + foreach), while

# ПРИРОДА ЦИКЛОВ И ПОЧЕМУ СОЗДАНЫ - РУТИНА ОДНИХ И ТЕХ ЖЕ ДЕЙСТВИЙ
i = 0
print(i)
i = i + 1
print(i)

# КОГДА НЕТ ТОЧНОЙ ПОСЛЕДОВАТЕЛЬНОСТИ, НО ЕСТЬ ТОЧНОЕ УСЛОВИЕ РАБОТЫ ЦИКЛА
# НО НУЖНО ЧЕТКО ПЛАНИРОВАТЬ ВЫХОД ЧТОБ ЦИКЛ НЕ СТАЛ БЕСКОНЕЧНЫМ - ЭТО ПЛОХО
# i = 0
# while 1 > 0:
#     print(i)
#     i += 1
# В ПИТОНЕ НЕТ ПОСТУСЛОВИЯ ЦИКЛА

# КОГДА ЕСТЬ ПОСЛЕДОВАТЕЛЬНОСТЬ

# ЕСЛИ В range(2) передать число то он построит ГЕНЕРАТОР
# из последовательности чисел ОТ 0 ДО переданного числа - 1:
# то есть тут будет (0, 1), то есть как в slice list: lst_1[:2]
for i in range(0, 5, 1):
    print(i)

# ЧЕМ КРУТ RANGE
# ТО ЖЕ САМОЕ:
for i in range(5):
    print(i)

tpl_1 = tuple((1, 2, 3))
lst_1 = [1, 2, 3]

for i in tpl_1:
    print(f'tpl {i}')

for i in lst_1:
    print(f'lst {i}')

dct_1 = {'k1': 'v1', 'k2': 'v2'}

for i in dct_1.keys():
    print(f'dct_k: {i}')
# ТО ЖЕ САМОЕ ПО КЛЮЧАМ
for i in dct_1:
    print(i)

for i in dct_1.values():
    print(f'dct_k: {i}')

print(dct_1.items())
# РАБОТАЕТ КАК *args в функциях (unpacking)
for k, v in dct_1.items():
    print(f'dct_k = {k}, dct_v = {v}')

lst_1 = [1, 2, 3]
# ТАКЖЕ КАК RANGE создает ПОСЛЕДОВАТЕЛЬНОСТЬ, но допольнительно создает ЕЩЕ
# ПОСЛЕДОВТАЕЛЬНОСТь индексов элементов и связывает обе последовательности
for i, v in enumerate(lst_1):
    print(f'lst_idx = {i}, lst_val = {v}')

lst_2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# ВЛОЖЕННЫЕ ЦИКЛЫ
for idx, lst_inner in enumerate(lst_2):
    print(f'{idx}. lst_inner: {lst_inner}')

    for elem in lst_inner:
        print(f' - {elem}')

# ОСТАНОВКА ЦИКЛА
for lst_inner in lst_2:
    print(f'{lst_inner}')
    break

for idx, lst_inner in enumerate(lst_2):
    print(f'{idx}. lst_inner: {lst_inner}')

    for elem in lst_inner:
        print(f' - {elem}')
        # РАБОТАЕТ ТОЛЬКО НА ТОТ ЦИКЛ ВНУТРИ КОТОРОГО ПРИПИСАН
        break

lst_3 = [1, 2, 3]
# ПЕРЕХОД К СЛЕДУЮЩЕМУ ЭЛЕМЕНТУ (ШАГУ) ЦИКЛА - continue
for elem in lst_3:

    if elem == 2:
        # РАБОТАЕТ ТОЛЬКО НА ТОТ ЦИКЛ ВНУТРИ КОТОРОГО ПРИПИСАН
        continue

    print(f'{elem}')
