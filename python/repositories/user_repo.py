from typing import List
from configs import Database
from enums import Role
from models import User


class UserRepo:
    def __init__(self, database: Database) -> None:
        self.__database = database

    def getCustomer(self) -> List[User] :
        users = self.__database.user.getUsers()
        adminUsers = []
        for user in users:
            if user.role == Role.CUSTOMER:
                adminUsers.append(user)
        return adminUsers

    def getUserByEmail(self, email: str) -> User | None:
        users = self.getCustomer()
        for user in users:
            if user.email == email:
                return user
        else:
            return None

    def getUserById(self, user_id: int) -> User | None:
        users = self.getCustomer()
        for user in users:
            if user.user_id == user_id:
                return user
        else:
            return None

    def saveUser(self, user: User) -> bool:
        return self.__database.user.saveUser(user)

    def removeUser(self, user: User) -> bool:
        return self.__database.user.deleteUser(user)

    def getAdminUsers(self) -> List[User] | None:
        users = self.__database.user.getUsers()
        adminUsers = []
        for user in users:
            if user.role == Role.ADMIN:
                adminUsers.append(user)
        return adminUsers

    def updatePassword(self, user_id, newPassword) -> bool:
        return self.__database.user.update_password(user_id, newPassword)


