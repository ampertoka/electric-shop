# 🎓 Шпаргалка по ООП - Python

## 📚 Основные принципы ООП

### 1. Инкапсуляция 🔒

**Что это:** Сокрытие внутренних данных объекта и предоставление доступа через методы.

**Зачем:** Защита данных от неправильного использования, контроль доступа.

```python
class Product:
    def __init__(self, name, price):
        self._name = name      # Приватное поле (по соглашению)
        self._price = price
    
    # Геттер
    @property
    def price(self):
        return self._price
    
    # Сеттер с валидацией
    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("Цена должна быть положительной")
        self._price = value

# Использование
product = Product("iPhone", 99990)
print(product.price)      # 99990 (через геттер)
product.price = 89990     # Устанавливаем через сеттер (с валидацией)
# product.price = -100    # ❌ ValueError!
```

**Ключевые моменты:**
- `_name` - приватное поле (по соглашению, не строгое)
- `@property` - создает геттер
- `@name.setter` - создает сеттер
- Валидация в сеттере защищает от некорректных данных

---

### 2. Наследование 🌳

**Что это:** Создание новых классов на основе существующих.

**Зачем:** Переиспользование кода, создание иерархии классов.

```python
# Базовый класс
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def get_info(self):
        return f"{self.name}: {self.price}₽"

# Наследник
class Smartphone(Product):
    def __init__(self, name, price, brand, ram_gb):
        super().__init__(name, price)  # Вызов конструктора родителя
        self.brand = brand
        self.ram_gb = ram_gb
    
    # Переопределение метода
    def get_info(self):
        base_info = super().get_info()  # Вызов метода родителя
        return f"{base_info}, {self.brand}, {self.ram_gb}GB RAM"

# Использование
phone = Smartphone("iPhone 15", 99990, "Apple", 8)
print(phone.get_info())  # iPhone 15: 99990₽, Apple, 8GB RAM
```

**Ключевые моменты:**
- `class Child(Parent):` - наследование
- `super()` - доступ к методам родителя
- Можно переопределять методы родителя
- Наследуются все поля и методы

---

### 3. Полиморфизм 🎭

**Что это:** Один интерфейс - разные реализации.

**Зачем:** Работа с разными объектами через единый интерфейс.

```python
class Product:
    def get_warranty(self):
        pass  # Базовая реализация

class Smartphone(Product):
    def get_warranty(self):
        return 12  # 12 месяцев

class Laptop(Product):
    def get_warranty(self):
        return 24  # 24 месяца

class Cable(Product):
    def get_warranty(self):
        return 6   # 6 месяцев

# Полиморфизм в действии
products = [
    Smartphone("iPhone", 99990),
    Laptop("MacBook", 189990),
    Cable("USB-C", 1990)
]

# Один и тот же код работает с разными типами
for product in products:
    print(f"{product.__class__.__name__}: {product.get_warranty()} мес.")

# Вывод:
# Smartphone: 12 мес.
# Laptop: 24 мес.
# Cable: 6 мес.
```

**Ключевые моменты:**
- Разные классы реализуют одинаковые методы по-своему
- Можно работать с объектами через общий интерфейс
- Не нужно знать конкретный тип объекта

---

### 4. Абстракция 🎨

**Что это:** Определение интерфейса без реализации.

**Зачем:** Гарантия, что все наследники реализуют нужные методы.

```python
from abc import ABC, abstractmethod

# Абстрактный класс
class Product(ABC):
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    # Абстрактный метод (должен быть реализован в наследниках)
    @abstractmethod
    def get_category(self):
        pass
    
    @abstractmethod
    def get_warranty(self):
        pass
    
    # Обычный метод (может быть использован как есть)
    def get_info(self):
        return f"{self.name}: {self.price}₽"

# Конкретный класс
class Smartphone(Product):
    # ОБЯЗАТЕЛЬНО реализуем абстрактные методы
    def get_category(self):
        return "smartphone"
    
    def get_warranty(self):
        return 12

# Использование
# product = Product("Test", 100)  # ❌ Ошибка! Нельзя создать абстрактный класс
phone = Smartphone("iPhone", 99990)  # ✅ OK
print(phone.get_category())  # smartphone
```

**Ключевые моменты:**
- `ABC` - базовый класс для абстракций
- `@abstractmethod` - помечает метод как абстрактный
- Нельзя создать экземпляр абстрактного класса
- Наследники обязаны реализовать все абстрактные методы

---

## 🔧 Дополнительные концепции

### Композиция 🧩

**Что это:** Объект содержит другие объекты.

```python
class OrderItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity
    
    def get_subtotal(self):
        return self.product.price * self.quantity

class Order:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.items = []  # Композиция: Order содержит OrderItem
    
    def add_item(self, product, quantity):
        item = OrderItem(product, quantity)
        self.items.append(item)
    
    def get_total(self):
        return sum(item.get_subtotal() for item in self.items)

# Использование
order = Order("Иван Иванов")
order.add_item(phone, 2)
order.add_item(cable, 3)
print(order.get_total())
```

---

### Магические методы ✨

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    # Строковое представление для пользователя
    def __str__(self):
        return f"{self.name}: {self.price}₽"
    
    # Строковое представление для разработчика
    def __repr__(self):
        return f"Product(name='{self.name}', price={self.price})"
    
    # Сравнение
    def __eq__(self, other):
        return self.price == other.price
    
    def __lt__(self, other):
        return self.price < other.price
    
    # Длина (если применимо)
    def __len__(self):
        return len(self.name)

# Использование
p1 = Product("iPhone", 99990)
p2 = Product("Samsung", 79990)

print(p1)           # iPhone: 99990₽ (вызывает __str__)
print(repr(p1))     # Product(name='iPhone', price=99990) (вызывает __repr__)
print(p1 == p2)     # False (вызывает __eq__)
print(p1 > p2)      # True (вызывает __lt__)
print(len(p1))      # 6 (вызывает __len__)
```

**Популярные магические методы:**
- `__init__` - конструктор
- `__str__` - строковое представление
- `__repr__` - техническое представление
- `__eq__`, `__lt__`, `__gt__` - сравнение
- `__len__` - длина
- `__getitem__`, `__setitem__` - доступ по индексу
- `__call__` - вызов как функции

---

### Классовые переменные и методы 📊

```python
class Product:
    # Классовая переменная (общая для всех экземпляров)
    _id_counter = 0
    tax_rate = 0.20  # 20% налог
    
    def __init__(self, name, price):
        # Увеличиваем счетчик для каждого нового товара
        Product._id_counter += 1
        self.id = Product._id_counter
        self.name = name
        self.price = price
    
    # Метод экземпляра (работает с конкретным объектом)
    def get_price_with_tax(self):
        return self.price * (1 + Product.tax_rate)
    
    # Классовый метод (работает с классом, не с экземпляром)
    @classmethod
    def set_tax_rate(cls, rate):
        cls.tax_rate = rate
    
    # Статический метод (не зависит ни от класса, ни от экземпляра)
    @staticmethod
    def is_valid_price(price):
        return price > 0

# Использование
p1 = Product("iPhone", 100000)
p2 = Product("Samsung", 80000)

print(p1.id)  # 1
print(p2.id)  # 2

# Изменяем налог для всех товаров
Product.set_tax_rate(0.15)

print(p1.get_price_with_tax())  # 115000
print(p2.get_price_with_tax())  # 92000

# Статический метод
print(Product.is_valid_price(100))   # True
print(Product.is_valid_price(-100))  # False
```

---

### Множественное наследование 🔀

```python
class Discountable:
    def apply_discount(self, percent):
        self.price *= (1 - percent / 100)

class Reviewable:
    def __init__(self):
        self.reviews = []
    
    def add_review(self, rating, comment):
        self.reviews.append({"rating": rating, "comment": comment})

# Множественное наследование
class Product(Discountable, Reviewable):
    def __init__(self, name, price):
        Reviewable.__init__(self)  # Инициализируем Reviewable
        self.name = name
        self.price = price

# Использование
product = Product("iPhone", 100000)
product.apply_discount(10)  # Скидка 10%
product.add_review(5, "Отлично!")
print(product.price)  # 90000
print(product.reviews)  # [{"rating": 5, "comment": "Отлично!"}]
```

---

## 🎯 SOLID принципы (кратко)

### S - Single Responsibility (Единственная ответственность)
Класс должен иметь только одну причину для изменения.

```python
# ❌ Плохо: класс делает слишком много
class Product:
    def save_to_database(self): pass
    def send_email(self): pass
    def generate_report(self): pass

# ✅ Хорошо: разделяем ответственность
class Product: pass
class ProductRepository:
    def save(self, product): pass
class EmailService:
    def send(self, email): pass
class ReportGenerator:
    def generate(self, product): pass
```

### O - Open/Closed (Открыт для расширения, закрыт для изменения)
Можно добавлять новую функциональность без изменения существующего кода.

```python
# ✅ Хорошо: добавляем новые типы без изменения базового класса
class Product(ABC):
    @abstractmethod
    def get_warranty(self): pass

class Smartphone(Product):
    def get_warranty(self): return 12

class Laptop(Product):
    def get_warranty(self): return 24
```

### L - Liskov Substitution (Подстановка Лисков)
Объекты подклассов должны вести себя так же, как объекты базового класса.

### I - Interface Segregation (Разделение интерфейсов)
Много специализированных интерфейсов лучше, чем один универсальный.

### D - Dependency Inversion (Инверсия зависимостей)
Зависимость от абстракций, а не от конкретных реализаций.

---

## 💡 Лучшие практики

1. **Используй инкапсуляцию** - делай поля приватными, предоставляй доступ через методы
2. **Не злоупотребляй наследованием** - иногда композиция лучше
3. **Следуй принципу DRY** (Don't Repeat Yourself) - не повторяйся
4. **Пиши docstrings** - документируй классы и методы
5. **Используй type hints** - указывай типы для лучшей читаемости
6. **Тестируй код** - пиши unit-тесты для классов
7. **Следуй PEP 8** - стандарт оформления кода Python

---

## 🚀 Быстрая справка

```python
# Создание класса
class MyClass:
    pass

# Наследование
class Child(Parent):
    pass

# Множественное наследование
class Child(Parent1, Parent2):
    pass

# Абстрактный класс
from abc import ABC, abstractmethod
class MyClass(ABC):
    @abstractmethod
    def my_method(self):
        pass

# Property (геттер/сеттер)
@property
def name(self):
    return self._name

@name.setter
def name(self, value):
    self._name = value

# Классовый метод
@classmethod
def my_method(cls):
    pass

# Статический метод
@staticmethod
def my_method():
    pass

# Вызов родительского метода
super().parent_method()

# Проверка типа
isinstance(obj, MyClass)

# Проверка наследования
issubclass(ChildClass, ParentClass)
```

---

**Используй эту шпаргалку как справочник! 📖**
