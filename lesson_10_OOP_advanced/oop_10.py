"""
Урок 10 - Закрепление ООП на примере магазина электронной техники
Простое ООП для начинающих: классы, наследование, функции, циклы, условия

Принципы ООП:
1. Инкапсуляция - сокрытие данных (приватные поля, геттеры/сеттеры)
2. Наследование - иерархия классов Product -> Smartphone, Laptop, etc.
3. Полиморфизм - разные классы реализуют одинаковые методы по-своему
"""

from datetime import datetime
from typing import List, Optional, Dict, Any
from enum import Enum


# ============= ENUMS =============
class ProductCategory(str, Enum):
    """Категории товаров"""
    SMARTPHONE = "smartphone"
    ACCESSORY = "accessory"
    MONITOR = "monitor"


# ============= БАЗОВЫЙ КЛАСС ТОВАРА =============
class Product:
    """
    Базовый класс для всех товаров
    Демонстрирует ИНКАПСУЛЯЦИЮ и НАСЛЕДОВАНИЕ
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
    
    # Методы, которые можно переопределить в наследниках
    def get_category(self) -> ProductCategory:
        """Возвращает категорию товара (по умолчанию ACCESSORY)"""
        return ProductCategory.ACCESSORY
    
    def get_specifications(self) -> Dict[str, Any]:
        """Возвращает технические характеристики товара (по умолчанию пустой словарь)"""
        return {}
    
    def get_warranty_period(self) -> int:
        """Возвращает срок гарантии в месяцах (по умолчанию 12 месяцев)"""
        return 12
    
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


# ============= КОНКРЕТНЫЕ КЛАССЫ ТОВАРОВ (Наследование) =============

class Smartphone(Product):
    """
    Класс смартфона - наследник Product
    Демонстрирует НАСЛЕДОВАНИЕ
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
    
    # Переопределение методов родительского класса
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


# ============= ДЕМОНСТРАЦИЯ РАБОТЫ =============

def demo_oop_principles():
    """Простая демонстрация ООП"""
    
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
    
    # Добавляем в инвентарь
    for product in [phone1, phone2]:
        inventory.add_product(product)
        print(f"✓ Добавлен: {product}")
    
    # 2. НАСЛЕДОВАНИЕ - переопределение методов
    print("\n2. НАСЛЕДОВАНИЕ - Характеристики товаров")
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
    print(f"{phone2.name} - Время работы батареи: {phone2.get_battery_life_estimate()}")
    
    # 5. РАБОТА С ИНВЕНТАРЕМ
    print("\n5. УПРАВЛЕНИЕ ИНВЕНТАРЕМ")
    print("-" * 80)
    print(f"Всего товаров: {len(inventory)}")
    print(f"Общая стоимость инвентаря: {inventory.get_total_inventory_value():,.2f}₽")
    
    smartphones = inventory.get_products_by_category(ProductCategory.SMARTPHONE)
    print(f"\nСмартфонов в наличии: {len(smartphones)}")
    for phone in smartphones:
        print(f"  - {phone}")
    
    # 6. ПРИМЕНЕНИЕ СКИДКИ К КАТЕГОРИИ
    print("\n6. МАССОВОЕ ПРИМЕНЕНИЕ СКИДКИ")
    print("-" * 80)
    print("Применяем скидку 15% на все смартфоны...")
    inventory.apply_discount_to_category(ProductCategory.SMARTPHONE, 15)
    
    for phone in smartphones:
        print(f"  {phone.name}: {phone.price}₽ → {phone.get_final_price()}₽")
    
    print("\n" + "=" * 80)
    print("ДЕМОНСТРАЦИЯ ЗАВЕРШЕНА")
    print("=" * 80)


if __name__ == "__main__":
    demo_oop_principles()
