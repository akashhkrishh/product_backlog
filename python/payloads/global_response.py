from typing import  TypeVar, Optional

T = TypeVar("T")

class GlobalResponse():

    def __init__(
            self,
            data: Optional[T] = None,
            status: bool = True,
            message: str = ""
    ):
        self.data: Optional[T] = data
        self.status: bool = status
        self.message: str = message

    def __str__(self):
        return (f"Response("
                f"status={self.status}, "
                f"message='{self.message}', "
                f"data={self.data})"
        )
