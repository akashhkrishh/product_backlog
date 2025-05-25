
class CustomerLoginRequest:
    def __init__(
            self,
            customer_id: int = None,
            password: str = "",
    ) -> None:
        self.customer_id = customer_id
        self.password = password