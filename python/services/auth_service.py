from configs import Database
from enums import Role
from models import User
from payloads import AdminLoginRequest, CustomerLoginRequest
from payloads.global_response import GlobalResponse
from repositories import UserRepo


class AuthService:
    def __init__(self, database: Database) -> None:
        self.__database = database
        self.__user_repo = UserRepo(self.__database)

    def loginAdmin(self, request: AdminLoginRequest) -> GlobalResponse:
        adminUsers = self.__user_repo.getAdminUsers()
        for user in adminUsers:
            if user.email == request.email:
                if user.password == request.password:
                    self.__database.session.setSession(user)
                    return GlobalResponse(user, True, "Admin login successful")
                else:
                    return GlobalResponse(None, False, "Invalid password")

        return GlobalResponse(None, False, "Admin not found")

    def loginUser(self, request: CustomerLoginRequest) -> GlobalResponse:
        user = self.__user_repo.getUserById(request.customer_id)

        if user:
            if user.password == request.password:
                self.__database.session.setSession(user)
                return GlobalResponse(user, True, "Customer login successful")
            else:
                return GlobalResponse(None, False, "Invalid password")

        return GlobalResponse(None, False, "Customer not found")


    def registerUser(self, newUser: User) -> GlobalResponse:
        users = self.__user_repo.getUserByEmail(newUser.email)
        if users:
            return GlobalResponse(None,False,"User with this email already exists")
        self.__user_repo.saveUser(newUser)
        return GlobalResponse(newUser,True,"User registered")

