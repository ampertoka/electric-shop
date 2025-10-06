# Урок 4 — Словари: простое эталонное решение

# 1–2. База
student = {"name": "Serg", "age": 36, "city": "Podolsk"}
print(student["name"])            # вывод имени
student["age"] = 25                # изменить возраст
student["course"] = "Python"      # добавить ключ course
student.pop("city")                 # удалить city
student.clear()                      # полностью очистить словарь

# 3. Книги
books = {"1984": "Orwell", "Hamlet": "Shakespeare"}
print(books.get("1984"))                       # автор 1984
print(books.get("The Hobbit", "Такой книги нет"))  # книги нет
books.update({"Idiot": "Dostoevsky"})
if "Idiot" in books:
    print(books["Idiot"])  # печать автора из словаря
else:
    print("Книга не найдена")

# 4. Товары
products = {"apple": 50, "banana": 30, "milk": 70}
print(list(products.keys()))    # все ключи
print(list(products.values()))  # все значения
print(list(products.items()))   # все пары

# 5. Вложенные словари — компания
company = {
    "emp1": {"name": "Serg", "position": "dev"},
    "emp2": {"name": "Max", "position": "manager"},
    "emp3": {"name": "Egor", "position": "tester"}
}
print(company["emp2"]["name"])          # имя второго сотрудника
company["emp3"]["position"] = "senior tester"
company["emp4"] = {"name": "John", "position": "dev"}

# 6. Корзина
shop_cart = {"apple": 3, "banana": 2}
shop_cart["milk"] = 1
shop_cart["apple"] = 5
for item, qty in shop_cart.items():
    print(f"Товар: {item}, Кол-во: {qty}")
