from typing import List
from configs import Database
from models import Order

class OrderRepo:
    def __init__(self, database: Database) -> None:
        self.__database = database

    def getAllOrders(self) -> List[Order]:
        return self.__database.order.get_all_orders()

    def getOrderById(self, order_id: int) -> Order | None:
        orders = self.getAllOrders()
        for order in orders:
            if order.order_id == order_id:
                return order
        return None

    def getOrdersByCustomerId(self, customer_id: int) -> List[Order]:
        orders = self.getAllOrders()
        customer_orders = []
        for order in orders:
            if order.customer_id == customer_id:
                customer_orders.append(order)
        return customer_orders

    def saveOrder(self, order: Order) -> bool:
        return self.__database.order.save_order(order)

    def removeOrder(self, order: Order) -> bool:
        return self.__database.order.delete_order(order)

    def updateOrder(self, updated_order: Order) -> bool:
        orders = self.getAllOrders()
        for idx, order in enumerate(orders):
            if order.order_id == updated_order.order_id:
                orders[idx] = updated_order
                return True
        return False
