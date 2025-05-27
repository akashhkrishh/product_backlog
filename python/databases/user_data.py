from typing import List, Optional
from enums import Role
from models import User

class UserData:
    def __init__(self):
        self.__users: List[User] = []
        self.initialize()

    def initialize(self):
        admin = User("Admin", "admin@gmail.com", 9087589692, "India", "Admin@123", Role.ADMIN)
        customer = User("Akashh", "akashh@gmail.com", 9087589692, "India", "PassWord", Role.CUSTOMER)
        self.__users.extend([admin, customer])

    def getUsers(self) -> List[User]:
        return self.__users

    def saveUser(self, user: User) -> bool:
        self.__users.append(user)
        return True

    def removeUser(self, user: User) -> bool:
        self.__users.remove(user)
        return True

    def update_password(self, user_id: int, new_password: str) -> bool:
        for user in self.__users:
            if user.user_id == user_id:
                user.password = new_password
                return True
        return False

    def get_user_by_id(self, user_id: int) -> Optional[User]:
        for user in self.__users:
            if user.user_id == user_id:
                return user
        return None
