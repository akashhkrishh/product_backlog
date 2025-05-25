from configs import Database
from services import AdminService
from utils import console


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
                choice = int(input("Enter your choice: ").strip())

                if choice == 1:
                    self.adminService.handleAddProduct()
                elif choice == 2:
                    self.adminService.view()
                elif choice == 3:
                    self.adminService.updateProduct()
                elif choice == 4:
                    self.adminService.deleteProduct()
                elif choice == 5:
                    self.adminService.searchByProduct()
                elif choice == 6:
                    self.adminService.viewAllCustomers()
                elif choice == 7:
                    self.adminService.viewAllOrders()
                elif choice == 8:
                    self.adminService.searchByOrder()
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

