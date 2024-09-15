class Store:
    def __init__(self, brand, address):
        self.brand = brand
        self.address = address
        self.items = {}

    def add_item(self, name, price):
        self.items[name] = price

    def remove_item(self,name):
        if name not in self.items:
            print('Товар не найден')
        else:
            self.items.pop(name)
            print('Товар удален')

    def get_price(self, item_name):
        """Возвращает цену товара по его названию. Если товара нет, возвращает None."""
        return self.items.get(item_name, None)

    def get_price(self, name):
        if name not in self.items:
            print('Товар не найден')
        else:
            return self.items.get(name, None)

    def update_price(self, name, new_price):
        if name not in self.items:
            print('Товар не найден')
        else:
            self.items[name] = new_price
            print('Товар обновлен')


store1 = Store("Пятерочка", "Советская 25")
store2 = Store("Десяточка", "Ленина 14")
store3 = Store("Дикси", "Якиманиха 8")

# Добавление товаров в магазины
store1.add_item("apples", 0.5)
store1.add_item("bananas", 0.75)

store2.add_item("laptop", 1000)
store2.add_item("headphones", 150)

store3.add_item("t-shirt", 20)
store3.add_item("jeans", 40)

# Тестирование магазина store1
print(f"Реквизиты магазина {store1.brand}: {store1.address}")
print(f'Товары магазина {store1.brand}: {store1.items}')
# Добавление товара
store1.add_item("oranges", 0.85)
print(f"После добавления товара: {store1.items}")

# Обновление цены товара
store1.update_price("bananas", 0.8)
print(f"После обновления цены натовар: {store1.items}")

# Удаление товара
store1.remove_item("apples")
print(f"После удаления товара: {store1.items}")

# Получение цены товара
price = store1.get_price("bananas")
print(f"Цена на товар bananas: {price}")

# Попытка получения цены несуществующего товара
price = store1.get_price("apples")

