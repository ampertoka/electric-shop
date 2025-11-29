"""
FastAPI приложение для магазина электронной техники
Использует классы из oop_10.py

Запуск: uvicorn lesson_10_OOP_advanced.fastapi_app:app --reload
"""

from fastapi import FastAPI, HTTPException, status
from fastapi.responses import JSONResponse
from typing import List, Optional
from pydantic import BaseModel, Field

from lesson_10_OOP_advanced.oop_10 import (
    Inventory,
    Smartphone,
    Laptop,
    Tablet,
    Cable,
    Accessory,
    Order,
    ProductCategory,
    OrderStatus,
    Product
)


# ============= PYDANTIC MODELS для API =============

class ProductCreateRequest(BaseModel):
    """Запрос на создание товара"""
    name: str = Field(..., min_length=1, max_length=100)
    price: float = Field(..., gt=0)
    description: str = ""
    stock: int = Field(default=0, ge=0)
    category: ProductCategory
    
    # Специфичные поля для разных категорий
    # Для смартфонов
    brand: Optional[str] = None
    model: Optional[str] = None
    screen_size: Optional[float] = None
    ram_gb: Optional[int] = None
    storage_gb: Optional[int] = None
    battery_mah: Optional[int] = None
    
    # Для ноутбуков
    processor: Optional[str] = None
    has_dedicated_gpu: Optional[bool] = False
    
    # Для планшетов
    has_stylus: Optional[bool] = False
    
    # Для кабелей
    cable_type: Optional[str] = None
    length_m: Optional[float] = None
    color: Optional[str] = "black"
    
    # Для аксессуаров
    accessory_type: Optional[str] = None
    compatible_with: Optional[List[str]] = []


class ProductUpdateRequest(BaseModel):
    """Запрос на обновление товара"""
    name: Optional[str] = None
    price: Optional[float] = None
    description: Optional[str] = None
    stock: Optional[int] = None
    discount_percent: Optional[float] = None


class OrderCreateRequest(BaseModel):
    """Запрос на создание заказа"""
    customer_name: str = Field(..., min_length=1)
    customer_email: str = Field(..., regex=r'^[\w\.-]+@[\w\.-]+\.\w+$')
    items: List[dict] = Field(..., min_items=1)
    # items format: [{"product_id": "PROD_00001", "quantity": 2}, ...]


class OrderStatusUpdateRequest(BaseModel):
    """Запрос на изменение статуса заказа"""
    status: OrderStatus


# ============= FASTAPI APP =============

app = FastAPI(
    title="Магазин электронной техники",
    description="API для управления магазином электронной техники с использованием ООП",
    version="1.0.0"
)

# Глобальный инвентарь (в реальном приложении использовалась бы БД)
inventory = Inventory()

# Глобальное хранилище заказов
orders_storage: dict[str, Order] = {}


# ============= ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ =============

def create_product_from_request(req: ProductCreateRequest) -> Product:
    """Создает объект Product на основе запроса"""
    if req.category == ProductCategory.SMARTPHONE:
        if not all([req.brand, req.model, req.screen_size, req.ram_gb, req.storage_gb, req.battery_mah]):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Для смартфона необходимы: brand, model, screen_size, ram_gb, storage_gb, battery_mah"
            )
        return Smartphone(
            name=req.name,
            price=req.price,
            brand=req.brand,
            model=req.model,
            screen_size=req.screen_size,
            ram_gb=req.ram_gb,
            storage_gb=req.storage_gb,
            battery_mah=req.battery_mah,
            description=req.description,
            stock=req.stock
        )
    
    elif req.category == ProductCategory.LAPTOP:
        if not all([req.brand, req.processor, req.ram_gb, req.storage_gb, req.screen_size]):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Для ноутбука необходимы: brand, processor, ram_gb, storage_gb, screen_size"
            )
        return Laptop(
            name=req.name,
            price=req.price,
            brand=req.brand,
            processor=req.processor,
            ram_gb=req.ram_gb,
            storage_gb=req.storage_gb,
            screen_size=req.screen_size,
            has_dedicated_gpu=req.has_dedicated_gpu,
            description=req.description,
            stock=req.stock
        )
    
    elif req.category == ProductCategory.TABLET:
        if not all([req.brand, req.screen_size, req.storage_gb]):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Для планшета необходимы: brand, screen_size, storage_gb"
            )
        return Tablet(
            name=req.name,
            price=req.price,
            brand=req.brand,
            screen_size=req.screen_size,
            storage_gb=req.storage_gb,
            has_stylus=req.has_stylus,
            description=req.description,
            stock=req.stock
        )
    
    elif req.category == ProductCategory.CABLE:
        if not all([req.cable_type, req.length_m]):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Для кабеля необходимы: cable_type, length_m"
            )
        return Cable(
            name=req.name,
            price=req.price,
            cable_type=req.cable_type,
            length_m=req.length_m,
            color=req.color,
            description=req.description,
            stock=req.stock
        )
    
    elif req.category == ProductCategory.ACCESSORY:
        if not all([req.accessory_type, req.compatible_with]):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Для аксессуара необходимы: accessory_type, compatible_with"
            )
        return Accessory(
            name=req.name,
            price=req.price,
            accessory_type=req.accessory_type,
            compatible_with=req.compatible_with,
            description=req.description,
            stock=req.stock
        )
    
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=f"Неизвестная категория: {req.category}"
    )


# ============= ENDPOINTS - ТОВАРЫ =============

@app.get("/", tags=["Root"])
def root():
    """Корневой endpoint"""
    return {
        "message": "Добро пожаловать в API магазина электронной техники!",
        "docs": "/docs",
        "endpoints": {
            "products": "/products",
            "orders": "/orders",
            "inventory": "/inventory/stats"
        }
    }


@app.post("/products", status_code=status.HTTP_201_CREATED, tags=["Products"])
def create_product(product_req: ProductCreateRequest):
    """Создает новый товар"""
    try:
        product = create_product_from_request(product_req)
        product_id = inventory.add_product(product)
        return {
            "message": "Товар успешно создан",
            "product": product.to_dict()
        }
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@app.get("/products", tags=["Products"])
def get_all_products(
    category: Optional[ProductCategory] = None,
    available_only: bool = False,
    search: Optional[str] = None
):
    """Получает список всех товаров с фильтрацией"""
    try:
        if search:
            products = inventory.search_products(search)
        elif category:
            products = inventory.get_products_by_category(category)
        elif available_only:
            products = inventory.get_available_products()
        else:
            products = inventory.get_all_products()
        
        return {
            "count": len(products),
            "products": [p.to_dict() for p in products]
        }
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@app.get("/products/{product_id}", tags=["Products"])
def get_product(product_id: str):
    """Получает товар по ID"""
    product = inventory.get_product(product_id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Товар с ID {product_id} не найден"
        )
    return product.to_dict()


@app.patch("/products/{product_id}", tags=["Products"])
def update_product(product_id: str, update_req: ProductUpdateRequest):
    """Обновляет товар"""
    product = inventory.get_product(product_id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Товар с ID {product_id} не найден"
        )
    
    try:
        if update_req.name is not None:
            product.name = update_req.name
        if update_req.price is not None:
            product.price = update_req.price
        if update_req.description is not None:
            product.description = update_req.description
        if update_req.stock is not None:
            product.stock = update_req.stock
        if update_req.discount_percent is not None:
            product.discount_percent = update_req.discount_percent
        
        return {
            "message": "Товар успешно обновлен",
            "product": product.to_dict()
        }
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@app.delete("/products/{product_id}", tags=["Products"])
def delete_product(product_id: str):
    """Удаляет товар"""
    if inventory.remove_product(product_id):
        return {"message": f"Товар {product_id} успешно удален"}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Товар с ID {product_id} не найден"
    )


@app.post("/products/{product_id}/stock/add", tags=["Products"])
def add_stock(product_id: str, quantity: int = Field(..., gt=0)):
    """Добавляет товар на склад"""
    product = inventory.get_product(product_id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Товар с ID {product_id} не найден"
        )
    
    try:
        product.add_stock(quantity)
        return {
            "message": f"Добавлено {quantity} единиц товара",
            "new_stock": product.stock
        }
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@app.post("/products/category/{category}/discount", tags=["Products"])
def apply_category_discount(category: ProductCategory, discount: float = Field(..., ge=0, le=100)):
    """Применяет скидку ко всей категории товаров"""
    try:
        inventory.apply_discount_to_category(category, discount)
        affected_products = inventory.get_products_by_category(category)
        return {
            "message": f"Скидка {discount}% применена к категории {category.value}",
            "affected_products_count": len(affected_products),
            "products": [p.to_dict() for p in affected_products]
        }
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


# ============= ENDPOINTS - ЗАКАЗЫ =============

@app.post("/orders", status_code=status.HTTP_201_CREATED, tags=["Orders"])
def create_order(order_req: OrderCreateRequest):
    """Создает новый заказ"""
    try:
        order = Order(
            customer_name=order_req.customer_name,
            customer_email=order_req.customer_email
        )
        
        # Добавляем товары в заказ
        for item in order_req.items:
            product_id = item.get("product_id")
            quantity = item.get("quantity")
            
            if not product_id or not quantity:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Каждый элемент должен содержать product_id и quantity"
                )
            
            product = inventory.get_product(product_id)
            if not product:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"Товар с ID {product_id} не найден"
                )
            
            order.add_item(product, quantity)
        
        # Сохраняем заказ
        orders_storage[order.id] = order
        
        return {
            "message": "Заказ успешно создан",
            "order": order.to_dict()
        }
    
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@app.get("/orders", tags=["Orders"])
def get_all_orders(status_filter: Optional[OrderStatus] = None):
    """Получает список всех заказов"""
    orders = list(orders_storage.values())
    
    if status_filter:
        orders = [o for o in orders if o.status == status_filter]
    
    return {
        "count": len(orders),
        "orders": [o.to_dict() for o in orders]
    }


@app.get("/orders/{order_id}", tags=["Orders"])
def get_order(order_id: str):
    """Получает заказ по ID"""
    order = orders_storage.get(order_id)
    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Заказ с ID {order_id} не найден"
        )
    return order.to_dict()


@app.patch("/orders/{order_id}/status", tags=["Orders"])
def update_order_status(order_id: str, status_req: OrderStatusUpdateRequest):
    """Изменяет статус заказа"""
    order = orders_storage.get(order_id)
    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Заказ с ID {order_id} не найден"
        )
    
    try:
        order.change_status(status_req.status)
        return {
            "message": f"Статус заказа изменен на {status_req.status.value}",
            "order": order.to_dict()
        }
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@app.delete("/orders/{order_id}", tags=["Orders"])
def cancel_order(order_id: str):
    """Отменяет заказ"""
    order = orders_storage.get(order_id)
    if not order:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Заказ с ID {order_id} не найден"
        )
    
    try:
        order.cancel_order(inventory)
        return {
            "message": f"Заказ {order_id} отменен, товары возвращены на склад",
            "order": order.to_dict()
        }
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


# ============= ENDPOINTS - СТАТИСТИКА =============

@app.get("/inventory/stats", tags=["Inventory"])
def get_inventory_stats():
    """Получает статистику инвентаря"""
    all_products = inventory.get_all_products()
    available_products = inventory.get_available_products()
    
    # Статистика по категориям
    category_stats = {}
    for category in ProductCategory:
        products = inventory.get_products_by_category(category)
        category_stats[category.value] = {
            "count": len(products),
            "total_value": sum(p.price * p.stock for p in products)
        }
    
    return {
        "total_products": len(all_products),
        "available_products": len(available_products),
        "total_inventory_value": inventory.get_total_inventory_value(),
        "category_stats": category_stats
    }


@app.get("/orders/stats", tags=["Orders"])
def get_orders_stats():
    """Получает статистику заказов"""
    all_orders = list(orders_storage.values())
    
    # Статистика по статусам
    status_stats = {}
    for status_enum in OrderStatus:
        orders = [o for o in all_orders if o.status == status_enum]
        status_stats[status_enum.value] = {
            "count": len(orders),
            "total_revenue": sum(o.get_total() for o in orders)
        }
    
    total_revenue = sum(o.get_total() for o in all_orders)
    
    return {
        "total_orders": len(all_orders),
        "total_revenue": total_revenue,
        "status_stats": status_stats
    }


# ============= ИНИЦИАЛИЗАЦИЯ ТЕСТОВЫХ ДАННЫХ =============

@app.on_event("startup")
def startup_event():
    """Создает тестовые данные при запуске"""
    print("🚀 Запуск приложения...")
    print("📦 Создание тестовых данных...")
    
    # Создаем тестовые товары
    test_products = [
        Smartphone(
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
        ),
        Smartphone(
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
        ),
        Laptop(
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
        ),
        Tablet(
            name="iPad Air",
            price=54990,
            brand="Apple",
            screen_size=10.9,
            storage_gb=64,
            has_stylus=True,
            description="Планшет для работы и творчества",
            stock=25
        ),
        Cable(
            name="USB-C кабель",
            price=1990,
            cable_type="USB-C to USB-C",
            length_m=2.0,
            color="white",
            description="Быстрая зарядка и передача данных",
            stock=100
        ),
        Accessory(
            name="AirPods Pro",
            price=24990,
            accessory_type="headphones",
            compatible_with=["iPhone", "iPad", "MacBook"],
            description="Беспроводные наушники с шумоподавлением",
            stock=30
        )
    ]
    
    for product in test_products:
        inventory.add_product(product)
        print(f"  ✓ {product.name}")
    
    print(f"✅ Создано {len(test_products)} тестовых товаров")
    print("📚 Документация доступна по адресу: http://localhost:8000/docs")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
