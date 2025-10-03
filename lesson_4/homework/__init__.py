student = {'name':'serg', 'age': 36, 'city':'podolsk'}

student['age'] = 25
student['course'] = 'Python'
cityNew = student.pop('city', '')
cityNew_ = student.pop('city', '')

student.clear()


books = {"1984": "Orwell", "Hamlet": "Shakespeare"}
author1984 = books.get("1984")
print(author1984)
print(books.get("Oskar", "Такой книги нет"))
print(books)
books['Преступление и наказание'] = '123123'
books.update({
    "Idiot": "Федор Достоевский",
    "Преступление и наказание": "Федор Достоевский",
})
books['Idiot'] = "Федор Достоевский"
books['Преступление и наказание'] = "Федор Достоевский Достоевский"
books.popitem()
print(books)




if "Idiot" in books:
    print(books['Idiot'])
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

shop_cart_2 = shop_cart.copy()
shop_cart_2.clear()

tuple()
str_ = 'asdadad'

for item, q in shop_cart.items():
    print(f'Товар: {item}, Кол-во: {q}')

# много по памяти - плохо/
list_1 = [x for x in range(1000000000000000000)]
# мало по памяти - хорошо
gen_1 = (x for x in range(1000000000000000000))
