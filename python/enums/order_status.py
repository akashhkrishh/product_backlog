from enum import Enum

class OrderStatus(Enum):
    CONFIRMED = "Confirmed"
    IN_TRANSIT = "In Transit"
    DELIVERED = "Delivered"
    CANCELLED = "Cancelled"

    def __str__(self)->str:
        return self.value