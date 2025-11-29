# 🚀 Быстрый старт - Урок 10

## 📖 Что здесь?

Полноценное приложение магазина электронной техники с демонстрацией **всех принципов ООП**:
- ✅ **Инкапсуляция** - приватные поля, геттеры/сеттеры
- ✅ **Наследование** - иерархия классов Product → Smartphone, Laptop, etc.
- ✅ **Полиморфизм** - один интерфейс, разные реализации
- ✅ **Абстракция** - абстрактные классы (ABC)
- ✅ **Композиция** - Order содержит OrderItem
- ✅ **Интеграция с FastAPI** - готовое REST API

---

## 🎯 Три способа использования

### 1️⃣ Демонстрация ООП (консоль)

```bash
# Активируй виртуальное окружение
source .venv/bin/activate

# Запусти демонстрацию
python lesson_10_OOP_advanced/oop_10.py
```

**Что увидишь:**
- Создание товаров разных типов
- Полиморфизм в действии
- Работу с инвентарем
- Создание заказов
- Применение скидок

---

### 2️⃣ FastAPI приложение (API)

```bash
# Активируй виртуальное окружение
source .venv/bin/activate

# Запусти сервер
uvicorn lesson_10_OOP_advanced.fastapi_app:app --reload
```

**Открой в браузере:**
- 📚 **Swagger UI**: http://localhost:8000/docs
- 📖 **ReDoc**: http://localhost:8000/redoc
- 🏠 **API**: http://localhost:8000

**Что можно делать:**
- Создавать товары через API
- Управлять инвентарем
- Создавать заказы
- Получать статистику
- Применять скидки

---

### 3️⃣ Домашнее задание (практика)

```bash
# Открой файл для редактирования
code lesson_10_OOP_advanced/homework/homework_10.py

# Читай задания
cat lesson_10_OOP_advanced/homework/homework_10.md

# Запускай свои решения
python lesson_10_OOP_advanced/homework/homework_10.py
```

---

## 📁 Структура файлов

```
lesson_10_OOP_advanced/
├── oop_10.py              # ⭐ Основные классы с ООП
├── fastapi_app.py         # 🚀 FastAPI приложение
├── README.md              # 📚 Полная документация
├── QUICKSTART.md          # 🚀 Этот файл
├── api_examples.md        # 📡 Примеры API запросов
└── homework/
    ├── homework_10.md     # 📝 Задания
    └── homework_10.py     # ✏️ Твои решения
```

---

## 🎓 Основные классы

### Product (абстрактный)
Базовый класс для всех товаров:
```python
from lesson_10_OOP_advanced.oop_10 import Product

# Нельзя создать напрямую (абстрактный класс)
# product = Product(...)  # ❌ Ошибка!
```

### Smartphone, Laptop, Tablet, Cable, Accessory
Конкретные классы товаров:
```python
from lesson_10_OOP_advanced.oop_10 import Smartphone

phone = Smartphone(
    name="iPhone 15 Pro",
    price=99990,
    brand="Apple",
    model="15 Pro",
    screen_size=6.1,
    ram_gb=8,
    storage_gb=256,
    battery_mah=3274,
    stock=15
)

print(phone.name)                    # iPhone 15 Pro
print(phone.get_category())          # ProductCategory.SMARTPHONE
print(phone.get_specifications())    # {...}
print(phone.get_warranty_period())   # 12
```

### Inventory
Управление инвентарем:
```python
from lesson_10_OOP_advanced.oop_10 import Inventory

inventory = Inventory()
inventory.add_product(phone)

# Поиск
smartphones = inventory.get_products_by_category(ProductCategory.SMARTPHONE)
results = inventory.search_products("Apple")

# Скидки
inventory.apply_discount_to_category(ProductCategory.SMARTPHONE, 10)
```

### Order
Создание заказов:
```python
from lesson_10_OOP_advanced.oop_10 import Order

order = Order(
    customer_name="Иван Иванов",
    customer_email="ivan@mail.ru"
)

order.add_item(phone, quantity=2)
print(order.get_total())  # Общая сумма
```

---

## 💡 Быстрые примеры

### Создать товар и применить скидку

```python
from lesson_10_OOP_advanced.oop_10 import Laptop, Inventory

laptop = Laptop(
    name="MacBook Pro",
    price=189990,
    brand="Apple",
    processor="M3 Pro",
    ram_gb=18,
    storage_gb=512,
    screen_size=14.2,
    has_dedicated_gpu=True,
    stock=10
)

# Применяем скидку
laptop.discount_percent = 15
print(f"Цена со скидкой: {laptop.get_final_price()}₽")
```

### Полиморфизм в действии

```python
from lesson_10_OOP_advanced.oop_10 import Smartphone, Laptop, Cable

products = [
    Smartphone(...),
    Laptop(...),
    Cable(...)
]

# Один интерфейс - разные реализации
for product in products:
    print(f"{product.name}:")
    print(f"  Категория: {product.get_category().value}")
    print(f"  Гарантия: {product.get_warranty_period()} мес.")
    print(f"  Характеристики: {product.get_specifications()}")
```

### API запрос (curl)

```bash
# Получить все товары
curl http://localhost:8000/products

# Создать заказ
curl -X POST "http://localhost:8000/orders" \
  -H "Content-Type: application/json" \
  -d '{
    "customer_name": "Петр Петров",
    "customer_email": "petr@mail.ru",
    "items": [
      {"product_id": "PROD_00001", "quantity": 1}
    ]
  }'
```

---

## 🎯 Что изучить дальше?

1. **Прочитай** `README.md` - полная документация
2. **Изучи** `oop_10.py` - все классы с комментариями
3. **Попробуй** `fastapi_app.py` - запусти API
4. **Реши** задания в `homework/homework_10.md`
5. **Посмотри** `api_examples.md` - примеры запросов

---

## 🆘 Частые вопросы

**Q: Как запустить FastAPI?**
```bash
source .venv/bin/activate
uvicorn lesson_10_OOP_advanced.fastapi_app:app --reload
```

**Q: Где документация API?**
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

**Q: Как создать свой класс товара?**
```python
from lesson_10_OOP_advanced.oop_10 import Product, ProductCategory

class Monitor(Product):
    def __init__(self, name, price, ...):
        super().__init__(name, price)
        # твои поля
    
    def get_category(self):
        return ProductCategory.ACCESSORY
    
    def get_specifications(self):
        return {...}
    
    def get_warranty_period(self):
        return 24
```

**Q: Как импортировать классы?**
```python
from lesson_10_OOP_advanced.oop_10 import (
    Product,
    Smartphone,
    Laptop,
    Inventory,
    Order,
    ProductCategory
)
```

---

## 🎉 Готово!

Теперь у тебя есть:
- ✅ Полноценное ООП приложение
- ✅ FastAPI интеграция
- ✅ Примеры использования
- ✅ Задания для практики

**Начни с демонстрации, затем запусти API, потом делай домашку!**

---

**Удачи! 🚀**
