# 1) Базовая склейка и индексы
#
# - Объяви переменные `name='egor'`, `surname='zubachenko'`.
# - Создай `full_name` тремя способами: конкатенацией, f-строкой и через `.format()`.
# - Выведи первый и последний символ строки `full_name`, а также срез первых 4 символов.
# name = 'egor'
# surname = 'zubachenko'
# full_name = name + " "+ surname
# print(full_name)
# full_name = f'{name} {surname}'
# print(full_name)
# full_name = "{} {}".format(name, surname)
# print(full_name)
# print(full_name[0])
# print(full_name[-1])
# print(full_name[0:4])


# 2) Регистры и подсчет
#
# - Для строки `s = 'hello, world'` выведи: `s.upper()`, `s.lower()`, `s.title()`.
# - Посчитай количество букв `l` через `count`.
# - Найди первую позицию `o` через `find` и индекс через `index` (обработай возможную ошибку).
# s = 'hello, world'
# print(s.upper())
# print(s.lower())
# print(s.title())
# print(s.count('l'))
# print(s.find('o'))
# print(s.index('o'))


# 3) Обработка пробелов и сплит
#
# - Пользователь вводит строку с пробелами по краям. Убери пробелы `strip()`.
# - Разбей строку на слова `split()` и выведи список и количество слов.
# - Склей обратно через `';'.join(words)` и выведи результат.
# a = input().strip().split()
# print(a, len(a))
# print(';'.join(a))


# 4) Заполнение и выравнивание значений
#
# - Дано: `order_id = '7'`, `amount = 3.14159`.
# - Выведи номер заказа с нулями слева до длины 6 через `zfill`.
# - Сформируй строку старым стилем: `Int:%d Float:%.2f Width:%10s Left:%-10s Zero:%05d Percent:100%%` подставив свои
#   значения.
# order_id = '7'.zfill(6)
# print(order_id)
# amount = 3.14159
# print("Int:%d Float:%.2f Width:%10s Left:%-10s Zero:%05d Percent:100%%" % (4, amount, order_id, 6, 9))


# 5) Проверки и замены
#
# - Дано: `name = 'egoreeeeeee'`.
# - Пока в `name` есть символ `e`, заменяй все `e` на пустую строку через `replace` и выводи промежуточные результаты.
# - В конце выведи итоговое значение и сообщения, начинается ли изначальная строка с `'egor'` и заканчивается ли на
#   `'ch'`.
# name = 'egoreeeeeee'
# while 'e' in name:
#     name = name.replace('e', '')
#     print(name)
# print(name.startswith('egor'))
# print(name.endswith('ch'))


# 6) Разбор CSV-строки и форматированный вывод
#
# - Дано: `tech = 'python,fastapi,django'`.
# - Разбей в список и в цикле `for` выведи каждую технологию в формате: `Технология: <ИМЯ_В_ВЕРХНЕМ_РЕГИСТРЕ>`.
# - Итоговый список собери обратно в строку через запятую, но имена сделай в `title()`.
# tech = 'python,fastapi,django'.split()
# for i in tech:
#     print(f'Технология: {i.upper()}')
# print(', '.join(tech).title())


# 7) Валидация и числовые строки
#
# - Дано: `num_str = '00123'`.
# - Преобразуй в `int`, увеличь на 10, снова сделай строку и дополни слева нулями до длины 6 через `zfill`.
# - Проверь разные строки на `isalpha()` и `isdigit()` и коротко выведи результаты в одну строку через `';'.join(...)`.
# num_str = int('00123') + 10
# num_str = str(num_str).zfill(6)
# print(num_str)
# print(num_str.isalpha())
# print(num_str.isdigit())
# print(';'.join([num_str]))


# 8) Мини-CSV ФИО
#
# - Дано: список `['egor', 'zubachenko', 'maksimovich']`.
# - Собери CSV-строку через `join`, выведи варианты: `upper`, `lower`, `title`.
# - Найди позицию первой буквы `'a'` через `find` и количество всех `'e'` через `count`.
# lst = ['egor', 'zubachenko', 'maksimovich']
# full_name = ','.join(lst)
# print(full_name.upper())
# print(full_name.lower())
# print(full_name.title())
# print(full_name.find('a'))
# print(full_name.count('e'))


# 9) Комбинированный отчёт
#
# - Пользователь вводит ФИО с лишними пробелами и разными регистрами, например:
# `'   eGoR, zUbAcHeNkO ,  MaKsImOvIcH  '`.
#   Используй `strip`, `split` по запятой и `strip` для каждого элемента.
# - Приведи каждую часть к `title()`. Собери CSV-строку через `join`.
# - Сформируй три строки одним выражением каждая: через f-строку,
# через `.format`, через старое `%`-форматирование.
#   Вставь:
# - Порядковый номер (дополненный нулями до 5: `zfill(5)`),
# - Полное имя (CSV и пробельный вариант с пробелом между словами),
# - Кол-во букв `'o'` и позицию первой `'a'`.
# - Выведи все три строки и убедись, что содержимое логически совпадает.
fio = input().strip().title().split(',')# ПоторАшкиН,СергеЙ,    МиХайлоВич

'''
   eGoR, zUbAcHeNkO ,  MaKsImOvIcH  
'''
# print(fio)
# idx = fio.index('Egor')
# print(idx)
# elem = fio[idx]
# print(elem)
# fio[idx] = 'asfasfasdada'

# самое запутанное - нет смысла делать 'in fio' если хотим обращаться по индексу
for elem in fio:
    elem_idx = fio.index(elem)
    fio[elem_idx] = elem.strip()

# уже лучше, но все равно in fio.
# применять когда очень хочется генератор по элементам
for idx, elem in enumerate(fio):
    fio[idx] = elem.strip()

# классический цилк по индексам. самое понятное решение для любого языка прогр.
for i in range(len(fio)):
    fio[i] = fio[i].strip()

print(fio)
fio_str = ','.join(fio)
print(fio_str)
num = '1'.zfill(5)
