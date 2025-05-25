from enums import Role
from utils import random_number_generator_7digits


class User:
    def __init__(
            self,
            name: str = "",
            email: str = "",
            mobile: int = "",
            address: str = "",
            password: str = "",
            role: Role = Role.CUSTOMER
    ):
        self.user_id = random_number_generator_7digits()
        self.name = name
        self.email = email
        self.mobile = mobile
        self.address = address
        self.password = password
        self.role = role

    def __str__(self):
        return (f"{self.user_id} "
                f"{self.name} "
                f"{self.email} "
                f"{self.mobile} "
                f"{self.address} "
                f"{self.role}")
