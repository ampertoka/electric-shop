# 📡 Примеры использования API

## 🚀 Запуск сервера

```bash
# Активируй виртуальное окружение
source .venv/bin/activate

# Запусти FastAPI сервер
uvicorn lesson_10_OOP_advanced.fastapi_app:app --reload

# Сервер запустится на http://localhost:8000
# Документация: http://localhost:8000/docs
```

---

## 📦 Примеры запросов

### 1. Получить все товары

```bash
curl http://localhost:8000/products
```

**Ответ:**
```json
{
  "count": 6,
  "products": [
    {
      "id": "PROD_00001",
      "name": "iPhone 15 Pro",
      "price": 99990,
      "final_price": 99990,
      "category": "smartphone",
      "stock": 15,
      ...
    }
  ]
}
```

---

### 2. Получить товары по категории

```bash
# Смартфоны
curl "http://localhost:8000/products?category=smartphone"

# Ноутбуки
curl "http://localhost:8000/products?category=laptop"

# Только доступные товары
curl "http://localhost:8000/products?available_only=true"
```

---

### 3. Поиск товаров

```bash
curl "http://localhost:8000/products?search=Apple"
```

---

### 4. Получить конкретный товар

```bash
curl http://localhost:8000/products/PROD_00001
```

---

### 5. Создать новый смартфон

```bash
curl -X POST "http://localhost:8000/products" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "iPhone 16 Pro Max",
    "price": 129990,
    "description": "Новейший флагман Apple",
    "stock": 5,
    "category": "smartphone",
    "brand": "Apple",
    "model": "16 Pro Max",
    "screen_size": 6.7,
    "ram_gb": 8,
    "storage_gb": 512,
    "battery_mah": 4500
  }'
```

---

### 6. Создать ноутбук

```bash
curl -X POST "http://localhost:8000/products" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Dell XPS 15",
    "price": 149990,
    "description": "Мощный ноутбук для профессионалов",
    "stock": 8,
    "category": "laptop",
    "brand": "Dell",
    "processor": "Intel Core i7-13700H",
    "ram_gb": 32,
    "storage_gb": 1024,
    "screen_size": 15.6,
    "has_dedicated_gpu": true
  }'
```

---

### 7. Создать кабель

```bash
curl -X POST "http://localhost:8000/products" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "HDMI кабель 4K",
    "price": 2490,
    "description": "Поддержка 4K 60Hz",
    "stock": 50,
    "category": "cable",
    "cable_type": "HDMI 2.1",
    "length_m": 3.0,
    "color": "black"
  }'
```

---

### 8. Обновить товар

```bash
curl -X PATCH "http://localhost:8000/products/PROD_00001" \
  -H "Content-Type: application/json" \
  -d '{
    "price": 89990,
    "discount_percent": 10
  }'
```

---

### 9. Добавить товар на склад

```bash
curl -X POST "http://localhost:8000/products/PROD_00001/stock/add?quantity=10"
```

---

### 10. Применить скидку к категории

```bash
curl -X POST "http://localhost:8000/products/category/smartphone/discount?discount=15"
```

**Ответ:**
```json
{
  "message": "Скидка 15% применена к категории smartphone",
  "affected_products_count": 2,
  "products": [...]
}
```

---

### 11. Создать заказ

```bash
curl -X POST "http://localhost:8000/orders" \
  -H "Content-Type: application/json" \
  -d '{
    "customer_name": "Петр Петров",
    "customer_email": "petr@example.com",
    "items": [
      {"product_id": "PROD_00001", "quantity": 1},
      {"product_id": "PROD_00005", "quantity": 2}
    ]
  }'
```

**Ответ:**
```json
{
  "message": "Заказ успешно создан",
  "order": {
    "id": "ORD_000001",
    "customer_name": "Петр Петров",
    "customer_email": "petr@example.com",
    "status": "pending",
    "items": [...],
    "total": 103970,
    "created_at": "2024-11-29T10:30:00"
  }
}
```

---

### 12. Получить все заказы

```bash
# Все заказы
curl http://localhost:8000/orders

# Только с определенным статусом
curl "http://localhost:8000/orders?status_filter=pending"
```

---

### 13. Получить конкретный заказ

```bash
curl http://localhost:8000/orders/ORD_000001
```

---

### 14. Изменить статус заказа

```bash
curl -X PATCH "http://localhost:8000/orders/ORD_000001/status" \
  -H "Content-Type: application/json" \
  -d '{"status": "processing"}'
```

Доступные статусы:
- `pending` - ожидает обработки
- `processing` - в обработке
- `shipped` - отправлен
- `delivered` - доставлен
- `cancelled` - отменен

---

### 15. Отменить заказ

```bash
curl -X DELETE "http://localhost:8000/orders/ORD_000001"
```

**Важно:** При отмене заказа товары автоматически возвращаются на склад!

---

### 16. Статистика инвентаря

```bash
curl http://localhost:8000/inventory/stats
```

**Ответ:**
```json
{
  "total_products": 6,
  "available_products": 6,
  "total_inventory_value": 1234567.00,
  "category_stats": {
    "smartphone": {
      "count": 2,
      "total_value": 359960
    },
    "laptop": {
      "count": 1,
      "total_value": 1899900
    },
    ...
  }
}
```

---

### 17. Статистика заказов

```bash
curl http://localhost:8000/orders/stats
```

**Ответ:**
```json
{
  "total_orders": 5,
  "total_revenue": 567890.00,
  "status_stats": {
    "pending": {
      "count": 2,
      "total_revenue": 150000
    },
    "delivered": {
      "count": 3,
      "total_revenue": 417890
    },
    ...
  }
}
```

---

### 18. Удалить товар

```bash
curl -X DELETE "http://localhost:8000/products/PROD_00001"
```

---

## 🐍 Примеры на Python (requests)

### Установка библиотеки

```bash
pip install requests
```

### Создание товара

```python
import requests

url = "http://localhost:8000/products"
data = {
    "name": "Samsung Galaxy Tab S9",
    "price": 64990,
    "description": "Премиальный планшет",
    "stock": 15,
    "category": "tablet",
    "brand": "Samsung",
    "screen_size": 11.0,
    "storage_gb": 128,
    "has_stylus": True
}

response = requests.post(url, json=data)
print(response.json())
```

### Получение всех товаров

```python
import requests

response = requests.get("http://localhost:8000/products")
data = response.json()

print(f"Всего товаров: {data['count']}")
for product in data['products']:
    print(f"- {product['name']}: {product['final_price']}₽")
```

### Создание заказа

```python
import requests

url = "http://localhost:8000/orders"
data = {
    "customer_name": "Анна Смирнова",
    "customer_email": "anna@example.com",
    "items": [
        {"product_id": "PROD_00001", "quantity": 1},
        {"product_id": "PROD_00006", "quantity": 1}
    ]
}

response = requests.post(url, json=data)
order = response.json()['order']

print(f"Заказ создан: {order['id']}")
print(f"Сумма: {order['total']}₽")
print(f"Статус: {order['status']}")
```

### Применение скидки

```python
import requests

# Применяем скидку 20% на все аксессуары
url = "http://localhost:8000/products/category/accessory/discount"
params = {"discount": 20}

response = requests.post(url, params=params)
result = response.json()

print(f"Скидка применена к {result['affected_products_count']} товарам")
```

---

## 🧪 Тестирование через Swagger UI

1. Открой в браузере: http://localhost:8000/docs
2. Увидишь интерактивную документацию
3. Можешь тестировать все endpoints прямо в браузере
4. Swagger автоматически показывает структуру запросов и ответов

---

## 📊 Полезные команды

### Получить все смартфоны Apple

```bash
curl "http://localhost:8000/products?category=smartphone&search=Apple"
```

### Получить товары со скидкой

```bash
# Сначала применяем скидку
curl -X POST "http://localhost:8000/products/category/smartphone/discount?discount=10"

# Затем получаем товары
curl "http://localhost:8000/products?category=smartphone"
```

### Проверить остатки на складе

```bash
curl "http://localhost:8000/products?available_only=true" | jq '.products[] | {name: .name, stock: .stock}'
```

(требует установленный `jq` для форматирования JSON)

---

## 🎯 Сценарий использования

### Полный цикл работы магазина:

```bash
# 1. Создаем товар
curl -X POST "http://localhost:8000/products" -H "Content-Type: application/json" -d '{"name": "Test Phone", "price": 50000, "category": "smartphone", "brand": "Test", "model": "T1", "screen_size": 6.0, "ram_gb": 8, "storage_gb": 128, "battery_mah": 4000, "stock": 10}'

# 2. Проверяем товар (замени PROD_XXXXX на реальный ID)
curl http://localhost:8000/products/PROD_00007

# 3. Создаем заказ
curl -X POST "http://localhost:8000/orders" -H "Content-Type: application/json" -d '{"customer_name": "Test User", "customer_email": "test@test.com", "items": [{"product_id": "PROD_00007", "quantity": 2}]}'

# 4. Проверяем остаток товара (должен уменьшиться)
curl http://localhost:8000/products/PROD_00007

# 5. Меняем статус заказа
curl -X PATCH "http://localhost:8000/orders/ORD_000001/status" -H "Content-Type: application/json" -d '{"status": "shipped"}'

# 6. Смотрим статистику
curl http://localhost:8000/inventory/stats
curl http://localhost:8000/orders/stats
```

---

## 💡 Советы

1. **Используй Swagger UI** для первого знакомства с API - это самый простой способ
2. **Сохраняй ID товаров и заказов** - они понадобятся для других запросов
3. **Проверяй остатки** перед созданием заказа
4. **Используй фильтры** для поиска нужных товаров
5. **Следи за статусами заказов** - нельзя отменить доставленный заказ

---

**Удачи в работе с API! 🚀**
