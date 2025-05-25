from configs import Database
from models import User
from repositories import UserRepo
from utils import validate_password


class CustomerService:
    def __init__(self, database:Database) -> None:
        self.__database = database
        self.__user_repo = UserRepo(database)

    def viewProducts(self):
        pass

    def payment(self):
        pass

    def previousOrders(self):
        pass

    def viewProfile(self):
        user:User = self.__database.session.getCurrentUser()
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
                        print("Password didn't updated")
                    break
                print("Password must contain lowercase, uppercase, and alphabet characters.")
        else:
            return