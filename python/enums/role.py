from enum import Enum


class Role(Enum):
    ADMIN = "admin"
    CUSTOMER = "customer"

    def __str__(self) -> str:
        return self.value