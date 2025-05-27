from configs import Database
from models import Product
from enums import Category
from typing import Optional, Union, List


class AdminService:
    def __init__(self, database: Database) -> None:
        self.__database = database

    def searchByProduct(self, query: Union[str, int]) -> List[Product]:
        products = self.__database.product.get_all_products()

        if isinstance(query, int):
            return [product for product in products if product.product_id == query]
        else:
            keyword_lower = query.lower()
            return [
                product for product in products
                if keyword_lower in product.name.lower() or keyword_lower in product.description.lower()
            ]

    def deleteProduct(self, product_id: int) -> bool:
        return self.__database.product.remove_product(product_id)

    def updateProduct(self, product_id: int, name: Optional[str] = None,
                      price: Optional[float] = None,
                      category: Optional[Category] = None,
                      description: Optional[str] = None) -> bool:
        product = self.__database.product.get_product_by_id(product_id)
        if product:
            if name: product.name = name
            if price is not None: product.price = price
            if category: product.category = category
            if description: product.description = description
            return True
        return False

    def handleAddProduct(self, name: str, price: float,
                         category: Category, description: str) -> bool:
        from models import Product
        new_product = Product(name=name, price=price, category=category, description=description)
        return self.__database.product.save_product(new_product)

    def viewAllProducts(self) -> None:
        print("-" * 120)
        print("All Products".center(120), end="\n")
        print("-" * 120)
        print(f"{'Product ID':<12} | {'Product Name':<20} | {'Price ($)':<12} | {'Category':<20} | Description")
        print("-" * 120)

        products = self.__database.product.get_all_products()
        if not products:
            print("No products available.")
        else:
            for product in products:
                print(
                    f"{str(product.product_id).center(12)} | {product.name:<20} | ${product.price:<11.2f} | {product.category.name:<20} | {product.description}")

        print("-" * 120)

    def viewAllCustomers(self) -> None:
        print("-" * 100)
        print("All Customers".center(100), end="\n")
        print("-" * 100)
        print(f"{'Customer ID':<14} | {'Customer Name':<20} | {'Email':<25} | {'Mobile':<15} | Address")
        print("-" * 100)

        found = False
        for user in self.__database.user.getUsers():
            if user.role.name == "CUSTOMER":
                found = True
                print(f"{user.user_id:<14} | {user.name:<20} | {user.email:<25} | {user.mobile:<15} | {user.address}")

        if not found:
            print("No customers found.")

        print("-" * 100)

    def viewAllOrders(self) -> None:
        orders = self.__database.order.get_all_orders()
        if not orders:
            print("No orders found.")
            return

        print("\nAll Orders")
        print("-" * 100)
        print(f"{'Order ID':<14} | {'Customer Name':<20} | {'Email':<25} | {'Mobile':<15} | Address")
        print("-" * 100)

        for order in orders:
            customer = self.__database.user.get_user_by_id(order.customer_id)
            print(
                f"{order.order_id:<14} | {customer.name:<20} | {customer.email:<25} | {customer.mobile:<15} | {customer.address}")
        print("-" * 100)

    def searchByOrderId(self, order_id: int):
        orders = self.__database.order.get_all_orders()
        for order in orders:
            if order.order_id == order_id:
                return order  # Return the single order matching order_id
        return None  # Return None if not found
