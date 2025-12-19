"""
Домашнее задание - Урок 10
Закрепление ООП на примере магазина электронной техники

Импортируй необходимые классы из oop_10.py и создавай свои классы здесь
"""
from lesson_10_OOP_advanced.oop_10 import (
    Inventory,
    Order,
    ProductCategory,
    OrderStatus,
    Smartphone,
    Product
)
from typing import List, Optional, Dict, Any
from datetime import datetime

# ============= ЗАДАНИЕ 1: Monitor =============

# TODO: Создай класс Monitor, который наследует Product
# (Задание уже выполнено, можно оставить как есть)
# ============= ЗАДАНИЕ 2: SmartWatch =============

# TODO: Создай класс SmartWatch, который наследует Product
# Смотри задание в homework_10.md


# ============= ЗАДАНИЕ 3: SmartphoneWithCamera =============

# TODO: Создай класс SmartphoneWithCamera, который наследует Smartphone
# Смотри задание в homework_10.md


# ============= ЗАДАНИЕ 4: DiscountManager =============

# TODO: Создай класс DiscountManager
# (Задание уже выполнено, можно оставить как есть)


# ============= ЗАДАНИЕ 5: Customer =============

# TODO: Создай класс Customer
# Используй циклы for для подсчета суммы и количества заказов
# Используй условия if для проверки VIP статуса


# ============= ЗАДАНИЕ 6: Функция отчета =============

# TODO: Создай функцию generate_product_report
# Используй цикл for для перебора товаров
# Используй цикл для подсчета общей стоимости


# ============= ЗАДАНИЕ 7: Review =============

# TODO: Создай класс Review
# Используй условия if для валидации рейтинга и комментария


# ============= ЗАДАНИЕ 8: PaymentMethod =============

# TODO: Создай 3 простых класса для способов оплаты
# CreditCardPayment, CashPayment, CryptocurrencyPayment
# Используй цикл for для демонстрации работы всех способов


# ============= ЗАДАНИЕ 9: PromoCode =============

# TODO: Создай класс PromoCode
# Добавь метод apply_promo_code в класс Order
# Используй условия if для проверки активности промокода и суммы заказа


# ============= ЗАДАНИЕ 10: NotificationService =============

# TODO: Создай 3 простых класса для уведомлений
# EmailNotification, SMSNotification, PushNotification
# Добавь в Order список уведомлений и используй цикл for для отправки


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
