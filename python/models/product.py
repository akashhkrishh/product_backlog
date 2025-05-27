import random
from enums import Category
from utils import random_number_generator_3digits


class Product:
    existing_ids = set()

    def __init__(
        self,
        name: str,
        price: float,
        category: Category,
        description: str = ""
    ):
        self.product_id = random_number_generator_3digits()
        self.name = name
        self.price = float(price)
        self.category = category
        self.description = description

    def __str__(self):
        return (f"Product ID: {self.product_id}, "
                f"Name: {self.name}, "
                f"Price: ₹{self.price:.2f}, "
                f"Category: {self.category.value}, "
                f"Description: {self.description}")
