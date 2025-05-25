from databases import UserData, SessionData


class Database:
    def __init__(self):
        self.user = UserData()
        self.session = SessionData()
