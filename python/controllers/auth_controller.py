from configs import Database
from controllers.customer_controller import CustomerController
from controllers.admin_controller import AdminController
from models import User
from payloads import GlobalResponse, AdminLoginRequest, CustomerLoginRequest
from services import AuthService
from utils import validate_name, validate_email, validate_mobile, validate_address, validate_password, \
    validate_confirm_password, console


def handle_register(user: User) -> User:
    print("User Registration")
    while True:
        name = input("Enter your name: ").strip()
        if validate_name(name):
            user.name = name
            break
        print("Name with minimum 3 or maximum 50 character")

    while True:
        email = input("Enter your email: ").strip()
        if validate_email(email):
            user.email = email
            break
        print("Invalid email. Must contain '@'.")

    while True:
        try:
            mobile = input("Enter your mobile: ").strip()
            if not mobile.isdigit():
                raise ValueError("Mobile number must contain only digits.")

            if validate_mobile(mobile):
                user.mobile = mobile
                break
            else:
                print("Mobile number must be exactly 10 digits.")
        except ValueError as e:
            print(f"Invalid input: {e}")

    while True:
        address = input("Enter Address: ").strip()
        if validate_address(address):
            user.address = address
            break
        else:
            print("Address must be between 1 and 300 characters.")

    while True:
        password = input("Enter Password: ").strip()
        if validate_password(password):
            confirm = input("Confirm Password: ").strip()
            if validate_confirm_password(password, confirm):
                user.password = password
                break
            else:
                print("Passwords do not match.")
        else:
            print("Password must contain lowercase, uppercase, and alphabet characters.")
    return user

def handle_admin_login(request: AdminLoginRequest) -> AdminLoginRequest:
    while True:
        email = input("Enter your email: ").strip()
        if validate_email(email):
            request.email = email
            break
        print("Invalid email. Must contain '@'.")

    while True:
        password = input("Enter your password: ").strip()
        if validate_password(password):
            request.password = password
            break
        print("Password must contain lowercase, uppercase, and alphabet characters.")
    return request

def handle_customer_login(request: CustomerLoginRequest) -> CustomerLoginRequest:
    while True:
        try:
            customerId = int(input("Enter your customerId: ").strip())
            request.customer_id = customerId
            break
        except ValueError:
            print("Invalid customer ID. Please enter a valid number.")

    while True:
        password = input("Enter your password: ").strip()
        if validate_password(password):
            request.password = password
            break
        print("Password must contain lowercase, uppercase, and alphabet characters.")
    return request

class AuthController:
    def __init__(self, database : Database) -> None:
        self.__database = database
        self.__auth_service = AuthService(self.__database)
        self.__admin_controller = AdminController(self.__database)
        self.__customer_controller = CustomerController(self.__database)

    def login(self) -> None:
        while True:
            print("Choose LoginType")
            print(f"1. Customer"
                  f"\n2. Admin"
                  f"\n3. Back to Main Menu"
                  )
            choice = int(input("Enter your choice: ").strip())
            if choice == 1:
                customerRequest = handle_customer_login(CustomerLoginRequest())
                response: GlobalResponse = self.__auth_service.loginUser(customerRequest)
                if response.status:
                    console.clear()
                    print(response.message)
                    self.__customer_controller.customerMenu()

                else:
                    print(response.message)
                    isContinue = input("\nWould you like to try again? (Y/N): ").lower()
                    if isContinue == "n":
                        console.clear()
                        break
                    console.clear()
            elif choice == 2:
                adminRequest = handle_admin_login(AdminLoginRequest())
                response: GlobalResponse = self.__auth_service.loginAdmin(adminRequest)
                if response.status:
                    console.clear()
                    print(response.message)
                    self.__admin_controller.adminMenu()
                else:
                    print(response.message)
                    isContinue = input("\nWould you like to try again? (Y/N): ").lower()
                    if isContinue == "n":
                        console.clear()
                        break
                    console.clear()
            elif choice == 3:
                break
            else:
                print("Invalid choice. Please try again.")


    def register(self) -> None:
        while True:
            newUser = handle_register(User())
            response: GlobalResponse = self.__auth_service.registerUser(newUser)
            if response.status:
                console.clear()
                print(response.message)
                print(f"Customer ID: {response.data.user_id}"
                      f"\nEmail: {response.data.email}"
                      f"\nMobile: {response.data.mobile}")
                console.pause()
                break
            else:
                print(response.message)
                isContinue = input("\nWould you like to try again? (Y/N): ").lower()
                if isContinue == "n":
                    console.clear()
                    break
                console.clear()
