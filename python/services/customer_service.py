from collections import defaultdict
from models import User, Order  # Make sure Order model exists
from utils import (
    validate_card_number,
    validate_card_holder_name,
    validate_expiry_date,
    validate_cvv,
    validate_password,
)
from repositories import OrderRepo, UserRepo
from enums import OrderStatus


class CustomerService:
    def __init__(self, database):
        self.__database = database
        self.__user_repo = UserRepo(database)   # Initialize user repo here
        self.cart = defaultdict(int)
        self.__order_repo = OrderRepo(database)

    def viewProducts(self):
        categories = list(self.__database.product.get_all_categories())
        print("Categories:")
        for idx, cat in enumerate(categories, start=1):
            print(f"{idx}. {cat.name.title()}")

        try:
            cat_choice = int(input("Select category number (0 to cancel): ").strip())
            if cat_choice == 0:
                return
            selected_cat = categories[cat_choice - 1]
        except (ValueError, IndexError):
            print("Invalid category choice.")
            return

        products = [p for p in self.__database.product.get_all_products() if p.category == selected_cat]
        if not products:
            print("No products found in this category.")
            return

        print(f"\nProducts in {selected_cat.name.title()}:")
        print("-" * 100)
        print(f"{'Product ID':<12} | {'Product Name':<20} | {'Price ($)':<10} | Description")
        print("-" * 100)

        for p in products:
            print(f"{str(p.product_id).center(12)} | {p.name:<20} | ${p.price:<9.2f} | {p.description}")

        print("-" * 100)

        try:
            pid = int(input("Enter product ID to add to cart (0 to cancel): ").strip())
            if pid == 0:
                return
            product = next((prod for prod in products if prod.product_id == pid), None)
            if not product:
                print("Invalid product ID.")
                return
            qty = int(input("Enter quantity: ").strip())
            if qty <= 0:
                print("Quantity must be positive.")
                return
            self.add_to_cart(pid, qty)
            print(f"Added {qty} x {product.name} to cart.")
        except ValueError:
            print("Invalid input.")

    def add_to_cart(self, product_id: int, quantity: int):
        self.cart[product_id] += quantity

    def view_cart(self):
        if not self.cart:
            print("Your cart is empty.")
            return

        print("\nYour Cart:")
        print("-" * 90)
        print(f"{'Product ID':<12} | {'Product Name':<20} | {'Quantity':<10} | {'Price (₹)':<12} | Line Total")
        print("-" * 90)

        total = 0.0
        for pid, qty in self.cart.items():
            product = next((p for p in self.__database.product.get_all_products() if p.product_id == pid), None)
            if product:
                line_total = product.price * qty
                total += line_total
                print(f"{pid:<12} | {product.name:<20} | {qty:<10} | ₹{product.price:<11.2f} | ₹{line_total:.2f}")
        print("-" * 90)
        print(f"{'Total Amount:':>70} ₹{total:.2f}")

    def remove_from_cart(self):
        if not self.cart:
            print("Your cart is empty.")
            return
        try:
            pid = int(input("Enter product ID to remove from cart: ").strip())
            if pid in self.cart:
                del self.cart[pid]
                print("Product removed from cart.")
            else:
                print("Product not found in cart.")
        except ValueError:
            print("Invalid input.")

    def checkout(self):
        if not self.cart:
            print("Your cart is empty. Add products before checkout.")
            return

        total = 0.0
        products_to_buy = []
        for pid, qty in self.cart.items():
            product = next((p for p in self.__database.product.get_all_products() if p.product_id == pid), None)
            if product:
                total += product.price * qty
                products_to_buy.append((product, qty))

        print("\nCheckout Summary:")
        print("-" * 90)
        print(f"{'Product ID':<12} | {'Product Name':<20} | {'Quantity':<10} | {'Price (₹)':<12} | Line Total")
        print("-" * 90)
        for product, qty in products_to_buy:
            line_total = product.price * qty
            print(
                f"{product.product_id:<12} | {product.name:<20} | {qty:<10} | ₹{product.price:<11.2f} | ₹{line_total:.2f}")
        print("-" * 90)
        print(f"{'Total amount to pay:':>70} ₹{total:.2f}")
        print("\nEnter payment details:")

        while True:
            card_no = input("Card Number (16 digits): ").strip()
            if validate_card_number(card_no):
                break
            print("Invalid card number. Please enter a 16-digit numeric card number.")

        while True:
            card_holder = input("Card Holder Name (min 10 chars): ").strip()
            if validate_card_holder_name(card_holder):
                break
            print("Invalid name. Minimum 10 characters required.")

        while True:
            expiry = input("Expiry Date (MM/YY): ").strip()
            if validate_expiry_date(expiry):
                break
            print("Invalid expiry date format or expired.")

        while True:
            cvv = input("CVV (3 digits): ").strip()
            if validate_cvv(cvv):
                break
            print("Invalid CVV. Must be a 3-digit number.")

        print("Processing payment...")
        print("Payment successful!")

        user: User = self.__database.session.getCurrentUser()

        order = Order(
            customer_id=user.user_id,
            products=products_to_buy,  # list of (Product, quantity) tuples
            status=OrderStatus.CONFIRMED,
        )

        saved = self.__order_repo.saveOrder(order)
        if saved:
            print("\nOrder placed successfully!")
            print("-" * 50)
            print(f"Order ID     : {order.order_id}")
            print(f"Amount Paid  : ${total:.2f}")
            print("-" * 50)
            print("Thank you for shopping with us!")
            self.cart.clear()
        else:
            print("\nFailed to save order. Please contact support.")

    def payment(self):
        self.checkout()

    def viewOrdersByStatus(self):
        user: User = self.__database.session.getCurrentUser()
        orders = self.__order_repo.getOrdersByCustomerId(user.user_id)

        if not orders:
            print("No previous orders found.")
            return

        while True:
            print("\nView Orders by Status:")
            print("1) Confirmed orders")
            print("2) In Transit")
            print("3) Delivered")
            print("4) Cancelled")
            print("5) Exit")

            choice = input("Select an option: ").strip()

            status_map = {
                "1": OrderStatus.CONFIRMED,
                "2": OrderStatus.IN_TRANSIT,
                "3": OrderStatus.DELIVERED,
                "4": OrderStatus.CANCELLED
            }

            if choice == "5":
                print("Exiting order history view...")
                break

            selected_status = status_map.get(choice)
            if not selected_status:
                print("Invalid choice. Please select a valid option.")
                continue

            filtered_orders = [o for o in orders if o.status == selected_status]

            if not filtered_orders:
                print(f"No orders found with status '{selected_status.name.title()}'.")
            else:
                print(f"\nOrders with status '{selected_status.name.title()}':")
                print("-" * 80)
                print(f"{'Order ID':<14} | {'Customer Name':<20} | {'Total Items':<12} | {'Status':<15}")
                print("-" * 80)
                for order in filtered_orders:
                    customer = self.__database.user.get_user_by_id(order.customer_id)
                    total_items = sum(qty for _, qty in order.products)  # assuming products is list of (Product, qty)
                    print(
                        f"{order.order_id:<14} | {customer.name:<20} | {total_items:<12} | {order.status.name.title():<15}")
                print("-" * 80)

    def previousOrders(self):
        self.viewOrdersByStatus()

    def viewProfile(self):
        user: User = self.__database.session.getCurrentUser()
        print(f"Customer ID: {user.user_id}\n"
              f"Name: {user.name}\n"
              f"Email: {user.email}\n"
              f"Update Password (Y / N): ", end="")
        choice = input().lower()
        if choice == "y":
            while True:
                newPassword = input("Enter your new Password: ")
                if validate_password(newPassword):
                    if self.__user_repo.updatePassword(user.user_id, newPassword):
                        print("Password updated successfully")
                    else:
                        print("Password didn't update")
                    break
                print("Password must contain lowercase, uppercase, and alphabet characters.")
        else:
            return
