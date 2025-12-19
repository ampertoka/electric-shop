"""
Домашнее задание - Урок 10
Закрепление ООП на примере магазина электронной техники

Импортируй необходимые классы из oop_10.py и создавай свои классы здесь

ПРИМЕР: Как создать класс, который наследует Product:
    
    class MyProduct(Product):
        def __init__(self, name: str, price: float, my_field: str, stock: int = 0):
            # Вызываем конструктор родителя
            super().__init__(name, price, "", stock)
            # Сохраняем свои поля
            self._my_field = my_field
        
        # Переопределяем методы родителя
        def get_category(self) -> ProductCategory:
            return ProductCategory.ACCESSORY
        
        def get_specifications(self) -> Dict[str, Any]:
            return {"my_field": self._my_field}
        
        def get_warranty_period(self) -> int:
            return 12
"""
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
    """Класс монитора - пример наследования от Product"""
    
    def __init__(self, name: str, price: float, brand: str, 
                 screen_size: float, resolution: str, 
                 refresh_rate: int, panel_type: str,
                 description: str = "", stock: int = 0):
        # Вызываем конструктор родительского класса
        super().__init__(name, price, description, stock)
        # Сохраняем специфичные для монитора поля
        self._brand = brand
        self._screen_size = screen_size
        self._resolution = resolution
        self._refresh_rate = refresh_rate
        self._panel_type = panel_type

    def get_specifications(self) -> Dict[str, Any]:
        """Возвращает характеристики монитора"""
        return {
            'brand': self._brand,
            'screen_size': f"{self._screen_size}\"",
            'resolution': self._resolution,
            'refresh_rate': f"{self._refresh_rate} Гц",
            'panel_type': self._panel_type
        }
    
    def get_warranty_period(self) -> int:
        """Гарантия на монитор - 24 месяца"""
        return 24
    
    def get_category(self) -> ProductCategory:
        """Категория товара - монитор"""
        return ProductCategory.MONITOR
    
    def is_gaming_monitor(self) -> bool:
        """Проверяет, является ли монитор игровым (частота >= 144 Гц)"""
        if self._refresh_rate >= 144:
            return True
        return False

# Пример использования Monitor:
# monitor = Monitor(
#     name="LG UltraGear 27GL850",
#     price=35990,
#     brand="LG",
#     screen_size=27,
#     resolution="2560x1440",
#     refresh_rate=144,
#     panel_type="IPS",
#     stock=8
# )
# print(monitor)
# print(monitor.get_specifications())
# print(f"Игровой: {monitor.is_gaming_monitor()}")

# ============= ЗАДАНИЕ 1.1: DiscountManager =============

# TODO: Создай класс DiscountManager для управления скидками
# Смотри задание 1.1 в homework_10.md


# ============= ЗАДАНИЕ 2: SmartWatch =============

# TODO: Создай класс SmartWatch, который наследует Product
# Смотри задание 2 в homework_10.md
class SmartWatch(Product):
    def __init__(
            self, brand: str, model: str, display_size: float,
            battery_days: int, has_gps: bool,
            waterproof_rating: str
    ):
        super(SmartWatch, self).__init__()
        self._brand = brand
        self._model = model
        self._display_size = display_size
        self._battery_days = battery_days
        self._has_gps = has_gps
        self._waterproof_rating = waterproof_rating
        

# ПОДСКАЗКА - структура класса:
# class SmartWatch(Product):
#     def __init__(self, name, price, brand, model, display_size, 
#                  battery_days, has_gps, waterproof_rating, stock=0):
#         super().__init__(name, price, "", stock)
#         self._brand = brand
#         # ... остальные поля
#     
#     def get_category(self) -> ProductCategory:
#         return ProductCategory.ACCESSORY
#     
#     def get_specifications(self) -> Dict[str, Any]:
#         return {...}  # словарь с характеристиками
#     
#     def get_warranty_period(self) -> int:
#         return 12
#     
#     def is_suitable_for_sports(self) -> bool:
#         if self._has_gps == True and self._waterproof_rating:
#             return True
#         return False


# ============= ЗАДАНИЕ 3: SmartphoneWithCamera =============

# TODO: Создай класс SmartphoneWithCamera, который наследует Smartphone
# Смотри задание 3 в homework_10.md
# 
# ПОДСКАЗКА - структура класса:
# class SmartphoneWithCamera(Smartphone):
#     def __init__(self, name, price, brand, model, screen_size,
#                  ram_gb, storage_gb, battery_mah,
#                  main_camera_mp, front_camera_mp, has_optical_zoom,
#                  stock=0):
#         # Вызываем конструктор Smartphone
#         super().__init__(name, price, brand, model, screen_size,
#                          ram_gb, storage_gb, battery_mah, "", stock)
#         # Добавляем свои поля
#         self._main_camera_mp = main_camera_mp
#         # ... остальные поля
#     
#     def get_specifications(self) -> Dict[str, Any]:
#         specs = super().get_specifications()  # Получаем базовые характеристики
#         specs["main_camera"] = f"{self._main_camera_mp} МП"
#         # ... добавляем информацию о камерах
#         return specs
#     
#     def get_camera_rating(self) -> str:
#         if self._main_camera_mp >= 48 and self._has_optical_zoom == True:
#             return "Отличная"
#         elif self._main_camera_mp >= 48:
#             return "Хорошая"
#         else:
#             return "Средняя"


# ============= ЗАДАНИЕ 4: Функция отчета =============

# TODO: Создай функцию generate_product_report
# Смотри задание 4 в homework_10.md
# 
# ПОДСКАЗКА - структура функции:
# def generate_product_report(products: List[Product]) -> str:
#     report = "=== ОТЧЕТ ПО ТОВАРАМ ===\n"
#     
#     # Цикл для перебора товаров с нумерацией
#     for i, product in enumerate(products, 1):
#         name = product.name
#         category = product.get_category().value
#         price = product.price
#         warranty = product.get_warranty_period()
#         report += f"{i}. {name} [{category}] - {price}₽ (гарантия: {warranty} мес.)\n"
#     
#     report += "------------------------\n"
#     
#     # Подсчет общей стоимости
#     total = 0
#     for product in products:
#         total += product.price
#     
#     report += f"Всего товаров: {len(products)}\n"
#     report += f"Общая стоимость: {total}₽\n"
#     
#     return report


# ============= ЗАДАНИЕ 5: Review =============

# TODO: Создай класс Review
# Смотри задание 5 в homework_10.md
# 
# ПОДСКАЗКА - структура класса:
# class Review:
#     _id_counter = 0  # Счетчик для ID (как в Product)
#     
#     def __init__(self, product_id: str, customer_name: str, 
#                  rating: int, comment: str):
#         # Валидация рейтинга
#         if rating < 1 or rating > 5:
#             raise ValueError("Рейтинг должен быть от 1 до 5")
#         
#         # Валидация комментария
#         if not comment:
#             raise ValueError("Комментарий не может быть пустым")
#         
#         # Генерация ID
#         Review._id_counter += 1
#         self._id = f"REV_{Review._id_counter:05d}"
#         
#         # Сохранение полей
#         self._product_id = product_id
#         self._customer_name = customer_name
#         self._rating = rating
#         self._comment = comment
#         self._created_at = datetime.now()
#     
#     def is_positive(self) -> bool:
#         if self._rating >= 4:
#             return True
#         return False
#     
#     def to_dict(self) -> dict:
#         return {
#             "id": self._id,
#             "product_id": self._product_id,
#             "customer_name": self._customer_name,
#             "rating": self._rating,
#             "comment": self._comment,
#             "created_at": self._created_at.isoformat()
#         }


# ============= ЗАДАНИЕ 6: PaymentMethod =============

# TODO: Создай 3 простых класса для способов оплаты
# Смотри задание 6 в homework_10.md
# 
# ПОДСКАЗКА - пример класса:
# class CreditCardPayment:
#     def __init__(self, card_number: str):
#         self._card_number = card_number
#     
#     def process_payment(self, amount: float):
#         print(f"Оплата картой {self._card_number} на сумму {amount}₽ прошла успешно")
#     
#     def get_payment_type(self) -> str:
#         return "Оплата картой"
# 
# # Аналогично создай CashPayment и CryptocurrencyPayment
# # Для CashPayment не нужен параметр в __init__ (просто self)
# # Для CryptocurrencyPayment нужен wallet_address: str


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
