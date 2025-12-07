"""
Урок 10 - Закрепление ООП на примере магазина электронной техники
Демонстрация всех принципов ООП с интеграцией FastAPI

Принципы ООП:
1. Инкапсуляция - сокрытие данных (приватные поля, геттеры/сеттеры)
2. Наследование - иерархия классов Product -> Smartphone, Laptop, etc.
3. Полиморфизм - разные классы реализуют одинаковые методы по-своему
4. Абстракция - абстрактные классы и интерфейсы (ABC)
"""

from abc import ABC, abstractmethod
from datetime import datetime
from typing import List, Optional, Dict, Any
from enum import Enum
from pydantic import BaseModel, Field, field_validator


# ============= ENUMS =============
class ProductCategory(str, Enum):
    """Категории товаров"""
    SMARTPHONE = "smartphone"
    LAPTOP = "laptop"
    TABLET = "tablet"
    ACCESSORY = "accessory"
    CABLE = "cable"
    MONITOR = "monitor"


class OrderStatus(str, Enum):
    """Статусы заказа"""
    PENDING = "pending"
    PROCESSING = "processing"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"


# ============= PYDANTIC MODELS для FastAPI =============
class ProductBase(BaseModel):
    """Базовая Pydantic модель для валидации данных продукта"""
    name: str = Field(..., min_length=1, max_length=100)
    price: float = Field(..., gt=0)
    description: Optional[str] = None
    stock: int = Field(default=0, ge=0)
    
    @field_validator('price')
    @classmethod
    def validate_price(cls, v):
        if v <= 0:
            raise ValueError('Цена должна быть положительной')
        return round(v, 2)


class ProductCreate(ProductBase):
    """Модель для создания продукта"""
    category: ProductCategory


class ProductResponse(ProductBase):
    """Модель ответа с продуктом"""
    id: str
    category: ProductCategory
    created_at: datetime
    
    class Config:
        from_attributes = True


# ============= АБСТРАКТНЫЕ КЛАССЫ (Абстракция) =============
class Product(ABC):
    """
    Абстрактный базовый класс для всех товаров
    Демонстрирует принцип АБСТРАКЦИИ
    """
    
    # Счетчик для генерации ID (класс-переменная)
    _id_counter = 0
    
    def __init__(self, name: str, price: float, description: str = "", stock: int = 0):
        # Инкапсуляция: приватные поля (с подчеркиванием)
        Product._id_counter += 1
        self._id = f"PROD_{Product._id_counter:05d}"
        self._name = name
        self._price = price
        self._description = description
        self._stock = stock
        self._created_at = datetime.now()
        self._discount_percent = 0.0
    
    # Геттеры и сеттеры (Инкапсуляция)
    @property
    def id(self) -> str:
        """ID товара (только чтение)"""
        return self._id
    
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, value: str):
        if not value or len(value) < 1:
            raise ValueError("Название не может быть пустым")
        self._name = value
    
    @property
    def price(self) -> float:
        return self._price
    
    @price.setter
    def price(self, value: float):
        if value <= 0:
            raise ValueError("Цена должна быть положительной")
        self._price = round(value, 2)
    
    @property
    def stock(self) -> int:
        return self._stock
    
    @stock.setter
    def stock(self, value: int):
        if value < 0:
            raise ValueError("Остаток не может быть отрицательным")
        self._stock = value
    
    @property
    def description(self) -> str:
        return self._description
    
    @description.setter
    def description(self, value: str):
        self._description = value
    
    @property
    def discount_percent(self) -> float:
        return self._discount_percent
    
    @discount_percent.setter
    def discount_percent(self, value: float):
        if value < 0 or value > 100:
            raise ValueError("Скидка должна быть от 0 до 100%")
        self._discount_percent = value
    
    def get_final_price(self) -> float:
        """Вычисляет финальную цену с учетом скидки"""
        return round(self._price * (1 - self._discount_percent / 100), 2)
    
    def is_available(self) -> bool:
        """Проверяет доступность товара"""
        return self._stock > 0
    
    def add_stock(self, quantity: int):
        """Добавляет товар на склад"""
        if quantity <= 0:
            raise ValueError("Количество должно быть положительным")
        self._stock += quantity
    
    def reduce_stock(self, quantity: int):
        """Уменьшает количество товара на складе"""
        if quantity <= 0:
            raise ValueError("Количество должно быть положительным")
        if quantity > self._stock:
            raise ValueError(f"Недостаточно товара на складе. Доступно: {self._stock}")
        self._stock -= quantity
    
    # Абстрактные методы (должны быть реализованы в наследниках)
    @abstractmethod
    def get_category(self) -> ProductCategory:
        """Возвращает категорию товара"""
        pass
    
    @abstractmethod
    def get_specifications(self) -> Dict[str, Any]:
        """Возвращает технические характеристики товара"""
        pass
    
    @abstractmethod
    def get_warranty_period(self) -> int:
        """Возвращает срок гарантии в месяцах"""
        pass
    
    def to_dict(self) -> dict:
        """Преобразует объект в словарь для JSON"""
        return {
            "id": self._id,
            "name": self._name,
            "price": self._price,
            "final_price": self.get_final_price(),
            "description": self._description,
            "stock": self._stock,
            "discount_percent": self._discount_percent,
            "category": self.get_category().value,
            "specifications": self.get_specifications(),
            "warranty_months": self.get_warranty_period(),
            "created_at": self._created_at.isoformat(),
            "available": self.is_available()
        }
    
    def __str__(self) -> str:
        return f"{self.get_category().value.upper()}: {self._name} - {self.get_final_price()}₽ (в наличии: {self._stock})"
    
    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}(id={self._id}, name={self._name})>"


# ============= КОНКРЕТНЫЕ КЛАССЫ ТОВАРОВ (Наследование и Полиморфизм) =============

class Smartphone(Product):
    """
    Класс смартфона - наследник Product
    Демонстрирует НАСЛЕДОВАНИЕ и ПОЛИМОРФИЗМ
    """
    
    def __init__(self, name: str, price: float, brand: str, model: str,
                 screen_size: float, ram_gb: int, storage_gb: int,
                 battery_mah: int, description: str = "", stock: int = 0):
        super().__init__(name, price, description, stock)
        self._brand = brand
        self._model = model
        self._screen_size = screen_size
        self._ram_gb = ram_gb
        self._storage_gb = storage_gb
        self._battery_mah = battery_mah
    
    # Реализация абстрактных методов (Полиморфизм)
    def get_category(self) -> ProductCategory:
        return ProductCategory.SMARTPHONE
    
    def get_specifications(self) -> Dict[str, Any]:
        return {
            "brand": self._brand,
            "model": self._model,
            "screen_size": f"{self._screen_size}\"",
            "ram": f"{self._ram_gb} GB",
            "storage": f"{self._storage_gb} GB",
            "battery": f"{self._battery_mah} mAh"
        }
    
    def get_warranty_period(self) -> int:
        return 12  # 12 месяцев гарантии
    
    # Специфичные методы для смартфона
    def get_battery_life_estimate(self) -> str:
        """Оценка времени работы батареи"""
        if self._battery_mah >= 5000:
            return "Отличное (2+ дня)"
        elif self._battery_mah >= 4000:
            return "Хорошее (1-2 дня)"
        else:
            return "Среднее (до 1 дня)"
    
    @property
    def brand(self) -> str:
        return self._brand
    
    @property
    def model(self) -> str:
        return self._model


class Laptop(Product):
    """
    Класс ноутбука - наследник Product
    """
    
    def __init__(self, name: str, price: float, brand: str, processor: str,
                 ram_gb: int, storage_gb: int, screen_size: float,
                 has_dedicated_gpu: bool = False, description: str = "", stock: int = 0):
        super().__init__(name, price, description, stock)
        self._brand = brand
        self._processor = processor
        self._ram_gb = ram_gb
        self._storage_gb = storage_gb
        self._screen_size = screen_size
        self._has_dedicated_gpu = has_dedicated_gpu
    
    def get_category(self) -> ProductCategory:
        return ProductCategory.LAPTOP
    
    def get_specifications(self) -> Dict[str, Any]:
        return {
            "brand": self._brand,
            "processor": self._processor,
            "ram": f"{self._ram_gb} GB",
            "storage": f"{self._storage_gb} GB",
            "screen_size": f"{self._screen_size}\"",
            "dedicated_gpu": "Да" if self._has_dedicated_gpu else "Нет"
        }
    
    def get_warranty_period(self) -> int:
        return 24  # 24 месяца гарантии
    
    def is_gaming_laptop(self) -> bool:
        """Определяет, является ли ноутбук игровым"""
        return self._has_dedicated_gpu and self._ram_gb >= 16
    
    @property
    def brand(self) -> str:
        return self._brand


class Tablet(Product):
    """Класс планшета"""
    
    def __init__(self, name: str, price: float, brand: str, screen_size: float,
                 storage_gb: int, has_stylus: bool = False,
                 description: str = "", stock: int = 0):
        super().__init__(name, price, description, stock)
        self._brand = brand
        self._screen_size = screen_size
        self._storage_gb = storage_gb
        self._has_stylus = has_stylus
    
    def get_category(self) -> ProductCategory:
        return ProductCategory.TABLET
    
    def get_specifications(self) -> Dict[str, Any]:
        return {
            "brand": self._brand,
            "screen_size": f"{self._screen_size}\"",
            "storage": f"{self._storage_gb} GB",
            "stylus_support": "Да" if self._has_stylus else "Нет"
        }
    
    def get_warranty_period(self) -> int:
        return 12


class Cable(Product):
    """Класс кабеля - простой товар"""
    
    def __init__(self, name: str, price: float, cable_type: str,
                 length_m: float, color: str = "black",
                 description: str = "", stock: int = 0):
        super().__init__(name, price, description, stock)
        self._cable_type = cable_type  # USB-C, Lightning, HDMI, etc.
        self._length_m = length_m
        self._color = color
    
    def get_category(self) -> ProductCategory:
        return ProductCategory.CABLE
    
    def get_specifications(self) -> Dict[str, Any]:
        return {
            "type": self._cable_type,
            "length": f"{self._length_m} м",
            "color": self._color
        }
    
    def get_warranty_period(self) -> int:
        return 6  # 6 месяцев гарантии


class Accessory(Product):
    """Класс аксессуара - общий класс для различных аксессуаров"""
    
    def __init__(self, name: str, price: float, accessory_type: str,
                 compatible_with: List[str], description: str = "", stock: int = 0):
        super().__init__(name, price, description, stock)
        self._accessory_type = accessory_type  # case, charger, headphones, etc.
        self._compatible_with = compatible_with
    
    def get_category(self) -> ProductCategory:
        return ProductCategory.ACCESSORY
    
    def get_specifications(self) -> Dict[str, Any]:
        return {
            "type": self._accessory_type,
            "compatible_with": ", ".join(self._compatible_with)
        }
    
    def get_warranty_period(self) -> int:
        return 6


# ============= СИСТЕМА УПРАВЛЕНИЯ ИНВЕНТАРЕМ =============

class Inventory:
    """
    Класс для управления инвентарем магазина
    Демонстрирует инкапсуляцию и работу с коллекциями объектов
    """
    
    def __init__(self):
        self._products: Dict[str, Product] = {}
    
    def add_product(self, product: Product) -> str:
        """Добавляет товар в инвентарь"""
        if product.id in self._products:
            raise ValueError(f"Товар с ID {product.id} уже существует")
        self._products[product.id] = product
        return product.id
    
    def get_product(self, product_id: str) -> Optional[Product]:
        """Получает товар по ID"""
        return self._products.get(product_id)
    
    def remove_product(self, product_id: str) -> bool:
        """Удаляет товар из инвентаря"""
        if product_id in self._products:
            del self._products[product_id]
            return True
        return False
    
    def get_all_products(self) -> List[Product]:
        """Возвращает все товары"""
        return list(self._products.values())
    
    def get_products_by_category(self, category: ProductCategory) -> List[Product]:
        """Возвращает товары по категории (Полиморфизм)"""
        return [p for p in self._products.values() if p.get_category() == category]
    
    def get_available_products(self) -> List[Product]:
        """Возвращает товары в наличии"""
        return [p for p in self._products.values() if p.is_available()]
    
    def search_products(self, query: str) -> List[Product]:
        """Поиск товаров по названию"""
        query_lower = query.lower()
        return [p for p in self._products.values() 
                if query_lower in p.name.lower() or query_lower in p.description.lower()]
    
    def get_total_inventory_value(self) -> float:
        """Вычисляет общую стоимость инвентаря"""
        return sum(p.price * p.stock for p in self._products.values())
    
    def apply_discount_to_category(self, category: ProductCategory, discount: float):
        """Применяет скидку ко всем товарам категории"""
        for product in self.get_products_by_category(category):
            product.discount_percent = discount
    
    def __len__(self) -> int:
        """Возвращает количество товаров"""
        return len(self._products)
    
    def __str__(self) -> str:
        return f"Inventory: {len(self._products)} products, total value: {self.get_total_inventory_value()}₽"


# ============= СИСТЕМА ЗАКАЗОВ =============

class OrderItem:
    """Элемент заказа - связь между заказом и товаром"""
    
    def __init__(self, product: Product, quantity: int):
        if quantity <= 0:
            raise ValueError("Количество должно быть положительным")
        if not product.is_available():
            raise ValueError(f"Товар {product.name} недоступен")
        if quantity > product.stock:
            raise ValueError(f"Недостаточно товара {product.name}. Доступно: {product.stock}")
        
        self._product = product
        self._quantity = quantity
        self._price_at_purchase = product.get_final_price()
    
    @property
    def product(self) -> Product:
        return self._product
    
    @property
    def quantity(self) -> int:
        return self._quantity
    
    @property
    def price_at_purchase(self) -> float:
        return self._price_at_purchase
    
    def get_subtotal(self) -> float:
        """Вычисляет стоимость позиции"""
        return round(self._price_at_purchase * self._quantity, 2)
    
    def to_dict(self) -> dict:
        return {
            "product_id": self._product.id,
            "product_name": self._product.name,
            "quantity": self._quantity,
            "price_per_item": self._price_at_purchase,
            "subtotal": self.get_subtotal()
        }


class Order:
    """
    Класс заказа
    Демонстрирует композицию (Order содержит OrderItem)
    """
    
    _order_counter = 0
    
    def __init__(self, customer_name: str, customer_email: str):
        Order._order_counter += 1
        self._id = f"ORD_{Order._order_counter:06d}"
        self._customer_name = customer_name
        self._customer_email = customer_email
        self._items: List[OrderItem] = []
        self._status = OrderStatus.PENDING
        self._created_at = datetime.now()
        self._updated_at = datetime.now()
    
    @property
    def id(self) -> str:
        return self._id
    
    @property
    def status(self) -> OrderStatus:
        return self._status
    
    def add_item(self, product: Product, quantity: int):
        """Добавляет товар в заказ"""
        item = OrderItem(product, quantity)
        self._items.append(item)
        # Резервируем товар
        product.reduce_stock(quantity)
        self._updated_at = datetime.now()
    
    def get_total(self) -> float:
        """Вычисляет общую стоимость заказа"""
        return round(sum(item.get_subtotal() for item in self._items), 2)
    
    def get_items_count(self) -> int:
        """Возвращает количество позиций в заказе"""
        return len(self._items)
    
    def change_status(self, new_status: OrderStatus):
        """Изменяет статус заказа"""
        self._status = new_status
        self._updated_at = datetime.now()
    
    def cancel_order(self, inventory: Inventory):
        """Отменяет заказ и возвращает товары на склад"""
        if self._status in [OrderStatus.DELIVERED, OrderStatus.CANCELLED]:
            raise ValueError(f"Невозможно отменить заказ со статусом {self._status.value}")
        
        # Возвращаем товары на склад
        for item in self._items:
            item.product.add_stock(item.quantity)
        
        self._status = OrderStatus.CANCELLED
        self._updated_at = datetime.now()
    
    def to_dict(self) -> dict:
        return {
            "id": self._id,
            "customer_name": self._customer_name,
            "customer_email": self._customer_email,
            "status": self._status.value,
            "items": [item.to_dict() for item in self._items],
            "items_count": self.get_items_count(),
            "total": self.get_total(),
            "created_at": self._created_at.isoformat(),
            "updated_at": self._updated_at.isoformat()
        }
    
    def __str__(self) -> str:
        return f"Order {self._id}: {self.get_items_count()} items, total: {self.get_total()}₽, status: {self._status.value}"


# ============= ДЕМОНСТРАЦИЯ РАБОТЫ =============

def demo_oop_principles():
    """Демонстрация всех принципов ООП"""
    
    print("=" * 80)
    print("ДЕМОНСТРАЦИЯ ООП - Магазин электронной техники")
    print("=" * 80)
    
    # Создаем инвентарь
    inventory = Inventory()
    
    # 1. СОЗДАНИЕ ОБЪЕКТОВ (Инкапсуляция)
    print("\n1. СОЗДАНИЕ ТОВАРОВ")
    print("-" * 80)
    
    phone1 = Smartphone(
        name="iPhone 15 Pro",
        price=99990,
        brand="Apple",
        model="15 Pro",
        screen_size=6.1,
        ram_gb=8,
        storage_gb=256,
        battery_mah=3274,
        description="Флагманский смартфон Apple",
        stock=15
    )
    
    phone2 = Smartphone(
        name="Samsung Galaxy S24",
        price=79990,
        brand="Samsung",
        model="Galaxy S24",
        screen_size=6.2,
        ram_gb=8,
        storage_gb=256,
        battery_mah=4000,
        description="Флагманский смартфон Samsung",
        stock=20
    )
    
    laptop1 = Laptop(
        name="MacBook Pro 14",
        price=189990,
        brand="Apple",
        processor="M3 Pro",
        ram_gb=18,
        storage_gb=512,
        screen_size=14.2,
        has_dedicated_gpu=True,
        description="Профессиональный ноутбук",
        stock=10
    )
    
    tablet1 = Tablet(
        name="iPad Air",
        price=54990,
        brand="Apple",
        screen_size=10.9,
        storage_gb=64,
        has_stylus=True,
        description="Планшет для работы и творчества",
        stock=25
    )
    
    cable1 = Cable(
        name="USB-C кабель",
        price=1990,
        cable_type="USB-C to USB-C",
        length_m=2.0,
        color="white",
        description="Быстрая зарядка и передача данных",
        stock=100
    )
    
    accessory1 = Accessory(
        name="AirPods Pro",
        price=24990,
        accessory_type="headphones",
        compatible_with=["iPhone", "iPad", "MacBook"],
        description="Беспроводные наушники с шумоподавлением",
        stock=30
    )
    
    # Добавляем в инвентарь
    for product in [phone1, phone2, laptop1, tablet1, cable1, accessory1]:
        inventory.add_product(product)
        print(f"✓ Добавлен: {product}")
    
    # 2. ПОЛИМОРФИЗМ - один интерфейс, разные реализации
    print("\n2. ПОЛИМОРФИЗМ - Характеристики товаров")
    print("-" * 80)
    for product in inventory.get_all_products():
        print(f"\n{product.name}:")
        print(f"  Категория: {product.get_category().value}")
        print(f"  Гарантия: {product.get_warranty_period()} мес.")
        print(f"  Характеристики: {product.get_specifications()}")
    
    # 3. ИНКАПСУЛЯЦИЯ - работа через геттеры/сеттеры
    print("\n3. ИНКАПСУЛЯЦИЯ - Применение скидки")
    print("-" * 80)
    print(f"Цена iPhone до скидки: {phone1.price}₽")
    phone1.discount_percent = 10
    print(f"Применена скидка: {phone1.discount_percent}%")
    print(f"Финальная цена: {phone1.get_final_price()}₽")
    
    # 4. НАСЛЕДОВАНИЕ - специфичные методы подклассов
    print("\n4. НАСЛЕДОВАНИЕ - Специфичные методы")
    print("-" * 80)
    print(f"{phone1.name} - Время работы батареи: {phone1.get_battery_life_estimate()}")
    print(f"{laptop1.name} - Игровой ноутбук: {'Да' if laptop1.is_gaming_laptop() else 'Нет'}")
    
    # 5. РАБОТА С ИНВЕНТАРЕМ
    print("\n5. УПРАВЛЕНИЕ ИНВЕНТАРЕМ")
    print("-" * 80)
    print(f"Всего товаров: {len(inventory)}")
    print(f"Общая стоимость инвентаря: {inventory.get_total_inventory_value():,.2f}₽")
    
    smartphones = inventory.get_products_by_category(ProductCategory.SMARTPHONE)
    print(f"\nСмартфонов в наличии: {len(smartphones)}")
    for phone in smartphones:
        print(f"  - {phone}")
    
    # 6. СОЗДАНИЕ ЗАКАЗА (Композиция)
    print("\n6. СОЗДАНИЕ ЗАКАЗА")
    print("-" * 80)
    
    order = Order(customer_name="Иван Иванов", customer_email="ivan@example.com")
    print(f"Создан заказ: {order.id}")
    
    # Добавляем товары в заказ
    order.add_item(phone1, 2)
    print(f"  + {phone1.name} x2")
    
    order.add_item(cable1, 3)
    print(f"  + {cable1.name} x3")
    
    order.add_item(accessory1, 1)
    print(f"  + {accessory1.name} x1")
    
    print(f"\nИтого: {order.get_total():,.2f}₽")
    print(f"Статус: {order.status.value}")
    
    # Проверяем остатки на складе
    print(f"\nОстаток {phone1.name} на складе: {phone1.stock} шт.")
    print(f"Остаток {cable1.name} на складе: {cable1.stock} шт.")
    
    # 7. ИЗМЕНЕНИЕ СТАТУСА ЗАКАЗА
    print("\n7. ОБРАБОТКА ЗАКАЗА")
    print("-" * 80)
    order.change_status(OrderStatus.PROCESSING)
    print(f"Статус изменен: {order.status.value}")
    
    order.change_status(OrderStatus.SHIPPED)
    print(f"Статус изменен: {order.status.value}")
    
    # 8. ПОИСК ТОВАРОВ
    print("\n8. ПОИСК ТОВАРОВ")
    print("-" * 80)
    search_results = inventory.search_products("Apple")
    print(f"Найдено товаров по запросу 'Apple': {len(search_results)}")
    for product in search_results:
        print(f"  - {product}")
    
    # 9. ПРИМЕНЕНИЕ СКИДКИ К КАТЕГОРИИ
    print("\n9. МАССОВОЕ ПРИМЕНЕНИЕ СКИДКИ")
    print("-" * 80)
    print("Применяем скидку 15% на все аксессуары...")
    inventory.apply_discount_to_category(ProductCategory.ACCESSORY, 15)
    
    accessories = inventory.get_products_by_category(ProductCategory.ACCESSORY)
    for acc in accessories:
        print(f"  {acc.name}: {acc.price}₽ → {acc.get_final_price()}₽")
    
    print("\n" + "=" * 80)
    print("ДЕМОНСТРАЦИЯ ЗАВЕРШЕНА")
    print("=" * 80)


if __name__ == "__main__":
    demo_oop_principles()
