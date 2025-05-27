from typing import List, Optional
from models import Product
from enums import Category

class ProductData:
    def __init__(self):
        self.__products: List[Product] = []
        self.initialize()

    def initialize(self):
        p1 = Product(
            name="Bluetooth Speaker",
            price=1999.99,
            category=Category.ELECTRONICS,
            description="Portable and waterproof"
        )
        p2 = Product(
            name="Wall Painting",
            price=799.50,
            category=Category.HOME_DECOR,
            description="Canvas artwork for home walls"
        )
        p3 = Product(
            name="Notebook Set",
            price=249.00,
            category=Category.STATIONARY,
            description="Pack of 3 ruled notebooks"
        )
        p4 = Product(
            name="Earphone",
            price=499.00,
            category=Category.ELECTRONICS,
            description="Wired in-ear earphones with mic"
        )
        p5 = Product(
            name="Laptop",
            price=54999.00,
            category=Category.ELECTRONICS,
            description="15.6 inch i5 laptop with 8GB RAM"
        )
        p6 = Product(
            name="TV",
            price=29999.00,
            category=Category.ELECTRONICS,
            description="43-inch 4K Ultra HD Smart LED TV"
        )
        p7 = Product(
            name="Mobile Phone",
            price=17999.00,
            category=Category.ELECTRONICS,
            description="6.5 inch smartphone with 128GB storage"
        )

        self.__products.extend([p1, p2, p3, p4, p5, p6, p7])

    def get_all_products(self) -> List[Product]:
        return self.__products

    def get_product_by_id(self, product_id: int) -> Optional[Product]:
        for product in self.__products:
            if product.product_id == product_id:
                return product
        return None

    def save_product(self, product: Product) -> bool:
        if any(p.name == product.name for p in self.__products):
            return False  # Prevent duplicate by name
        self.__products.append(product)
        return True

    def remove_product(self, product_id: int) -> bool:
        product = self.get_product_by_id(product_id)
        if product:
            self.__products.remove(product)
            return True
        return False

    def update_price(self, product_id: int, new_price: float) -> bool:
        product = self.get_product_by_id(product_id)
        if product:
            product.price = new_price
            return True
        return False

    def get_all_categories(self) -> List[Category]:
        categories = set(product.category for product in self.__products)
        return list(categories)
