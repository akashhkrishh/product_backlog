from databases import UserData, SessionData
from databases.order_data import OrderData
from databases.product_data import ProductData


class Database:
    def __init__(self):
        self.user = UserData()
        self.session = SessionData()
        self.product = ProductData()
        self.order = OrderData()
