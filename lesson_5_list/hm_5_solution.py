# Урок 5 — Списки: эталонное решение

# 1. База — индексация, замена, длина
nums = [1, 2, 3]
print(nums[0], nums[-1])  # первый и последний элементы
nums[-1] = 10
print(len(nums))  # длина списка
print(nums)
# 2. append / pop / remove
colors = ["red", "green"]
colors.append("blue")
last_color = colors.pop()  # удалит последний ("blue")
colors.remove("green")  # удалит значение "green"
print(colors, last_color)

# 3. Вставка и замена значений
a = [1, 2, 3, 4]
a[2] = 99  # замена по индексу
a.insert(1, 100)  # вставка со сдвигом вправо
print(a)

# 4. Сортировка чисел и строк
nums = [3, 1, 5, 2, 4]
nums.sort()  # по возрастанию
print("по возрастанию:", nums)
nums.sort(reverse=True)  # по убыванию
print("по убыванию:", nums)

words = ["aac", "aab", "ab", "az"]
words.sort()
print(words)

# 5. Объединение списков: for+append и extend
base = [1, 2, 3]
b = [4, 5]
# способ 1 — через цикл
merged1 = base.copy()
for x in b:
    merged1.append(x)
# способ 2 — через extend
merged2 = base.copy()
merged2.extend(b)
print(merged1, merged2, merged1 == merged2)

# 6. Подсчет и поиск
vals = [1, 1, 2, 3, 3]
print(vals.count(1))  # сколько раз встречается 1
arr = [1, 2, 3, 4, 2]
print(arr.index(2))  # индекс первого вхождения 2
if 10 in arr:
    print(arr.index(10))
else:
    print("не найдено")

# 7. Срезы: получение и удаление
arr = [1, 2, 3, 4, 5]
sub_arr = arr[1:3]
del arr[1:3]
print(sub_arr, arr)

# 8. Шаги срезов
x = [1, 2, 3, 4, 5, 6, 7, 8]
s1 = x[0:len(x):3]
s2 = x[::3]
print(s1, s2, s1 == s2)

# 9. Копирование и мини‑практика
data = [3, 1, 5, 2, 4]
data_copy = data.copy()
data_copy.clear()
print(data, data_copy)  # убеждаемся, что исходный не изменился

# операции над исходным data
data[0] = 10
data.insert(0, 0)
if 5 in data:
    data.remove(5)
data.extend([8, 1.5])
data.sort(reverse=True)
print(data)

top3 = data[:3]
print(top3)
