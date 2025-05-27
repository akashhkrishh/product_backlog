from typing import List, Optional
from models import Order

class OrderData:
    def __init__(self):
        self.__orders: List[Order] = []
        self.initialize()

    def initialize(self):
        pass

    def get_all_orders(self) -> List[Order]:
        return self.__orders

    def get_order_by_id(self, order_id: int) -> Optional[Order]:
        for order in self.__orders:
            if order.order_id == order_id:
                return order
        return None

    def save_order(self, order: Order) -> bool:
        if self.get_order_by_id(order.order_id):
            return False
        self.__orders.append(order)
        return True

    def remove_order(self, order_id: int) -> bool:
        order = self.get_order_by_id(order_id)
        if order:
            self.__orders.remove(order)
            return True
        return False

    def update_status(self, order_id: int, new_status) -> bool:
        order = self.get_order_by_id(order_id)
        if order:
            order.status = new_status
            return True
        return False

    def get_orders_by_customer_id(self, customer_id: int) -> List[Order]:
        return [order for order in self.__orders if order.customer_id == customer_id]
