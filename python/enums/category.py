from enum import Enum

class Category(Enum):
    ELECTRONICS = "Electronics"
    HOME_DECOR = "Home Decor"
    STATIONARY = "Stationary"

    def __str__(self) -> str:
        return self.value