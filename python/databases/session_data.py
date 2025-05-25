
from enums import Role
from models import User


class SessionData:
    def __init__(self):
        self.user: User | None = None
        self.role: Role | None = None
        self.session_id: int | None = None

    def getUser(self) -> User | None:
        return self.user

    def setSession(self, user: User):
        self.session_id = user.user_id
        self.user = user
        self.role = user.role

    def getRole(self) -> Role | None:
        return self.role

    def getSessionId(self) -> int | None:
        return self.session_id

    def getCurrentUser(self) -> User | None:
        return self.user