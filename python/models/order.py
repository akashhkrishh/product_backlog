from typing import List, Tuple
from enums import OrderStatus
from models.product import Product
from utils import random_number_generator_12digits


class Order:
    def __init__(
        self,
        customer_id: int,
        products: List[Tuple[Product, int]],  # list of (Product, quantity) tuples
        status: OrderStatus = OrderStatus.CONFIRMED
    ):
        self.order_id = random_number_generator_12digits()
        self.customer_id = customer_id
        self.products = products
        self.status = status
        # Calculate total considering quantity
        self.total = sum(product.price * qty for product, qty in products)

    def __str__(self):
        product_list = ', '.join([f"{p.name} x{qty}" for p, qty in self.products])
        return (f"Order ID: {self.order_id}\n"
                f"Customer ID: {self.customer_id}\n"
                f"Products: {product_list}\n"
                f"Total: ₹{self.total:.2f}\n"
                f"Status: {self.status.value}")
