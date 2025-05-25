
class AdminLoginRequest:
    def __init__(
            self,
            email: str = "",
            password: str = "",
    ) -> None:
        self.email = email
        self.password = password

    def __str__(self):
        return f"email: {self.email}\npassword: {self.password}"

