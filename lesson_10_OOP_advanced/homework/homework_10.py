"""
Домашнее задание - Урок 10
Закрепление ООП на примере магазина электронной техники

Импортируй необходимые классы из oop_10.py и создавай свои классы здесь
"""

from lesson_10_OOP_advanced.oop_10 import (
    Product,
    Inventory,
    Order,
    ProductCategory,
    OrderStatus,
    Smartphone
)
from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any
from datetime import datetime


# ============= ЗАДАНИЕ 1: Monitor =============

# TODO: Создай класс Monitor, который наследует Product


# ============= ЗАДАНИЕ 2: SmartWatch =============

# TODO: Создай класс SmartWatch


# ============= ЗАДАНИЕ 3: SmartphoneWithCamera =============

# TODO: Создай класс SmartphoneWithCamera, который наследует Smartphone


# ============= ЗАДАНИЕ 4: DiscountManager =============

# TODO: Создай класс DiscountManager


# ============= ЗАДАНИЕ 5: Customer =============

# TODO: Создай класс Customer


# ============= ЗАДАНИЕ 6: Функция отчета =============

# TODO: Создай функцию generate_product_report


# ============= ЗАДАНИЕ 7: Review =============

# TODO: Создай класс Review


# ============= ЗАДАНИЕ 8: PaymentMethod =============

# TODO: Создай абстрактный класс PaymentMethod и его реализации


# ============= ЗАДАНИЕ 9: PromoCode =============

# TODO: Создай класс PromoCode


# ============= ЗАДАНИЕ 10: NotificationService =============

# TODO: Создай абстрактный класс NotificationService и его реализации


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
