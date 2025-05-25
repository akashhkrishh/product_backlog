from configs import Database
from services import CustomerService

from utils import console


class CustomerController:
    def __init__(self, database: Database) -> None:
        self.__database = database
        self.customerService = CustomerService(self.__database)

    def customerMenu(self):
        while True:

            print("Customer Dashboard")
            print(f"1.View products\n"
                  f"2.Payment\n"
                  f"3.Previous orders\n"
                  f"4.View profile\n"
                  f"5.Logout"
                  )
            try:
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    self.customerService.viewProducts()
                elif choice == 2:
                    self.customerService.payment()
                elif choice == 3:
                    self.customerService.previousOrders()
                elif choice == 4:
                    self.customerService.viewProfile()
                elif choice == 5:
                    console.clear()
                    break
                else:
                    console.clear()
                    print("Invalid choice. Please try again.")

            except ValueError:
                console.clear()
                print("Please enter a valid number.")

