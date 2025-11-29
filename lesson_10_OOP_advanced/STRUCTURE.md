# 📂 Структура проекта Lesson 10

```
lesson_10_OOP_advanced/
│
├── 📄 INDEX.md                    ⭐ Полный индекс всех материалов
├── 🚀 QUICKSTART.md               ⭐ НАЧНИ ОТСЮДА! Быстрый старт
├── 📖 OOP_CHEATSHEET.md           ⭐ Шпаргалка по ООП
├── 📚 README.md                   Полная документация
├── 📡 api_examples.md             Примеры API запросов
├── 📋 STRUCTURE.md                Этот файл
│
├── 💎 oop_10.py                   ⭐ ОСНОВНОЙ ФАЙЛ с классами ООП
│   ├── Product (ABC)              Абстрактный базовый класс
│   ├── Smartphone                 Класс смартфона
│   ├── Laptop                     Класс ноутбука
│   ├── Tablet                     Класс планшета
│   ├── Cable                      Класс кабеля
│   ├── Accessory                  Класс аксессуара
│   ├── Inventory                  Управление инвентарем
│   ├── Order                      Класс заказа
│   ├── OrderItem                  Элемент заказа
│   └── demo_oop_principles()      Демонстрация работы
│
├── 🚀 fastapi_app.py              ⭐ FastAPI приложение
│   ├── ProductCreateRequest       Pydantic модели
│   ├── OrderCreateRequest         для валидации
│   ├── /products endpoints        CRUD для товаров
│   ├── /orders endpoints          CRUD для заказов
│   └── /stats endpoints           Статистика
│
├── 📦 __init__.py                 Пакет Python
│
└── 📁 homework/                   ⭐ ДОМАШНЕЕ ЗАДАНИЕ
    ├── 📝 homework_10.md          10 заданий для практики
    └── ✏️ homework_10.py          Файл для твоих решений
```

---

## 🎯 Что где находится?

### 📚 Документация

| Файл | Назначение | Когда читать |
|------|-----------|--------------|
| **INDEX.md** | Полный индекс материалов | Чтобы понять что где |
| **QUICKSTART.md** | Быстрый старт | **ПЕРВЫМ ДЕЛОМ** |
| **OOP_CHEATSHEET.md** | Шпаргалка по ООП | Как справочник |
| **README.md** | Полная документация | Для глубокого изучения |
| **api_examples.md** | Примеры API | При работе с API |
| **STRUCTURE.md** | Структура проекта | Этот файл |

---

### 💻 Код

| Файл | Строк | Назначение | Что внутри |
|------|-------|-----------|-----------|
| **oop_10.py** | ~700 | Основные классы | Все принципы ООП |
| **fastapi_app.py** | ~500 | FastAPI приложение | REST API endpoints |
| **homework_10.py** | ~100 | Твои решения | Шаблон с TODO |

---

### ✏️ Домашка

| Файл | Назначение |
|------|-----------|
| **homework_10.md** | 10 заданий + бонус |
| **homework_10.py** | Пиши код здесь |

---

## 🎓 Принципы ООП в файлах

### oop_10.py

```python
# ИНКАПСУЛЯЦИЯ (строки 70-140)
class Product:
    def __init__(self, name, price):
        self._name = name      # Приватное поле
        self._price = price
    
    @property                  # Геттер
    def price(self):
        return self._price
    
    @price.setter              # Сеттер с валидацией
    def price(self, value):
        if value <= 0:
            raise ValueError("Цена должна быть положительной")
        self._price = value

# АБСТРАКЦИЯ (строки 70-180)
from abc import ABC, abstractmethod

class Product(ABC):
    @abstractmethod
    def get_category(self):    # Абстрактный метод
        pass

# НАСЛЕДОВАНИЕ (строки 180-350)
class Smartphone(Product):     # Наследует Product
    def __init__(self, name, price, brand, ...):
        super().__init__(name, price)  # Вызов родителя
        self.brand = brand

# ПОЛИМОРФИЗМ (строки 180-350)
class Smartphone(Product):
    def get_warranty(self):
        return 12              # Своя реализация

class Laptop(Product):
    def get_warranty(self):
        return 24              # Другая реализация

# КОМПОЗИЦИЯ (строки 450-550)
class Order:
    def __init__(self):
        self.items = []        # Order содержит OrderItem
    
    def add_item(self, product, quantity):
        item = OrderItem(product, quantity)
        self.items.append(item)
```

---

### fastapi_app.py

```python
# ИНТЕГРАЦИЯ С FASTAPI
from fastapi import FastAPI
from lesson_10_OOP_advanced.oop_10 import (
    Inventory, Smartphone, Order
)

app = FastAPI()

# Глобальный инвентарь
inventory = Inventory()

# CRUD endpoints
@app.post("/products")
def create_product(req: ProductCreateRequest):
    product = create_product_from_request(req)
    inventory.add_product(product)
    return product.to_dict()

@app.get("/products")
def get_all_products():
    products = inventory.get_all_products()
    return [p.to_dict() for p in products]
```

---

## 🚀 Как использовать?

### 1. Изучение ООП

```bash
# Читай
cat lesson_10_OOP_advanced/OOP_CHEATSHEET.md

# Изучай
cat lesson_10_OOP_advanced/oop_10.py

# Запускай
source .venv/bin/activate
python lesson_10_OOP_advanced/oop_10.py
```

---

### 2. FastAPI приложение

```bash
# Запускай
source .venv/bin/activate
uvicorn lesson_10_OOP_advanced.fastapi_app:app --reload

# Открывай
open http://localhost:8000/docs
```

---

### 3. Домашнее задание

```bash
# Читай задания
cat lesson_10_OOP_advanced/homework/homework_10.md

# Пиши код
code lesson_10_OOP_advanced/homework/homework_10.py

# Тестируй
python lesson_10_OOP_advanced/homework/homework_10.py
```

---

## 📊 Статистика проекта

| Метрика | Значение |
|---------|----------|
| **Всего файлов** | 10 |
| **Строк кода (Python)** | ~1300 |
| **Строк документации** | ~1500 |
| **Классов** | 11 |
| **Методов** | ~80 |
| **API endpoints** | 15 |
| **Заданий** | 10 + бонус |

---

## 🎯 Классы в проекте

### Основные классы (oop_10.py)

```
Product (ABC)                    # Абстрактный базовый класс
├── _id: str                     # Приватные поля
├── _name: str
├── _price: float
├── _stock: int
├── get_category() [abstract]    # Абстрактные методы
├── get_specifications() [abstract]
├── get_warranty_period() [abstract]
├── get_final_price()            # Обычные методы
├── is_available()
├── add_stock()
└── reduce_stock()

Smartphone(Product)              # Наследник
├── _brand: str                  # Дополнительные поля
├── _model: str
├── _screen_size: float
├── _ram_gb: int
├── _storage_gb: int
├── _battery_mah: int
├── get_category() ✓             # Реализация абстрактных
├── get_specifications() ✓
├── get_warranty_period() ✓
└── get_battery_life_estimate()  # Свои методы

Laptop(Product)                  # Наследник
Tablet(Product)                  # Наследник
Cable(Product)                   # Наследник
Accessory(Product)               # Наследник

Inventory                        # Управление инвентарем
├── _products: Dict[str, Product]
├── add_product()
├── get_product()
├── remove_product()
├── get_all_products()
├── get_products_by_category()
├── search_products()
└── apply_discount_to_category()

Order                            # Заказ
├── _id: str
├── _customer_name: str
├── _customer_email: str
├── _items: List[OrderItem]      # Композиция
├── _status: OrderStatus
├── add_item()
├── get_total()
├── change_status()
└── cancel_order()

OrderItem                        # Элемент заказа
├── _product: Product            # Композиция
├── _quantity: int
├── _price_at_purchase: float
└── get_subtotal()
```

---

## 🔗 Связи между классами

```
┌─────────────┐
│   Product   │ (ABC)
│  (Abstract) │
└──────┬──────┘
       │
       ├──────────┬──────────┬──────────┬──────────┐
       │          │          │          │          │
   ┌───▼───┐  ┌──▼───┐  ┌───▼───┐  ┌──▼───┐  ┌───▼────┐
   │Smartphone│ │Laptop│ │Tablet │ │Cable │ │Accessory│
   └─────────┘ └──────┘ └───────┘ └──────┘ └─────────┘
       │
       │ используется в
       │
   ┌───▼────────┐
   │ Inventory  │
   │  (хранит)  │
   └────────────┘
       │
       │ используется в
       │
   ┌───▼────────┐
   │   Order    │
   │ (содержит) │
   └──────┬─────┘
          │
          │ содержит
          │
      ┌───▼────────┐
      │ OrderItem  │
      │  (ссылка)  │
      └────────────┘
```

---

## 💡 Быстрая навигация

### Хочу изучить ООП
→ **OOP_CHEATSHEET.md** + **oop_10.py**

### Хочу запустить API
→ **QUICKSTART.md** + **fastapi_app.py**

### Хочу делать домашку
→ **homework/homework_10.md** + **homework/homework_10.py**

### Хочу примеры API
→ **api_examples.md**

### Хочу понять структуру
→ **INDEX.md** + **STRUCTURE.md** (этот файл)

---

## 🎉 Готово!

Теперь ты знаешь где что находится!

**Начни с QUICKSTART.md и удачи! 🚀**
