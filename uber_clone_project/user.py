class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.is_authenticated = False

    def authenticate(self, username, password):
        if self.username == username and self.password == password:
            self.is_authenticated = True
        return self.is_authenticated

    def get_authentication_status(self):
        return self.is_authenticated