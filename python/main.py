from configs import Database
from controllers import AuthController
from utils import console


def show_main_menu():
    console.clear()
    print("Main Menu")
    print("1. Login\n2. Register\n3. Exit")


def handle_user_choice(choice: int, auth_controller : AuthController):
    if choice == 1:
        auth_controller.login()
    elif choice == 2:
        auth_controller.register()
    elif choice == 3:
        exit(1)
    else:
        print("Invalid choice")


class Main:
    def __init__(self) -> None:
        self.__database: Database = Database()
        self.__auth_controller = AuthController(self.__database)

    def main(self) -> None:
        while True:
            try:
                show_main_menu()
                for i in self.__database.user.getUsers():
                    print(i)
                choice = int(input("Enter your choice: ").strip())
                handle_user_choice(choice,self.__auth_controller)
            except ValueError:
                print("Please enter a valid numeric option.")
            except (KeyboardInterrupt, EOFError):
                print("\nApplication interrupted. Press Enter to exit...")
                exit(0)

if __name__ == '__main__':
    app = Main()
    app.main()
