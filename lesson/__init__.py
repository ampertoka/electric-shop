student = {'name':'serg', 'age': 36, 'city':'podolsk'}
print(student['name'])
student['age'] = 25
student['course'] = 'Python'
cityNew = student.pop('city')
print(cityNew)
student.clear()


books = {"1984": "Orwell", "Hamlet": "Shakespeare"}
author1984 = books.get("1984")
print(author1984)
peint(student.get("Oskar", "Такой книги нет"))
student.update({
    "Преступление и наказание": "Федор Достоевский"
})

if "Idiot" in student:
    print("Федор Достоевский")
else:
    print("Книга не найдена")

products = {"apple": 50, "banana": 30, "milk": 70}
print(products.keys())
print(products.values())
print(products.items())

company = {
    "emp1": {"name": "Serg", "position": "dev"},
    "emp2": {"name": "Max", "position": "manager"},
    "emp3": {"name": "Egor", "position": "tester"}
}

emp2Name = company["emp2"]["name"]
print(emp2Name)

company["emp3"]["position"] = "senior tester"
company["emp4"] = {"name": "djon", "position": "dev"}

shop_cart = {"apple": 3, "banana": 2}
shop_cart["milk"] = 1
shop_cart["apple"] = 5
shop_cart_items = shop_cart.items()
print(shop_cart_items)


