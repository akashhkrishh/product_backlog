from configs import Database
from services import AdminService
from utils import console
from enums import Category, OrderStatus


class AdminController:
    def __init__(self, database: Database) -> None:
        self.__database = database
        self.adminService = AdminService(self.__database)

    def adminMenu(self):
        while True:
            print("Admin Dashboard")
            print(
                "1. Add Product\n"
                "2. View Products\n"
                "3. Update a Product\n"
                "4. Delete a Product\n"
                "5. Search by Product\n"
                "6. View All Customers\n"
                "7. View All Orders\n"
                "8. Search by Order\n"
                "9. Logout"
            )
            try:
                choice = int(input("Enter your choice: "))
                print(choice)
                if choice == 1:
                    print("Add Product")
                    self.add_product()
                elif choice == 2:
                    self.adminService.viewAllProducts()
                elif choice == 3:
                    self.update_product()
                elif choice == 4:
                    self.delete_product()
                elif choice == 5:
                    self.search_by_product()
                elif choice == 6:
                    self.adminService.viewAllCustomers()
                elif choice == 7:
                    self.adminService.viewAllOrders()
                elif choice == 8:
                    self.search_by_order()
                elif choice == 9:
                    console.clear()
                    print("Logged out successfully.")
                    break
                else:
                    console.clear()
                    print("Invalid choice. Please try again.")

            except ValueError:
                console.clear()
                print("Please enter a valid number.")

    def add_product(self):
        name = input("Enter product name: ").strip()
        price = float(input("Enter product price: ").strip())

        # Show categories list and ask for category
        print("Choose category:")
        for idx, cat in enumerate(Category):
            print(f"{idx + 1}. {cat.name.title()}")
        cat_choice = int(input("Enter category number: ").strip())
        category = list(Category)[cat_choice - 1]

        description = input("Enter product description: ").strip()

        success = self.adminService.handleAddProduct(name, price, category, description)
        if success:
            print("Product added successfully.")
        else:
            print("Failed to add product. Possibly duplicate name.")

    def update_product(self):
        product_id = int(input("Enter product ID to update: ").strip())

        print("Leave input blank if no change is needed.")

        name = input("Enter new name (or press Enter to skip): ").strip()
        name = name if name else None

        price_input = input("Enter new price (or press Enter to skip): ").strip()
        price = float(price_input) if price_input else None

        print("Choose new category (or press Enter to skip):")
        for idx, cat in enumerate(Category):
            print(f"{idx + 1}. {cat.name.title()}")
        cat_choice_input = input("Enter category number or press Enter to skip: ").strip()
        category = list(Category)[int(cat_choice_input) - 1] if cat_choice_input else None

        description = input("Enter new description (or press Enter to skip): ").strip()
        description = description if description else None

        updated = self.adminService.updateProduct(product_id, name, price, category, description)
        if updated:
            print("Product updated successfully.")
        else:
            print("Product not found or update failed.")

    def delete_product(self):
        product_id = int(input("Enter product ID to delete: ").strip())
        deleted = self.adminService.deleteProduct(product_id)
        if deleted:
            print("Product deleted successfully.")
        else:
            print("Product not found.")

    def search_by_product(self):
        pID = int(input("Enter product id to search products: "))
        results = self.adminService.searchByProduct(pID)
        if results:
            print(f"Found {len(results)} product(s):")
            for product in results:
                print(product)
        else:
            print("No products found matching the keyword.")

    def search_by_order(self):
        try:
            order_id = int(input("Enter Order ID to search: ").strip())
        except ValueError:
            print("Invalid input. Order ID must be a number.")
            return

        order = self.adminService.searchByOrderId(order_id)
        if order:
            customer = self.__database.user.get_user_by_id(order.customer_id)
            if not customer:
                print("Customer not found for this order.")
                return

            print("\nOrder Details")
            print("-" * 100)
            print(f"{'Order ID':<14} | {'Customer Name':<20} | {'Email':<25} | {'Mobile':<15} | Address")
            print("-" * 100)
            print(f"{order.order_id:<14} | {customer.name:<20} | {customer.email:<25} | "
                  f"{customer.mobile:<15} | {customer.address}")
            print("-" * 100)

            print("\nOrdered Products")
            print(f"{'Product Name':<25} | {'Qty':<5} | {'Unit Price':<12} | {'Total Price'}")
            print("-" * 100)

            grand_total = 0.0
            for product, qty in order.products:
                total_price = product.price * qty
                grand_total += total_price
                print(f"{product.name:<40} | {qty:<5} | ${product.price:<11.2f} | ${total_price:.2f}")

            print("-" * 100)
            print(f"{'Grand Total':<40} ${grand_total:.2f}")
            print("-" * 100)
        else:
            print(f"No order found with ID {order_id}.")
