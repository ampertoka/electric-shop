"""
Домашнее задание - Урок 10
Закрепление ООП на примере магазина электронной техники

Импортируй необходимые классы из oop_10.py и создавай свои классы здесь
"""
from enum import Enum

from lesson_10_OOP_advanced.oop_10 import (
    Inventory,
    ProductCategory,
    Smartphone,
    Product
)
from typing import List, Optional, Dict, Any
from datetime import datetime

# ============= ЗАДАНИЕ 1: Monitor =============

'''
**Задача:**
- Создай класс `Monitor`, который наследует `Product`
- Добавь специфичные поля:
  - `brand: str` - бренд
  - `screen_size: float` - диагональ в дюймах
  - `resolution: str` - разрешение (например, "1920x1080", "2560x1440")
  - `refresh_rate: int` - частота обновления в Гц
  - `panel_type: str` - тип матрицы (IPS, VA, TN)
- Реализуй все абстрактные методы:
  - `get_category()` → верни `ProductCategory.ACCESSORY` (или создай новую категорию)
  - `get_specifications()` → верни словарь с характеристиками
  - `get_warranty_period()` → 24 месяца
- Добавь метод `is_gaming_monitor()` → возвращает `True`, если частота >= 144 Гц
'''


class Monitor(Product):
    _brand: str
    _screen_size: float
    _resolusion: str
    _refresh_rate: int
    _panel_type: str

    def get_specifications(self) -> Dict[str, Any]:
        return {
            'brand': self._brand,
            'screen_size': self.screen_size,
            'resolution:': self.resolusion,
            'refresh_rate': self.refresh_rate,
            'panel_type': self.panel_type
        }
    def get_warranty_period(self) -> int:
        return 24
    def get_category(self) -> ProductCategory:
        return ProductCategory.MONITOR
    def is_gaming_monitor(self) -> bool:
        if self.refresh_rate >= 144:
            return True
        return False
    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value: str):
        self._brand = value

# monitor_dell = Monitor()
# print(monitor_dell.screen_size)
# print(monitor_dell._brand)
# print(monitor_dell.brand)
# monitor_dell.brand = 1
# print(monitor_dell.brand)
class Role(str, Enum):
    """Категории ролей"""
    ADMIN = "admin"
    MANAGER = "manager"
# role_1 = Role('wera', 'kni')
# print(role_1)


# ============= ЗАДАНИЕ 1.1: DiscountManager =============
### 1.1 Создай систему скидок - класс DiscountManager

"""
**Задача:**
- Создай класс `DiscountManager` для управления скидками
- Методы:
- `apply_seasonal_discount(inventory: Inventory, discount: float)` - применяет скидку ко всем товарам
- `apply_clearance_discount(inventory: Inventory, min_stock: int, discount: float)` - применяет скидку к товарам с остатком меньше `min_stock`
- `apply_premium_discount(inventory: Inventory, min_price: float, discount: float)` - скидка на дорогие товары (цена >= min_price)
- `reset_all_discounts(inventory: Inventory)` - сбрасывает все скидки (устанавливает в 0)

**Проверка:**
```python
discount_mgr = DiscountManager()
discount_mgr.apply_clearance_discount(inventory, min_stock=10, discount=20)
# Все товары с остатком < 10 получат скидку 20%
```
"""
class DiscountManager:
    def apply_seasonal_discount(self, inventory, discount: float):
        for category in ProductCategory:
            inventory.apply_discount_to_category(category.value, discount)


# ============= ЗАДАНИЕ 2: SmartWatch =============

# TODO: Создай класс SmartWatch, который наследует Product
# Смотри задание в homework_10.md


# ============= ЗАДАНИЕ 3: SmartphoneWithCamera =============

# TODO: Создай класс SmartphoneWithCamera, который наследует Smartphone
# Смотри задание в homework_10.md


### 4️⃣ Функция для отчета о товарах

# ============= ЗАДАНИЕ 5: Customer =============

# TODO: Создай класс Customer
# Используй циклы for для подсчета суммы и количества заказов
# Используй условия if для проверки VIP статуса


# ============= ЗАДАНИЕ 6: Функция отчета =============

# TODO: Создай функцию generate_product_report
# Используй цикл for для перебора товаров
# Используй цикл для подсчета общей стоимости


# ============= ЗАДАНИЕ 5: Review =============

# TODO: Создай класс Review
# Используй условия if для валидации рейтинга и комментария


# ============= ЗАДАНИЕ 6: PaymentMethod =============

# TODO: Создай 3 простых класса для способов оплаты
# CreditCardPayment, CashPayment, CryptocurrencyPayment
# Используй цикл for для демонстрации работы всех способов


# ============= ТЕСТИРОВАНИЕ =============

def test_homework():
    """Функция для тестирования твоих решений"""
    print("=" * 80)
    print("ТЕСТИРОВАНИЕ ДОМАШНЕГО ЗАДАНИЯ")
    print("=" * 80)

    # Здесь будут тесты для каждого задания
    # Раскомментируй по мере выполнения заданий

    # # Тест 1: Monitor
    # print("\n1. Тест Monitor")
    # print("-" * 80)
    # monitor = Monitor(...)
    # print(monitor)

    # # Тест 2: SmartWatch
    # print("\n2. Тест SmartWatch")
    # print("-" * 80)
    # watch = SmartWatch(...)
    # print(watch)

    # И так далее...

    print("\n" + "=" * 80)
    print("ТЕСТИРОВАНИЕ ЗАВЕРШЕНО")
    print("=" * 80)


if __name__ == "__main__":
    test_homework()
